class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_usuario(self):
        self.app.cambiar_frame(self.app.vista_usuario)