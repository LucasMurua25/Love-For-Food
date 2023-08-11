import json
class Ubi:
    def __init__(self, id: int, direccion: str, coordenadas: list[float] ):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas


    def to_json(self):
        return {"id":self.id, 
                "direccion":self.direccion,
                "coordenadas":self.coordenadas}

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        id_ubicacion = datos.pop('id_ubicacion', None)
        direccion = datos.pop('direccion', None)
        coordenadas = datos.pop('coordenadas', None)
        return cls(id_ubicacion, direccion, coordenadas)
    
    @classmethod
    def cargar_ubicaciones_json(cls, ubicacion):
        with open(ubicacion, "r") as f:
            data = json.load(f)
        return [cls(**ubicacion) for ubicacion in data]