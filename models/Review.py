
class Review:
    def __init__(self, id: int, id_destino: int, id_usuario: int, calificacion: int, comentario: str, animo: str):

        """
        Calificacion int 1 to 5
        Animo str 'Positivo' o 'Negativo'
        """
        self.id = id 
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo 


    def to_json():
        pass


    @classmethod
    def from_json(cls,data):
        pass