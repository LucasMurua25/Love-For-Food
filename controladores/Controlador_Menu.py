class ControladorMenu:

    def __init__(self, app):
        # Aqui el controlador recibe la app para poder acceder a sus funciones
        self.app = app

    def a_destinos(self):
        self.app.cambiar_frame(self.app.vista_destinos)

    def a_review(self):
        self.app.cambiar_frame(self.app.vista_review)

    def a_filtro(self):
        self.app.cambiar_frame(self.app.vista_filltro)

    def a_visita(self):
        self.app.cambiar_frame(self.app.vista_visita)
