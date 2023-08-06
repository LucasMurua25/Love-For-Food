import json

class RV:
    def __init__(self, id: int, nombre: str, destinos: list[int]):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos


    def to_json(self):
        return {"id":self.id, 
                "nombre":self.nombre,
                "destinos":self.destinos,}


    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["id"],data["nombre"],data["destinos"])