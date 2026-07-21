from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript" / "submission_main.tex"
HIGHLIGHTS = ROOT / "submission" / "biosystems" / "highlights.txt"
BIB = ROOT / "library" / "references.bib"
PDF = ROOT / "output" / "pdf" / "icp_biosystems_submission.pdf"
SECTIONS = ROOT / "manuscript" / "sections"
SUPPORT = ROOT / "submission" / "biosystems"
ARCHIVE = ROOT / "output" / "submission" / "icp_biosystems_sources.zip"
ARCHIVE_SHA256 = ARCHIVE.with_suffix(".zip.sha256")
PDF_SHA256 = PDF.with_suffix(".pdf.sha256")
MANIFEST = (
    ROOT / "output" / "submission" / "icp_biosystems_build_manifest.json"
)
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
BUILD_INPUTS = (
    ROOT / "Makefile",
    ROOT / "scripts" / "package_icp_submission.py",
    ROOT / "scripts" / "validate_icp_submission.py",
)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL ICP submission validation: {message}")


def tex_words(text: str) -> list[str]:
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", text)
    text = re.sub(r"[{}$\\]", " ", text)
    return re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text)


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        fail(f"path escapes repository: {path}")


def without_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def referenced_sources(main_text: str) -> list[Path]:
    queue: list[tuple[Path, str]] = [(MAIN, main_text)]
    found: dict[str, Path] = {}
    sections_root = SECTIONS.resolve()
    while queue:
        _, source_text = queue.pop(0)
        for reference in INPUT_RE.findall(without_comments(source_text)):
            path = ROOT / reference
            if path.suffix == "":
                path = path.with_suffix(".tex")
            resolved = path.resolve()
            try:
                resolved.relative_to(sections_root)
            except ValueError:
                fail(
                    "referenced TeX input is outside manuscript/sections: "
                    f"{reference}"
                )
            if not resolved.is_file():
                fail(f"missing input source: {relative(resolved)}")
            name = relative(resolved)
            if name not in found:
                found[name] = resolved
                queue.append((resolved, resolved.read_text(encoding="utf-8")))
    return [found[name] for name in sorted(found)]


def expanded_sources(main_text: str, sources: list[Path]) -> str:
    chunks = [main_text]
    chunks.extend(path.read_text(encoding="utf-8") for path in sources)
    return "\n".join(chunks)


def package_inputs(sources: list[Path]) -> list[Path]:
    if not SUPPORT.is_dir():
        fail(f"missing support directory: {relative(SUPPORT)}")
    support_files: list[Path] = []
    for path in sorted(SUPPORT.rglob("*")):
        if path.is_symlink():
            fail(f"support package contains a symlink: {relative(path)}")
        if path.is_file():
            support_files.append(path)

    files: dict[str, Path] = {}
    for path in (MAIN, *sources, BIB, *support_files):
        if not path.is_file():
            fail(f"missing package input: {relative(path)}")
        name = relative(path)
        lowered = name.lower()
        if "/figures/" in lowered or Path(name).suffix.lower() in {
            ".pdf",
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".svg",
            ".eps",
        }:
            fail(f"artwork is not permitted in the source package: {name}")
        files[name] = path
    return [files[name] for name in sorted(files)]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_record(path: Path) -> dict[str, object]:
    return {
        "path": relative(path),
        "sha256": sha256_file(path),
        "size_bytes": path.stat().st_size,
    }


