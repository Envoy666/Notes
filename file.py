import os

ENCODING = "utf-8"


def ensure_file_exists(name):
    if not os.path.exists(name):
        with open(name, "w", encoding="utf-8") as _:
            pass


def read_file(name: str) -> str:
    if os.path.exists(name):
        with open(name, "r", encoding=ENCODING) as file:
            return file.read()
    return ""


def write_file(name: str, data: str):
    with open(name, "w", encoding=ENCODING) as file:
        file.write(data)
        file.close()
