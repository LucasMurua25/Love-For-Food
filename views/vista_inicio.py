import tkinter as tk
from tkinter import ttk



class VisualizacionImagen:

    def __init__(self, master):
        self.master = master
        self.inicializar_gui()

    def inicializar_gui(self):
        canvas = tk.Canvas(self.master, width=667, height=380)
        canvas.pack()

        img_logo_python = tk.PhotoImage(file='tkinterlogo.png')
        canvas.create_image(0, 0, anchor=tk.NW, image=img_logo_python)
        canvas.image = img_logo_python

         # Crea un boton de inicio
        button = ttk.Button(self.master, text="Inicio", style="my.TButton")
        button.pack()

         # Cambia el color de fondo del boton 
        style = ttk.Style()
        style.configure("my.TButton", background="orange")

    
def main():
    root = tk.Tk()
    root.title('LoveForFood V1.0')

    ventana = VisualizacionImagen(root)

    root.mainloop()

if __name__ == "__main__":
    main()