def git_output(*arguments: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.rstrip("\n")


def git_metadata(paths: list[Path]) -> dict[str, object]:
    commit = git_output("rev-parse", "HEAD")
    if commit is None:
        return {
            "available": False,
            "branch": None,
            "commit": None,
            "source_status_porcelain": [],
            "source_tree_dirty": None,
        }
    branch = git_output("symbolic-ref", "--quiet", "--short", "HEAD")
    status = git_output(
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
        "--",
        *(relative(path) for path in paths),
    )
    status_lines = sorted(status.splitlines()) if status else []
    return {
        "available": True,
        "branch": branch,
        "commit": commit,
        "source_status_porcelain": status_lines,
        "source_tree_dirty": bool(status_lines),
    }


def validate_checksum(checksum_path: Path, target: Path) -> None:
    if not checksum_path.is_file():
        fail(f"missing checksum: {relative(checksum_path)}")
    expected = f"{sha256_file(target)}  {target.name}\n"
    if checksum_path.read_text(encoding="ascii") != expected:
        fail(f"checksum does not match artifact: {relative(target)}")


def validate_artifacts(sources: list[Path]) -> None:
    for artifact in (ARCHIVE, ARCHIVE_SHA256, PDF_SHA256, MANIFEST):
        if not artifact.is_file() or artifact.stat().st_size == 0:
            fail(f"missing or empty artifact: {relative(artifact)}")

    inputs = package_inputs(sources)
    expected_names = [relative(path) for path in inputs]
    with zipfile.ZipFile(ARCHIVE, "r") as archive:
        entries = archive.infolist()
        names = [entry.filename for entry in entries]
        if names != expected_names:
            fail("source ZIP members do not exactly match sorted package inputs")
        if len(names) != len(set(names)):
            fail("source ZIP contains duplicate members")
        for entry, path in zip(entries, inputs):
            if entry.is_dir():
                fail(f"source ZIP contains directory entry: {entry.filename}")
            if entry.date_time != ZIP_TIMESTAMP:
                fail(f"source ZIP timestamp is not deterministic: {entry.filename}")
            if entry.compress_type != zipfile.ZIP_DEFLATED:
                fail(f"source ZIP member is not deflated: {entry.filename}")
            if (entry.external_attr >> 16) != 0o100644:
                fail(f"source ZIP permissions are not canonical: {entry.filename}")
            if sha256_bytes(archive.read(entry)) != sha256_file(path):
                fail(f"source ZIP member differs from repository: {entry.filename}")

    validate_checksum(ARCHIVE_SHA256, ARCHIVE)
    validate_checksum(PDF_SHA256, PDF)

    try:
        manifest_text = MANIFEST.read_text(encoding="utf-8")
        manifest = json.loads(manifest_text)
    except (OSError, json.JSONDecodeError) as error:
        fail(f"invalid build manifest: {error}")
    canonical = json.dumps(
        manifest, indent=2, sort_keys=True, ensure_ascii=False
    ) + "\n"
    if manifest_text != canonical:
        fail("build manifest is not canonical JSON")
    if manifest.get("schema_version") != 1:
        fail("unsupported build manifest schema")
    if manifest.get("manifest_path") != relative(MANIFEST):
        fail("build manifest records the wrong manifest path")

    expected_archive = {
        "fixed_member_timestamp": "1980-01-01T00:00:00Z",
        "format": "zip",
        "members": expected_names,
    }
    if manifest.get("archive") != expected_archive:
        fail("build manifest archive metadata is stale")

    expected_inputs = [file_record(path) for path in inputs]
    if manifest.get("inputs") != expected_inputs:
        fail("build manifest input hashes are stale")
    expected_build_inputs = [file_record(path) for path in sorted(BUILD_INPUTS)]
    if manifest.get("build_inputs") != expected_build_inputs:
        fail("build manifest build-input hashes are stale")
    expected_artifacts = [
        {
            **file_record(ARCHIVE),
            "checksum_file": relative(ARCHIVE_SHA256),
        },
        {
            **file_record(PDF),
            "checksum_file": relative(PDF_SHA256),
        },
    ]
    if manifest.get("artifacts") != expected_artifacts:
        fail("build manifest artifact hashes are stale")
    expected_git = git_metadata([*inputs, *BUILD_INPUTS])
    if manifest.get("git") != expected_git:
        fail("build manifest Git metadata is stale")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifacts",
        action="store_true",
        help="also verify the deterministic source ZIP, checksums, and manifest",
    )
    arguments = parser.parse_args()

    main_text = MAIN.read_text(encoding="utf-8")
    abstract_match = re.search(
        r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main_text, re.DOTALL
    )
    if abstract_match is None:
        fail("abstract not found")
    abstract_words = tex_words(abstract_match.group(1))
    if len(abstract_words) > 250:
        fail(f"abstract has {len(abstract_words)} words; maximum is 250")

    keyword_match = re.search(r"\\textbf\{Keywords:\}(.*?)(?:\n\n|\\linenumbers)", main_text, re.DOTALL)
    if keyword_match is None:
        fail("keywords not found")
    keyword_count = len([item for item in keyword_match.group(1).split(";") if item.strip()])
    if not 1 <= keyword_count <= 7:
        fail(f"found {keyword_count} keywords; BioSystems permits 1-7")

    highlights = [line[2:].strip() for line in HIGHLIGHTS.read_text(encoding="utf-8").splitlines() if line.startswith("- ")]
    if not 3 <= len(highlights) <= 5:
        fail(f"found {len(highlights)} highlights; expected 3-5")
    too_long = [(item, len(item)) for item in highlights if len(item) > 85]
    if too_long:
        fail(f"highlight exceeds 85 characters: {too_long[0]}")

    for required in (
        "Data and code availability",
        "Ethics statement",
        "Funding",
        "Declaration of competing interests",
        "CRediT author statement",
        "Declaration of generative AI and AI-assisted technologies",
    ):
        if required not in main_text:
            fail(f"missing required statement: {required}")

    sources = referenced_sources(main_text)
    expanded = expanded_sources(main_text, sources)
    if re.search(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b", expanded, re.IGNORECASE):
        fail("unresolved placeholder token in manuscript source")
    if "\\includegraphics" in expanded:
        fail("submission manuscript includes artwork; BioSystems bars AI-assisted images")

    bib_keys = set(re.findall(r"@\w+\{([^,]+),", BIB.read_text(encoding="utf-8")))
    cited: set[str] = set()
    for group in re.findall(r"\\cite\w*\s*(?:\[[^]]*\]\s*)?\{([^}]+)\}", expanded):
        cited.update(key.strip() for key in group.split(","))
    missing = sorted(cited - bib_keys)
    if missing:
        fail(f"missing BibTeX keys: {', '.join(missing)}")

    for artifact in (PDF,):
        if not artifact.exists() or artifact.stat().st_size == 0:
            fail(f"missing or empty artifact: {artifact.relative_to(ROOT)}")

    if arguments.artifacts:
        validate_artifacts(sources)

    print(
        "PASS ICP submission validation: "
        f"abstract={len(abstract_words)} words; keywords={keyword_count}; "
        f"highlights={len(highlights)}; citations={len(cited)}; figures=0; "
        f"artifacts={'verified' if arguments.artifacts else 'not-requested'}"
    )


if __name__ == "__main__":
    main()
