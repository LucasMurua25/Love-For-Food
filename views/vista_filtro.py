import customtkinter as ctk
from customtkinter import CTkLabel, CTkInputDialog
from PIL import ImageTk, Image
import os

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("LoveForFood V1.0")
        self.label = ctk.CTkLabel(self, text="Resultado")
        self.label.pack(padx=20, pady=20)
        self.attributes('-topmost', True)

class VistaFiltro(ctk.CTk):
    width = 900
    height = 600
    def __init__(self):
        super().__init__()
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
        
        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(
            Image.open(os.path.join(current_path,"image","tkinterlogo.png")),
            size=(self.width, self.height),
        )
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=1, column=5)
        # Agrega un mensaje en el label 
        self.lbl_mensaje = ctk.CTkLabel(self.master, text='¡Selecciona tu destino culinario, de acuerdo a tus preferencias!', font=('Roboto Condensed', 20))
        self.lbl_mensaje.place(x=40, y=100)

        frame_1 = ctk.CTkScrollableFrame(self, orientation="vertical", label_text="should not appear", fg_color="transparent")
        frame_1.grid(row=0, column=0, padx=10, pady=150)
        frame_1.configure(label_text=None)

        for i in range(7):
            ctk.CTkCheckBox(frame_1,).grid(row=i, padx=10, pady=10,sticky="w")
        frame_1.children["!ctkcheckbox"].configure(text="Destinos Culinarios",fg_color="#FA5F39")
        frame_1.children["!ctkcheckbox2"].configure(text="Tipos de cocina",fg_color="#FA5F39")
        frame_1.children["!ctkcheckbox3"].configure(text="Ingredientes",fg_color="#FA5F39")
        frame_1.children["!ctkcheckbox4"].configure(text="Precio Minimo",fg_color="#FA5F39")
        frame_1.children["!ctkcheckbox5"].configure(text="Precio Maximo",fg_color="#FA5F39")
        frame_1.children["!ctkcheckbox6"].configure(text="Popularidad",fg_color="#FA5F39")
        frame_1.children["!ctkcheckbox7"].configure(text="Actividad",fg_color="#FA5F39")
    
        boton1 = ctk.CTkButton(self, text="Filtrar",  fg_color="#FA5F39", command=self.resultado_filtro)
        boton1.place(x=25, y=400)

        boton2 = ctk.CTkButton(self, text="Regresar al menu",  fg_color="#FA5F39")
        boton2.place(x=250, y=400)
        
        self.toplevel_window = None
        
    def resultado_filtro(self):
        
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
if __name__ == "__main__":
    app = VistaFiltro()
    app.mainloop()
