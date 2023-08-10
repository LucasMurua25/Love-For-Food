class ControladorUsuario:
    def __init__(self, app):
        self.app = app

    def ir_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio) #va a la presentacion de inicio
    