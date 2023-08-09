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
            text=" Bienvenido! ",
            font=ctk.CTkFont(size=15, weight="bold",slant="italic"),
        )
        self.main_label.grid(row=0, column=1, padx=(0,0), pady=(8, 5))
        

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


        #caracteristicas del boton iniciar
        self.back_button = ctk.CTkButton(
            self.main_frame, text="Iniciar", command=self.controlador.iniciar, width=100,border_spacing=5,font=("bold",15)
        )
        self.back_button.grid(row=1, column=1, padx=20, pady=(15, 15))

