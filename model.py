import time

from note import Note


def timestamp() -> float:
    return time.time()


class Model:

    def __init__(self):
        self.__note_list = []
        self.__last_id = 0

    def set_note_list(self, note_list: list[Note]):
        self.__note_list = note_list
        if self.__note_list:
            self.__last_id = self.__note_list[-1].get_id()

    def get_note_list(self) -> list[Note]:
        return self.__note_list

    def size(self) -> int:
        return len(self.__note_list)

    def add_note(self, header: str, text: str):
        note = Note()
        note.set_header(header)
        note.set_text(text)
        _timestamp = timestamp()
        note.set_created(_timestamp)
        note.set_modified(_timestamp)
        self.__note_list.append(note)
        self.__last_id += 1
        note.set_id(self.__last_id)
