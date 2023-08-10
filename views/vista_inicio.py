import customtkinter as ctk
from customtkinter  import CTk
from PIL import ImageTk, Image
import os


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
            Image.open(os.path.join(current_path,"assets","tkinterlogo.png")),
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
        

        # Botón de inicio
        boton = ctk.CTkButton(self, text="Iniciar",  fg_color="#FA5F39",command=self.cambiar_frame)
        boton.place(x=250, y=350)