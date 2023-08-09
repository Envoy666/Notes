from note import Note


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
