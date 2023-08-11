from re import S
import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image
import os



class PantallaMenu(ctk.CTk):
    def __init__(self,master:None,controlador:None):
        super().__init__(master)
        self.master=master
        self.controlador=controlador

        # Botón de inicio de sesión
        boton1 = ctk.CTkButton(self, text="Destinos culinarios",  fg_color="#FA5F39",command=self.controlador.a_destinos)
        boton1.place(x=25, y=200)
        boton2 = ctk.CTkButton(self, text="Busqueda y Filtrado",  fg_color="#FA5F39",command=self.controlador.a_filtro)
        boton2.place(x=25, y=350)
        boton3 = ctk.CTkButton(self, text="Planificar Visitas",  fg_color="#FA5F39",command=self.controlador.a_visita)
        boton3.place(x=475, y=350)
        boton4 = ctk.CTkButton(self, text="Review y Calificaciones",  fg_color="#FA5F39",command=self.controlador.a_review)
        boton4.place(x=475, y=200)
