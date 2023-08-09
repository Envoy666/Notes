"""
для более-менее нормального отображения в PyCharm нужно
в Run/Debug Configurations активировать настройку Emulate terminal in output console
"""

from os import system

import adapter
import file
from model import Model
from note import Note

model: Model
DATA_DIR_NAME = "data"
DATA_FILE_NAME = "notes.json"


def clear_terminal():
    system("cls")


def show_all():
    show_note_list(model.get_note_list(), "Notes list:")


def show_note_list(notes: list[Note], list_header):
    clear_terminal()
    print(list_header)
    if notes:
        for note in notes:
            print(note)
    else:
        print("no entries")
    input("Enter anything to continue...")


def show_note():
    pass


def add_note():
    clear_terminal()
    note_data = input_note_data("Add new note:")
    model.add_note(*note_data)
    file.backup_file(DATA_DIR_NAME, DATA_FILE_NAME)
    file.write_file(DATA_DIR_NAME, DATA_FILE_NAME, adapter.list_to_json(model.get_note_list()))


def input_note_data(message):
    if message:
        print(message)
    header = input("Enter note header: ")
    text = input("Enter note text: ")
    return [header, text]


def find_note():
    pass


def edit_note():
    pass


def delete_note():
    pass


def export_import():
    pass


def main():
    global model

    if not file.ensure_path_exists(DATA_DIR_NAME, DATA_FILE_NAME):
        print(f"can't create data file (seems like directory with name \"{DATA_FILE_NAME}\" exists)")
        input("Enter anything to exit...")
        return

    note_list = adapter.json_to_list(file.read_file(DATA_DIR_NAME, DATA_FILE_NAME))
    model = Model()
    model.set_note_list(note_list)

    while True:
        clear_terminal()

        size = model.size()
        if size == 0:
            entries = "no entries"
        elif size == 1:
            entries = "1 entry"
        else:
            entries = f"{size} entries"

        answer = input(f"Note book ({entries}):\n"
                       "1. Show notes list\n"
                       "2. Show note\n"
                       "3. Add a note\n"
                       "4. Find a note\n"
                       "5. Edit a note\n"
                       "6. Delete a note\n"
                       "7. Export/Import\n"
                       "8. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                show_note()
            case "3":
                add_note()
            case "4":
                find_note()
            case "5":
                edit_note()
            case "6":
                delete_note()
            case "7":
                export_import()
            case "8":
                return
            case _:
                print(f"Unknown command - {answer}!")
                input("Enter anything to continue...")


if __name__ == '__main__':
    main()
