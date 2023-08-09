from note import Note


class FilterModeMap:
    ID = "Id"
    HDR = "Header"
    TXT = "Text"
    CRT = "Creation time"
    MDF = "Modification time"

    filter_mode_map = {
        "1": ID,
        "2": HDR,
        "3": TXT,
        "4": CRT,
        "5": MDF,
    }


def filter_notes(note_list: list[Note], mode: str, required: str) -> list[Note]:
    new_list = []
    match mode:
        case FilterModeMap.ID:
            new_list = list(filter(lambda note: required in str(note.get_id()), note_list))
        case FilterModeMap.HDR:
            new_list = list(filter(lambda note: required in note.get_header(), note_list))
        case FilterModeMap.TXT:
            new_list = list(filter(lambda note: required in note.get_text(), note_list))
        case FilterModeMap.CRT:
            new_list = list(filter(lambda note: note.get_created() == required, note_list))
        case FilterModeMap.MDF:
            new_list = list(filter(lambda note: note.get_modified() == required, note_list))

    return new_list
