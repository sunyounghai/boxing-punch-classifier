from dataclasses import dataclass

import numpy as np

CLASSES = ["jab", "cross", "lead hook", "lead uppercut", "rear hook", "rear uppercut"]
CLASS_TO_ID = {c: i for i, c in enumerate(CLASSES)}
VIDEO_NAMES = [f"V{i}" for i in range(1, 11)]


@dataclass
class VideoData:
    name: str
    skeleton: np.ndarray
    start: np.ndarray
    end: np.ndarray