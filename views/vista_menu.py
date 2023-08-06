import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image


class Menu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
       
        # Cargar la imagen de fondo
        image = Image.open("views/image/tkinterlogo.png")
        photo = ImageTk.PhotoImage(image)
        
        # Agregar la imagen de fondo a un widget Label
        label = CTkLabel(self, text="" ,image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Botón de inicio de sesión
        boton1 = ctk.CTkButton(self, text="Destinos culinarios",  fg_color="#FA5F39")
        boton1.place(x=25, y=200)
        boton2 = ctk.CTkButton(self, text="Busqueda y Filtrado",  fg_color="#FA5F39")
        boton2.place(x=25, y=350)
        boton3 = ctk.CTkButton(self, text="Planificar Visitas",  fg_color="#FA5F39")
        boton3.place(x=475, y=350)
        boton4 = ctk.CTkButton(self, text="Review y Calificaciones",  fg_color="#FA5F39")
        boton4.place(x=475, y=200)

        
    
app = App()
app.mainloop()