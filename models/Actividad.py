import datetime
import json

class Actividad:
    def __init__ (self,id: int, nombre: str, destino_id: int, hora_inicio: str):
        """
        hora_inicio datetime ISO 8601
        """
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio


    def to_json(self):
        return {"id":self.id, 
                "nombre":self.nombre,
                "destino_id":self.destino_id, 
                "hora_inicio":self.hora_inicio}


    @classmethod
    def cargar_actividad_json(cls, actividad):
        with open(actividad, "r") as f:
            data = json.load(f)
        return [cls(**actividad) for actividad in data]