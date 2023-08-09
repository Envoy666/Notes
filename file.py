from pathlib import Path

ENCODING = "utf-8"


def ensure_path_exists(dir_name: str, file_name: str) -> bool:
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    path = Path(dir_name, file_name)
    if not path.exists():
        path.write_text("{}", encoding=ENCODING)
    elif path.is_dir():
        return False
    return True


def read_file(dir_name: str, file_name: str) -> str:
    path = Path(dir_name, file_name)
    if path.exists():
        return path.read_text(encoding=ENCODING)
    return ""


def write_file(dir_name: str, file_name: str, data: str):
    path = Path(dir_name, file_name)
    path.write_text(data, encoding=ENCODING)
