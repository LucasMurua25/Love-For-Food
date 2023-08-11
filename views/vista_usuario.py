from click import command
import customtkinter as ctk
from customtkinter import CTkLabel
from PIL import ImageTk, Image
from tkinter import messagebox
import os

class PantallaUsuario(ctk.CTk):
    width = 900
    height = 600

    def __init__(self, master=None,controlador=None):
        super().__init__(master)
        self.master=master
        self.controlador=controlador
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
            self.login_frame, text="Login", command=self.login_event, width=200,bg_color="transparent",fg_color="#FF5722"
        )
        self.login_button.grid(row=3, column=0, padx=10, pady=(10, 10))

    def login_event(self):
        print(
            "Presionó Login - nombre de usuario:",
            self.username_entry.get(),
            "contraseña:",
            self.password_entry.get(),
        )
        self.controlador.ir_inicio