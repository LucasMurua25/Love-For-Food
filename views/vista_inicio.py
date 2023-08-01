
import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image


class App(ctk.CTk):
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
        boton = ctk.CTkButton(self, text="Iniciar sesión",  fg_color="#FA5F39")
        boton.place(x=250, y=350)

    
app = App()
app.mainloop()