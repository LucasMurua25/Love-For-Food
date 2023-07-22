

class DeestinoCulinario:
    def __init__ (self, id: int,nombre: str, tipo_cocina: str, ingredientes: list[str], precio_minimo: float, precio_maximo: float, popularidad: float, disponibilidad: bool, id_ubicacion: int, imagen: str):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina  
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    def to_json():
        pass


    @classmethod
    def from_json(cls,data):
        pass