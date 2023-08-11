import customtkinter as ctk

class PantallaInicio(ctk.CTk):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master=master
        self.controlador=controlador

         #INICIO
         # crear el frame principal
        self.main_frame = ctk.CTkFrame(self,border_width=5)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_label = ctk.CTkLabel(
        self.main_frame,
            text=f" Bienvenido! ",
            font=ctk.CTkFont(size=15, weight="bold",slant="italic"),
        )
        self.main_label.grid(row=0, column=1, padx=(0,0), pady=(8, 5))
        

        # Botón de inicio
        boton = ctk.CTkButton(self, text="Iniciar", fg_color="#FA5F39",command=self.controlador.ir_menu)
        boton.place(x=250, y=350)
