class ControladorInicio:
    def __init__(self, app):
        self.app = app
        
    def ir_menu(self):
        self.app.cambiar_frame(self.app.vista_menu)#direcciona al menu
