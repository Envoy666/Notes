"""
для более-менее нормального отображения в PyCharm нужно
в Run/Debug Configurations активировать настройку Emulate terminal in output console
"""

from os import system

import file


def clear_terminal():
    system("cls")


def show_all():
    pass


def show_note():
    pass


def add_note():
    pass


def find_note():
    pass


def edit_note():
    pass


def delete_note():
    pass


def export_import():
    text = "test file read/write"
    dir_name = "data"
    file_name = "test.json"
    if not file.ensure_path_exists(dir_name, file_name):
        print(f"can't create data file (seems like directory with name \"{file_name}\" exists)")
        input("Enter anything to continue...")
        return
    file.write_file(dir_name, file_name, text)
    red_text = file.read_file(dir_name, file_name)


def main():
    while True:
        clear_terminal()

        entries = "no entries"

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
