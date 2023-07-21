

class Usuario:
    def __init__(self, id: int, nombre: str, apellido: str, historial_rutas: list[int]):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas