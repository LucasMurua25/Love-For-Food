class ControladorUsuario:
    def __init__(self, app):
        self.app = app

    def ControladorUsuario(self):
        self.app.cambiar_frame(self.app.vista_inicio)