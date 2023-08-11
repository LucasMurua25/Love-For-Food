class ControladorDestinos:
    def __init__(self, app, destino_culinario):
        self.app = app
        self.destino_culinario= destino_culinario

    
    def marcadores_destinos(self):
        for ubicacion in self.app.ubicaciones:
            self.app.vista_destinos.agregar_marcador(ubicacion.coordenadas, texto='')


    def regresar_menu(self):
        self.app.cambiar_frame(self.app.vista_menu)