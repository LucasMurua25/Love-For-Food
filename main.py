import os
import customtkinter as ctk
from PIL import Image
from models.Actividad import Actividad
from models.DestinoCulinario import DC
from models.Ubicacion import Ubi
from models.Usuario import Us
from controladores.Controlador_Usuario import ControladorUsuario
from views.vista_usuario import PantallaUsuario
from views.vista_info import PantallaInfo
from views.vista_inicio import PantallaInicio
from views.vista_menu import PantallaMenu
#from views.vista_filltro import VistaFiltro
from views.vista_destinos import Mapa
#from views.vista_visita import MapRut
from controladores.Controlador_Destinos import ControladorDestinos
from controladores.Controlador_Info import ControladorInfo
from controladores.Controlador_Inicio import ControladorInicio
#from controladores.Controlador_Filtro import ControladorFiltro
#from controladores.Controlador_Ruta import ControladorRuta
from controladores.Controlador_Menu import ControladorMenu
import os


class App(ctk.CTk):
    width = 900
    height = 600
    ctk.set_appearance_mode("system")
    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Love For Food")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.inicializar()
        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(
            Image.open(os.path.join(current_path,"assets","tkinterlogo.png")))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label(row=0, column=0)
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        destinos = DC.cargar_destinos_de_json("data/DestinoCulinario.json")
        usuarios= Us.cargar_usuarios_de_json("data/Usuario.json")
        ubicacion= Ubi.cargar_ubicaciones_json("data/Ubicacion.json")
        actividad=Actividad.cargar_actividad_json("data/Actividad.json")

        Controlador_Usuario= ControladorUsuario(self,usuarios)
        Controlador_Inicio= ControladorInicio(self)
        Controlador_Menu=ControladorMenu(self)

        Controlador_Destinos = ControladorDestinos(self,destinos,ubicacion)
        Controlador_Info = ControladorInfo(self,actividad)
        #Controlador_Filtro=ControladorFiltro(self, destinos)
        #Controlador_Ruta=ControladorRuta(self)

        self.vista_usuario= PantallaUsuario(Controlador_Usuario)
        self.vista_inicio = PantallaInicio(Controlador_Inicio)
        self.vista_menu=PantallaMenu(Controlador_Menu)

        self.vista_destinos= Mapa(Controlador_Destinos)
        self.vista_info = PantallaInfo(Controlador_Info)
        #self.vista_filtro=VistaFiltro(Controlador_Filtro)
        #self.vista_visita= MapRut(Controlador_Ruta)

        self.ajustar_frame(self.vista_usuario)
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_menu)
        self.ajustar_frame(self.vista_destinos)
        #self.ajustar_frame(self.vista_filtro)
        self.ajustar_frame(self.vista_info) 
       # self.ajustar_frame(self.vista_visita)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()