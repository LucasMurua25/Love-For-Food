
class ControladorInicio:
    def __init__(self, app):
        self.app = app
    def iniciar(self):
        print( "Presionó Iniciar!")
        self.main_frame.grid_forget()
        self.main_frame.place_forget()  # eliminar el frame de inicio
