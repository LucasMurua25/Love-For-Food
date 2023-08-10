
import customtkinter as ctk
from PIL import ImageTk, Image
import os


class PantallaInfo(ctk.CTk):
    width = 900
    height = 600
    def __init__(self):
        super().__init__()
        self.title("Informacion Del Destino")
        self.geometry("900x600")
                # Cargar la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(
            Image.open(os.path.join(current_path,"assets","tkinterlogo.png")),
            size=(self.width, self.height),
        )
        # Agregar la imagen de fondo a un widget Label
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)
                
                # Botones
        boton1 = ctk.CTkButton(self, text="Volver a Menú",  fg_color="#FA5F39")
        boton1.place(x=50, y=20)
        boton2 = ctk.CTkButton(self, text="Hacer una Reseña",  fg_color="#FA5F39")
        boton2.place(x=375, y=20)
        boton3 = ctk.CTkButton(self, text="Reservar",  fg_color="#FA5F39")
        boton3.place(x=700, y=20)
        ctk.set_default_color_theme("dark-blue")
                # Mostrar la informacion del destino
        def mostrar_info_destino(self, DestinoCulinario):
         
         info=(f"Nombre : {DestinoCulinario.nombre}\n Ubicación: {DestinoCulinario.id}\n Tipo De Cocina: {DestinoCulinario.tipo_cocina}\n Popularidad: {DestinoCulinario.popularidad}\n Ingredientes Ocupados: {DestinoCulinario.ingredientes} \n Disponibilidad: {DestinoCulinario.disponibilidad}\nDireccion: {DestinoCulinario.id_ubicacion}\n Precio Maximo: $ {DestinoCulinario.precio_maximo} Precio Minimo: ${DestinoCulinario.precio_minimo} \n{DestinoCulinario.imagen} ")
