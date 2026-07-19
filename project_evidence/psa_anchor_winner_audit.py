#!/usr/bin/env python3
"""Reproduce the exploratory 115-star winning-anchor occupancy audit.

The script is read-only: it loads a sentence embedding archive and a guide-star
array, assigns each selected sentence to its maximum tier-weighted cosine
anchor, and prints a JSON summary to stdout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def l2_normalize(rows: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(rows, axis=1, keepdims=True)
    return rows / np.maximum(norms, 1e-12)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence_archive", type=Path)
    parser.add_argument("anchor_array", type=Path)
    parser.add_argument("--label", default="SentenceNode")
    parser.add_argument("--downweight-start", type=int, default=69)
    parser.add_argument("--downweight-end", type=int, default=75)
    parser.add_argument("--downweight", type=float, default=0.4)
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()

    archive = np.load(args.sentence_archive, allow_pickle=True)
    labels = np.asarray(archive["labels"])
    mask = labels == args.label
    sentences = np.asarray(archive["embeddings"][mask], dtype=np.float32)
    anchors = np.asarray(np.load(args.anchor_array), dtype=np.float32)

    if sentences.ndim != 2 or anchors.ndim != 2:
        raise ValueError("sentence and anchor arrays must both be matrices")
    if sentences.shape[1] != anchors.shape[1]:
        raise ValueError(
            f"dimension mismatch: sentences={sentences.shape}, anchors={anchors.shape}"
        )
    if not 0 <= args.downweight_start <= args.downweight_end <= anchors.shape[0]:
        raise ValueError("downweight interval is outside the anchor array")

    signatures = l2_normalize(sentences) @ l2_normalize(anchors).T
    tier_weights = np.ones(anchors.shape[0], dtype=np.float32)
    tier_weights[args.downweight_start : args.downweight_end] = args.downweight
    winners = np.argmax(signatures * tier_weights[None, :], axis=1)

    anchors_used, counts = np.unique(winners, return_counts=True)
    order = np.argsort(-counts)
    top = [
        {"anchor": int(anchors_used[index]), "count": int(counts[index])}
        for index in order[: args.top]
    ]

    result = {
        "sentence_archive": str(args.sentence_archive),
        "sentence_archive_sha256": sha256(args.sentence_archive),
        "anchor_array": str(args.anchor_array),
        "anchor_array_sha256": sha256(args.anchor_array),
        "selected_label": args.label,
        "selected_sentences": int(winners.size),
        "anchor_count": int(anchors.shape[0]),
        "active_anchors": int(anchors_used.size),
        "singleton_anchors": int(np.count_nonzero(counts == 1)),
        "maximum_occupancy": int(counts.max()),
        "tier_weight": {
            "start_inclusive": args.downweight_start,
            "end_exclusive": args.downweight_end,
            "weight": args.downweight,
        },
        "tie_rule": "numpy.argmax: lowest index on an exact tie",
        "top": top,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
