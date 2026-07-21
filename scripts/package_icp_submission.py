#!/usr/bin/env python3
"""Build a deterministic, figure-free BioSystems source package for ICP."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript" / "submission_main.tex"
SECTIONS = ROOT / "manuscript" / "sections"
BIB = ROOT / "library" / "references.bib"
SUPPORT = ROOT / "submission" / "biosystems"
PDF = ROOT / "output" / "pdf" / "icp_biosystems_submission.pdf"
OUTPUT = ROOT / "output" / "submission"
ARCHIVE = OUTPUT / "icp_biosystems_sources.zip"
ARCHIVE_SHA256 = OUTPUT / "icp_biosystems_sources.zip.sha256"
PDF_SHA256 = ROOT / "output" / "pdf" / "icp_biosystems_submission.pdf.sha256"
MANIFEST = OUTPUT / "icp_biosystems_build_manifest.json"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
BUILD_INPUTS = (
    ROOT / "Makefile",
    ROOT / "scripts" / "package_icp_submission.py",
    ROOT / "scripts" / "validate_icp_submission.py",
)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL ICP submission packaging: {message}")


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        fail(f"path escapes repository: {path}")


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


def without_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def referenced_sections() -> list[Path]:
    queue = [MAIN]
    found: dict[str, Path] = {}
    sections_root = SECTIONS.resolve()

    while queue:
        source = queue.pop(0)
        text = without_comments(source.read_text(encoding="utf-8"))
        for reference in INPUT_RE.findall(text):
            candidate = ROOT / reference
            if candidate.suffix == "":
                candidate = candidate.with_suffix(".tex")
            resolved = candidate.resolve()
            try:
                resolved.relative_to(sections_root)
            except ValueError:
                fail(
                    f"referenced TeX input is outside manuscript/sections: "
                    f"{reference}"
                )
            if not resolved.is_file():
                fail(f"missing referenced TeX input: {relative(resolved)}")
            name = relative(resolved)
            if name not in found:
                found[name] = resolved
                queue.append(resolved)

    return [found[name] for name in sorted(found)]


def support_files() -> list[Path]:
    if not SUPPORT.is_dir():
        fail(f"missing support directory: {relative(SUPPORT)}")
    files: list[Path] = []
    for path in sorted(SUPPORT.rglob("*")):
        if path.is_symlink():
            fail(f"support package contains a symlink: {relative(path)}")
        if path.is_file():
            files.append(path)
    return files


def package_inputs() -> list[Path]:
    candidates = [MAIN, *referenced_sections(), BIB, *support_files()]
    files: dict[str, Path] = {}
    for path in candidates:
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


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def write_archive(inputs: list[Path]) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = ARCHIVE.with_name(f".{ARCHIVE.name}.tmp")
    with zipfile.ZipFile(
        temporary,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in inputs:
            info = zipfile.ZipInfo(relative(path), date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.extra = b""
            info.comment = b""
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    os.replace(temporary, ARCHIVE)


def main() -> None:
    if not PDF.is_file() or PDF.stat().st_size == 0:
        fail(f"missing or empty review PDF: {relative(PDF)}")

    inputs = package_inputs()
    for path in BUILD_INPUTS:
        if not path.is_file():
            fail(f"missing build input: {relative(path)}")

    write_archive(inputs)
    archive_hash = sha256_file(ARCHIVE)
    pdf_hash = sha256_file(PDF)
    write_text_atomic(ARCHIVE_SHA256, f"{archive_hash}  {ARCHIVE.name}\n")
    write_text_atomic(PDF_SHA256, f"{pdf_hash}  {PDF.name}\n")

    manifest = {
        "schema_version": 1,
        "archive": {
            "fixed_member_timestamp": "1980-01-01T00:00:00Z",
            "format": "zip",
            "members": [relative(path) for path in inputs],
        },
        "artifacts": [
            {
                **file_record(ARCHIVE),
                "checksum_file": relative(ARCHIVE_SHA256),
            },
            {
                **file_record(PDF),
                "checksum_file": relative(PDF_SHA256),
            },
        ],
        "build_inputs": [file_record(path) for path in sorted(BUILD_INPUTS)],
        "git": git_metadata([*inputs, *BUILD_INPUTS]),
        "inputs": [file_record(path) for path in inputs],
        "manifest_path": relative(MANIFEST),
    }
    write_text_atomic(
        MANIFEST,
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
    )

    print(
        "PACKAGED ICP BioSystems sources: "
        f"members={len(inputs)}; archive={relative(ARCHIVE)}; "
        f"sha256={archive_hash}"
    )


if __name__ == "__main__":
    main()
