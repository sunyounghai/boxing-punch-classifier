from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

CLASSES = ["jab", "cross", "lead hook", "lead uppercut", "rear hook", "rear uppercut"]
CLASS_TO_ID = {c: i for i, c in enumerate(CLASSES)}
VIDEO_NAMES = [f"V{i}" for i in range(1, 11)]


@dataclass
class VideoData:
    name: str
    skeleton: np.ndarray
    mask: np.ndarray
    labels: np.ndarray
    start: np.ndarray
    end: np.ndarray


def read_annotations(path: str | Path) -> pd.DataFrame:
    raw = pd.read_excel(path, header=None)

    def norm(s: pd.Series) -> pd.Series:
        return s.astype(str).str.strip().str.lower()

    class_col, best = None, 0
    for c in raw.columns:
        hits = norm(raw[c]).isin(CLASS_TO_ID).sum()
        if hits > best:
            class_col, best = c, hits
    if class_col is None:
        raise ValueError("클래스 열을 찾지 못함")

    rows = raw[norm(raw[class_col]).isin(CLASS_TO_ID)]
    num_cols = [
        c
        for c in raw.columns
        if c != class_col and pd.to_numeric(rows[c], errors="coerce").notna().all()
    ]
    if len(num_cols) < 2:
        raise ValueError("시작/끝 프레임 열을 찾지 못함")

    out = pd.DataFrame(
        {
            "start": rows[num_cols[0]].astype(int).values,
            "end": rows[num_cols[1]].astype(int).values,
            "class": norm(rows[class_col]).values,
        }
    )

    out["label"] = out["class"].map(CLASS_TO_ID)
    return out.reset_index(drop=True)


def load_video(data_dir: str | Path, name: str) -> VideoData:
    data_dir = Path(data_dir)
    ann = read_annotations(data_dir / "annotation" / f"{name}.xlsx")
    sk = np.load(data_dir / "skeleton" / f"{name}.npy")

    if len(sk) != len(ann):
        raise ValueError(f"{name}: 클립 수 불일치 ({len(ann)} vs {len(sk)})")

    mask = ~(sk == 0).all(axis=(2, 3))

    return VideoData(
        name=name,
        skeleton=sk,
        mask=mask,
        labels=ann["label"].values,
        start=ann["start"].values,
        end=ann["end"].values,
    )