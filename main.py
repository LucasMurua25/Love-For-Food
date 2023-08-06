import os

import customtkinter

from customtkinter import CTkLabel, CTk

from PIL import ImageTk, Image

from views import vista_inicio, vista_usuario


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
    
       
        # Cargar la imagen de fondo
        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        image = Image.open(os.path.join(current_path + "/tkinterlogo.png"))
        photo = customtkinter.CTkImage(image)
        # Agregar la imagen de fondo a un widget Label
        label = customtkinter.CTkLabel(self, text="" ,image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Botón de inicio de sesión
        self.boton = customtkinter.CTkButton( text="Iniciar sesión", command=self.button_callback, fg_color="#FA5F39")
        self.boton.place(x=250, y=350)
        

    def button_callback(self):
        print("button clicked")
        vista_inicio.grid_forget()  # eliminar el frame principal
        vista_usuario.grid(row=0, column=0, sticky="ns")  # mostrar el frame de login 

if __name__ == "__main__":
    app = App()
    app.mainloop()