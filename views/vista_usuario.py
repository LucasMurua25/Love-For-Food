from click import command
import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
        self.button = ctk.CTkButton(self, text="Inicio", command=self.button_callbck)
        self.button.pack(padx=0, pady=200)
       
        # Cargar la imagen de fondo

        image = Image.open("views/image/tkinterlogo.png")
        photo = ImageTk.PhotoImage(image)
        ctk.set_default_color_theme("dark-blue")
        
        # Agregar la imagen de fondo a un widget Label

ctk.set_appearance_mode("System")
class PantallaUsuario(ctk.CTk):
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
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)


        #LOGIN
        #crear el frame de inicio de sesion
        #caracteristicas del fondo de login
        self.login_frame = ctk.CTkFrame( self,border_width=2.5)
        self.login_frame.grid(row=0,sticky="ne")
        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text="¡Registrate!",
            font=ctk.CTkFont(size=20, weight="bold", slant="roman"), )
        
        self.login_label.grid(row=0, column=0, pady=(10, 10))
        self.username_entry = ctk.CTkEntry(
            self.login_frame, width=200, placeholder_text="Nombre de usuario"
        )
        self.username_entry.grid(row=1, column=0, pady=(10, 10))
        self.password_entry = ctk.CTkEntry(
            self.login_frame, width=200, show="*", placeholder_text="Contraseña",
        )
        self.password_entry.grid(row=2, column=0, pady=(10, 10))
        self.login_button = ctk.CTkButton(
            self.login_frame, text="Login", command=self.login_event, width=200,bg_color="transparent",fg_color="#FA5F39"
        )
        self.login_button.grid(row=3, column=0, padx=10, pady=(10, 10))


    def iniciar_sesion(self):
        # Obtener el nombre y apellido ingresados por el usuario

        usuario = self.usuario.get()
        contrasenia = self.contrasenia.get()

    def login_event(self):
        print(
            "Presionó Login - nombre de usuario:",
            self.username_entry.get(),
            "contraseña:",
            self.password_entry.get(),
        )
        self.login_frame.grid_forget()
        self.login_frame.place_forget()
