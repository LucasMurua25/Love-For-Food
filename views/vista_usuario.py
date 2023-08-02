import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image
from tkinter import messagebox
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
        self.button = ctk.CTkButton(self, text="Inicio", command=self.button_callbck)
        self.button.pack(padx=0, pady=200)
       
        # Cargar la imagen de fondo

        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        image = Image.open(os.path.join(current_path,"image","tkinterlogo.png"))
        photo = ImageTk.PhotoImage(image)
        ctk.set_default_color_theme("dark-blue")
        
        # Agregar la imagen de fondo a un widget Label

        label = CTkLabel(self, text="", image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Campos de entrada para el nombre y apellido
    
        usuario= ctk.CTkEntry(self, placeholder_text="Usuario")
        usuario.place(x=90, y=200)
        
        contrasenia = ctk.CTkEntry(self, placeholder_text="Contraseña",show="*")
        contrasenia.place(x=90, y=250)
    
        # Botón de inicio de sesión

        boton = ctk.CTkButton(self, text="Ingresar", command=self.iniciar_sesion, fg_color="#FA5F39")
        boton.place(x=90, y=300)


    def iniciar_sesion(self):
        # Obtener el nombre y apellido ingresados por el usuario

        usuario = self.usuario.get()
        contrasenia = self.contrasenia.get()

        if len(usuario.get()) == 0:
            messagebox.showwarning("Mensaje", "El campo Usuario es obligatorio.")
            return
        
        if len(contrasenia.get()) == 0:
            messagebox.showwarning("Mensaje", "El campo Contraseña es obligatorio.")
            return
        
        if usuario.get() == "admin" and contrasenia.get() == "admin":
            messagebox.showinfo("Mensaje", "Bienvenido")
        else:
            messagebox.showwarning("Mensaje","Los datos no son validos")

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()