import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image
import os



class PantallaMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
        # Botón de inicio de sesión
        boton1 = ctk.CTkButton(self, text="Destinos culinarios",  fg_color="#FA5F39")
        boton1.place(x=25, y=200)
        boton2 = ctk.CTkButton(self, text="Busqueda y Filtrado",  fg_color="#FA5F39")
        boton2.place(x=25, y=350)
        boton3 = ctk.CTkButton(self, text="Planificar Visitas",  fg_color="#FA5F39")
        boton3.place(x=475, y=350)
        boton4 = ctk.CTkButton(self, text="Review y Calificaciones",  fg_color="#FA5F39")
        boton4.place(x=475, y=200)
