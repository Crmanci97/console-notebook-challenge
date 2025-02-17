# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
import datetime

class Note :
    HIGH : str = "HIGH"
    MEDIUM : str = "MEDIUM"
    LOW : str = "LOW"

    def __init__(self, code : str, title : str, text : str, importance : str):
        self.code :str = code
        self.title : str = title
        self.text : str = text
        self.importance : str = importance

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
            return tag


    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"

    class Notebook:
        def __init__(self):
            self.notes = []

    def add_note(self, title: str, text: str, importance: str, tags: list[str]) -> int:
        code = len(self.notes) + 1
        new_note = Note(title, text, importance, code, tags)
        self.notes.append(new_note)
        return code

    def delete_note(self, code: int):
        self.notes = [note for note in self.notes if note.code != code]

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes if note.importance in ['HIGH', 'MEDIUM']]

    def notes_by_tag(self, tag: str) -> list[Note]:
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        tag_counts = {}
        for note in self.notes:
            for tag in note.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        if not tag_counts:
            return ""

        # most_common_tag = min(tag_counts.items(), key=lambda item: (-item[1], item[0]))
        #return most_common_tag[0]