
from pathlib import Path

def _ensure_txt(name):
    p = Path(name)
    if p.suffix != ".txt":
        p = p.with_suffix(".txt")
    return p

def write_file(file_name: str, file_content: str) -> None:
    path = _ensure_txt(file_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(file_content)

def append_file(file_name: str, append_content: str) -> None:
    path = _ensure_txt(file_name)
    with open(path, "a", encoding="utf-8") as f:
        f.write(append_content)

def read_file(file_name: str) -> str:
    path = _ensure_txt(file_name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
