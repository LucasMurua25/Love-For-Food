class ControladorUsuario:
    def __init__(self, app, usuarios):
        self.app = app
        self.usuarios=usuarios
    def ir_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio) #va a la presentacion de inicio
    