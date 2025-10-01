"""Analysis helpers for forensic artifacts (src)."""

from typing import List, Dict


def analyze_file_metadata(file_paths: List[str]) -> List[Dict]:
    return [{"path": p} for p in file_paths]
