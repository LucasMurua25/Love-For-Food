import json

class Us:
    def __init__(self, id: int, nombre: str, apellido: str, historial_rutas: list[int]):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas


    def to_json(self):
        return {"id":self.id, 
                "nombre":self.nombre,
                "apellido":self.apellido, 
                "historial_rutas":self.historial_rutas}
    
    def guardar_en_json(self,archivo="data\\Usuario.json"):
        """
        Guarda los datos del usuario en un archivo json
        """
        datos = to_json()
        
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json


    @classmethod
    def cargar_usuarios_de_json(cls, users):
        with open(users, "r") as f:
            data = json.load(f)
        return [cls(**destino) for destino in data]

