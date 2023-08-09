import customtkinter as ctk
from PIL import Image
import os

ctk.set_appearance_mode("dark")


class PantallaInicio(ctk.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Love For Food")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(
            Image.open(os.path.join(current_path,"image","tkinterlogo.png")),
            size=(self.width, self.height),
        )
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=1, column=5)
        

         #INICIO
         # crear el frame principal
        self.main_frame = ctk.CTkFrame(self,border_width=5)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_label = ctk.CTkLabel(
        self.main_frame,
            text=f" Bienvenido! ",
            font=ctk.CTkFont(size=15, weight="bold",slant="italic"),
        )
        self.main_label.grid(row=0, column=1, padx=(0,0), pady=(8, 5))
        


        #caracteristicas del boton iniciar
        self.back_button = ctk.CTkButton(
            self.main_frame, text="Iniciar", command=self.controlador.iniciar, width=100,border_spacing=5,font=("bold",15)
        )
        self.back_button.grid(row=1, column=1, padx=20, pady=(15, 15))

