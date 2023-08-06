import customtkinter as ctk
from PIL import Image
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Campos de entrada para el nombre y apellido
    
        usuario= ctk.CTkEntry(self, placeholder_text="Usuario")
        usuario.place(x=90, y=200)
        
        contrasenia = ctk.CTkEntry(self, placeholder_text="Contraseña",show="*")
        contrasenia.place(x=90, y=250)
 
 # crear el frame de inicio de sesion
        self.login_frame = ctk.CTkFrame(self, corner_radius=10)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text="LOVE FOR FOOD\nPágina de Login",
            font=ctk.CTkFont(size=20, weight="bold"), )
        
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = ctk.CTkEntry(
            self.login_frame, width=200, placeholder_text="nombre de usuario"
        )
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = ctk.CTkEntry(
            self.login_frame, width=200, show="*", placeholder_text="contraseña"
        )
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = ctk.CTkButton(
            self.login_frame, text="Login", command=self.login_event, width=200
        )
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        print(
            "Presionó Login - nombre de usuario:",
            self.username_entry.get(),
            "contraseña:",
            self.password_entry.get(),
        )
app = App()
app.mainloop()