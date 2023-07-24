import json

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

    def to_json(self):
        return {"id":self.id, 
                "nombre":self.nombre,
                "tipo_cocina":self.tipo_cocina, 
                "ingredientes":self.ingredientes,
                "precio_minimo":self.precio_minimo, 
                "precio_maximo":self.precio_maximo,
                "popularidad":self.popularidad, 
                "id_ubicacion":self.id_ubicacion,
                "imagen":self.imagen}


    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["id"],data["nombre"],data["tipo_cocina"],data["ingredientes"],
                   data["precio_minimo"],data["precio_maximo"],data["popularidad"],data["id_ubicacion"],data["imagen"])