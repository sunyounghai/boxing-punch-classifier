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