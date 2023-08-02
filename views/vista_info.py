
import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image
import os


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Informacion Del Destino")
        self.geometry("650x550")
                # Cargar la imagen de fondo
        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        image = Image.open(os.path.join(current_path,"image","fondo.png"))
        photo = ImageTk.PhotoImage(image)
                # Agregar la imagen de fondo a un widget Label
        label = CTkLabel(self, text="" ,image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
                # Botones
        boton1 = ctk.CTkButton(self, text="Volver a Menú",  fg_color="#8787CE")
        boton1.place(x=10, y=10)
        boton2 = ctk.CTkButton(self, text="Hacer una Reseña",  fg_color="#8787CE")
        boton2.place(x=255, y=10)
        boton3 = ctk.CTkButton(self, text="Reservar",  fg_color="#8787CE")
        boton3.place(x=500, y=10)
        ctk.set_default_color_theme("dark-blue")
                # Mostrar la informacion del destino
        def mostrar_info_destino(self, DestinoCulinario):
         
         info=(f"Nombre : {DestinoCulinario.nombre}\n Ubicación: {DestinoCulinario.id}\n Tipo De Cocina: {DestinoCulinario.tipo_cocina}\n Popularidad: {DestinoCulinario.popularidad}\n Ingredientes Ocupados: {DestinoCulinario.ingredientes} \n Disponibilidad: {DestinoCulinario.disponibilidad}\nDireccion: {DestinoCulinario.id_ubicacion}\n Precio Maximo: $ {DestinoCulinario.precio_maximo} Precio Minimo: ${DestinoCulinario.precio_minimo} \n{DestinoCulinario.imagen} ")
        
app = App()
app.mainloop()