import os
from typing import Any
import customtkinter as ctk
from PIL import Image
from tkintermapview import TkinterMapView
from models.Review import Rw
import models.Actividad
import models.Usuario
import models.Ubicacion
import models.RutaVisita
from models.DestinoCulinario import DC
from views.vista_usuario import PantallaUsuario
from views.vista_info import PantallaInfo
from views.vista_inicio import PantallaInicio
from views.vista_menu import PantallaMenu
from controladores.Controlador_Destinos import ControladorDestinos
from controladores.Controlador_Info import ControladorInfo
from controladores.Controlador_Inicio import ControladorInicio

ctk.set_appearance_mode("System")

class App(ctk.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.CTk.__init__(self)
        self.title("Love For Food")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_usuario)

        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(
            Image.open(os.path.join(current_path,"image","tkinterlogo.png")),
            size=(self.width, self.height),
        )
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)

    def inicializar(self):
        destinos = DC.from_json("data/DestinoCulinario.json")

        Controlador_Inicio= ControladorInicio(self)
        Controlador_Usuario=ControladorUsuario()
        Controlador_Menu=ControladorMenu()
        Controlador_Destinos = ControladorDestinos(self, destinos)
        Controlador_Info = ControladorInfo(self)
        Controlador_Filtro=ControladorFiltro()
        Controlador_PRuta=ControladorRuta()

        self.vista_inicio = PantallaInicio(self, Controlador_Inicio)
        self.vista_menu= PantallaMenu(self, Controlador_Destinos)
        self.vista_info = PantallaInfo(self, Controlador_Info)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_menu)

        self.ajustar_frame(self.vista_info)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tk.Tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
