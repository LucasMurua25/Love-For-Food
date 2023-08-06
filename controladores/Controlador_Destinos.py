class ControladorDDestinos:
    def __init__(self, app, modelo_destino_culinario):
        self.app = app
        self.modelo_destino_culinario= modelo_destino_culinario

    def obtener_destinos(self):
        return self.modelo_destino_culinario

    def seleccionar_destino(self):
        """
        Obtiene el índice del destino seleccionado y llama a la vista de
        información para mostrar la información del destino.
        """
        indice = self.app.vista_destinos.obtener_destino_seleccionado()
        if indice is not None:
            destino = self.modelo_destino_culinario[indice]
            self.app.vista_info.mostrar_info_destino(destino)
            self.app.cambiar_frame(self.app.vista_info)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_menu)