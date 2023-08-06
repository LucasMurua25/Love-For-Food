import customtkinter as ctk
from customtkinter import CTkLabel, CTkInputDialog
from PIL import ImageTk, Image
from tkinter import scrolledtext

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("LoveForFood V1.0")
        self.label = ctk.CTkLabel(self, text="Resultado")
        self.label.pack(padx=20, pady=20)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoveForFood V1.0")
        self.geometry("650x550")
        
        # Cargar la imagen de fondo
        image = Image.open("tkinterlogo.png")
        photo = ImageTk.PhotoImage(image)
        
        # Agregar la imagen de fondo a un widget Label
        label = CTkLabel(self, text="" ,image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)


        checkbox_1 = ctk.CTkCheckBox(self, text="Destinos culinarios",  fg_color="#FA5F39")
        checkbox_1.place(x=25, y=200)
        checkbox_2 = ctk.CTkCheckBox(self, text="Tipo de cocina",  fg_color="#FA5F39")
        checkbox_2.place(x=25, y=250)
        checkbox_3 = ctk.CTkCheckBox(self, text="Ingredientes",  fg_color="#FA5F39")
        checkbox_3.place(x=25, y=300)
        checkbox_4 = ctk.CTkCheckBox(self, text="Precio Maximo",  fg_color="#FA5F39")
        checkbox_4.place(x=25, y=350)
        checkbox_5 = ctk.CTkCheckBox(self, text="Precio Minimo",  fg_color="#FA5F39")
        checkbox_5.place(x=180, y=200)
        checkbox_6 = ctk.CTkCheckBox(self, text="Popularidad",  fg_color="#FA5F39")
        checkbox_6.place(x=180, y=250)
        checkbox_7 = ctk.CTkCheckBox(self, text="Actividad",  fg_color="#FA5F39")
        checkbox_7.place(x=180, y=250)

        
        boton1 = ctk.CTkButton(self, text="Filtrar",  fg_color="#FA5F39", command=self.resultado_filtro)
        boton1.place(x=250, y=400)
        
        self.toplevel_window = None
        
    def resultado_filtro(self):
        
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
         
            
           
app = App()
app.mainloop()