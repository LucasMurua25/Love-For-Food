class ControladorInfo:
    def __init__(self, app,actividades):
        self.app = app
        self.actividades=actividades
    def regresar_menu(self):
        self.app.cambiar_frame(self.app.vista_menu)