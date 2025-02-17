# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
import datetime

class Note :
    HIGH : str = "HIGH"
    MEDIUM : str = "MEDIUM"
    LOW : str = "LOW"

    def __init__(self, code : str, title : str, text : str, importance : str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance