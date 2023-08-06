
class ControladorInicio:
    def __init__(self, app):
        self.app = app
    def iniciar(self):
        self.login_frame.grid_forget()  # eliminar el frame de inicio
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # mostrar el frame de login  
