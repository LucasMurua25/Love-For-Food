import os
from typing import Any
import customtkinter as ctk
from PIL import Image
from models.DestinoCulinario import DC
from models.Ubicacion import Ubi
from models.Usuario import Us
from controladores.Controlador_Usuario import ControladorUsuario
from views.vista_usuario import PantallaUsuario
from views.vista_info import PantallaInfo
from views.vista_inicio import PantallaInicio
from views.vista_menu import PantallaMenu
from views.vista_filtro import VistaFiltro
from views.vista_destinos import Mapa
from views.vista_visita import MapRut
from controladores.Controlador_Destinos import ControladorDestinos
from controladores.Controlador_Info import ControladorInfo
from controladores.Controlador_Inicio import ControladorInicio
#from controladores.Controlador_Filtro import ControladorFiltro
#from controladores.Controlador_Ruta import ControladorRuta
#from controladores.Controlador_Menu import ControladorMenu


ctk.set_appearance_mode("System")

class App(ctk.CTk):
    width = 900
    height = 600
    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Love For Food")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)
        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(
            Image.open(os.path.join(current_path,"image","tkinterlogo.png")),
            size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)

    def inicializar(self):
        destinos = DC.from_json("data/DestinoCulinario.json")
        usuarios= Us.from_json("data/Usuario.json")
        ubicacion= Ubi.from_json("data/Ubicacion.json")
        Controlador_Usuario= ControladorUsuario(self)
        Controlador_Inicio= ControladorInicio(self)
        Controlador_Menu=(self)
        Controlador_Destinos = ControladorDestinos(self, ubicacion)
        Controlador_Info = ControladorInfo(self)
        #Controlador_Filtro=ControladorFiltro(self, destinos)
        #Controlador_Ruta=ControladorRuta(self)

        self.vista_usuario= PantallaMenu(Controlador_Usuario)
        self.vista_inicio = PantallaInicio(Controlador_Inicio)
        self.vista_info = PantallaInfo(Controlador_Info)
        self.vista_destinos= Mapa(Controlador_Destinos)
        #self.vista_filtro=VistaFiltro(Controlador_Filtro)
        self.vista_menu=PantallaMenu(Controlador_Menu)
        #self.vista_visita= MapRut(Controlador_Ruta)

        self.ajustar_frame(self.vista_usuario)
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_menu)
        self.ajustar_frame(self.vista_destinos)
        #self.ajustar_frame(self.vista_filtro)
        self.ajustar_frame(self.vista_info) 
        #self.ajustar_frame(self.vista_visita)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()