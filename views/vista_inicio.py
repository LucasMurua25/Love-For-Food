
import customtkinter as ctk
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel,CTkButton,CTkCheckBox
from PIL import ImageTk, Image
from tkinter import messagebox


class VistaInicio(ctk.CTk):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
        self.master = master
        self.controlador = controlador       
        # Cargar la imagen de fondo
        image = Image.open("views/image/tkinterlogo.png")
        photo = ImageTk.PhotoImage(image)
        
        # Agregar la imagen de fondo a un widget Label
        label = CTkLabel(self, text="" ,image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Botón de inicio de sesión
        boton = CTkButton(self, text="Iniciar sesión",  fg_color="#FA5F39",command=self.iniciar_sesion)
        boton.place(x=250, y=350)


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
