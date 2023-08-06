import customtkinter as ctk
from PIL import Image
import os
from controladores import Controlador_Inicio

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
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
        self.bg_image_label.grid(row=0, column=0)



        #crear el frame de inicio de sesion
        #caracteristicas del fondo de login
        self.login_frame = ctk.CTkFrame( self, corner_radius=10, bg_color="transparent")
        self.login_frame.grid(row=0,sticky="ne")
        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text="¡Registrate!",
            font=ctk.CTkFont(size=20, weight="bold", slant="roman"), )
        
        self.login_label.grid(row=0, column=0, pady=(10, 10))
        self.username_entry = ctk.CTkEntry(
            self.login_frame, width=200, placeholder_text="Nombre de usuario",
        )
        self.username_entry.grid(row=1, column=0, pady=(10, 10))
        self.password_entry = ctk.CTkEntry(
            self.login_frame, width=200, show="*", placeholder_text="Contraseña"
        )
        self.password_entry.grid(row=2, column=0, pady=(10, 10))
        self.login_button = ctk.CTkButton(
            self.login_frame, text="Login", command=self.login_event, width=200,bg_color="transparent"
        )
        self.login_button.grid(row=3, column=0, padx=10, pady=(10, 10))
 
         # crear el frame principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=50,bg_color="transparent")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = ctk.CTkLabel(
        self.main_frame,
            text="BIENVENIDO A\n LoveForFood",
            font=ctk.CTkFont(size=20, weight="bold",slant="italic"),
        )
        self.main_label.grid(row=0, column=1, padx=(0,0), pady=(8, 5))

        #caracteristicas del boton iniciar
        self.back_button = ctk.CTkButton(
            self.main_frame, text="INICIAR", command=self.iniciar, width=200,border_spacing=10,font=("bold",15)
        )
        self.back_button.grid(row=1, column=1, padx=30, pady=(15, 15))
        
    def login_event(self):
        print(
            "Presionó Login - nombre de usuario:",
            self.username_entry.get(),
            "contraseña:",
            self.password_entry.get(),
        )
        self.login_frame.grid_forget()  # eliminar el frame de login
        self.main_frame.grid(
            row=0, column=0, padx=0
        )  # mostrar el frame principal
    def iniciar(self):
        print( "Presionó Iniciar!")
        self.main_frame.grid_forget()  # eliminar el frame de inicio
        #self.login_frame.grid(row=0,sticky="ne")  # mostrar el frame de login  

if __name__ == "__main__":
 app = App()
 app.mainloop()