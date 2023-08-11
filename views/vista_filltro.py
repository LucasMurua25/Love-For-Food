import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkLabel, CTkInputDialog
from PIL import ImageTk, Image
import json
import os




class VistaFiltro(ctk.CTk):
    width = 900
    height = 600
    def __init__(self):
        super().__init__()
        # Agrega un mensaje en el label 
        self.lbl_mensaje = ctk.CTkLabel(self.master, text='¡Selecciona tu destino culinario, de acuerdo a tus preferencias!', font=('Roboto Condensed', 20))
        self.lbl_mensaje.place(x=40, y=100)

        frame_1 = ctk.CTkScrollableFrame(self, orientation="vertical", label_text="should not appear", fg_color="transparent")
        frame_1.grid(row=0, column=0, padx=10, pady=150)
        frame_1.configure(label_text=None)
        # Crea los checkbox de la lista
        for i in range(2):
            ctk.CTkCheckBox(frame_1,).grid(row=i, padx=10, pady=10,sticky="w")
        frame_1.children["!ctkcheckbox"].configure(text="Tipos de cocina",fg_color="#FA5F39")
        frame_1.children["!ctkcheckbox2"].configure(text="Ingredientes",fg_color="#FA5F39")
#        frame_1.children["!ctkcheckbox3"].configure(text="Precio Maximo",fg_color="#FA5F39")
#        frame_1.children["!ctkcheckbox4"].configure(text="Precio Minimo",fg_color="#FA5F39")
#        frame_1.children["!ctkcheckbox5"].configure(text="Popularidad",fg_color="#FA5F39")
#        frame_1.children["!ctkcheckbox6"].configure(text="Actividad",fg_color="#FA5F39")  
        #Boton de filtrado
        boton1 = ctk.CTkButton(self, text="Filtrar",  fg_color="#FA5F39", command=self.resultado_filtro)
        boton1.place(x=25, y=400)
        #Boton de regreso al menu
        boton2 = ctk.CTkButton(self, text="Regresar al menu",  fg_color="#FA5F39")
        boton2.place(x=250, y=400)

        self.toplevel_window = None  
             
    def resultado_filtro(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # crea una ventana emergente
        else:
            self.toplevel_window.focus()  # Hace foco en la ventana 


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.master=master
        self.controlador=controlador
        self.geometry("400x300")
        self.title("LoveForFood V1.0")
        self.label = ctk.CTkLabel(self, text="Resultado")
        self.label.pack(padx=20, pady=20)
        self.attributes('-topmost', True)
                # Agregar un cuadro de texto para el buscador
        self.buscador_entry = tk.Entry(self, width=40)
        self.buscador_entry.place(x=10, y=120)
            #self.listbox = tk.Listbox(self, width=35, fg="#595959", font=("Arial", 10))
        self.listbox = tk.Listbox(self, width=35, font=("Arial", 10))
        self.listbox.place(x=10, y=150)

        # Asocia el evento de selección del Listbox a la función mostrar_informacion_destino
        self.listbox.bind("<<ListboxSelect>>", self.mostrar_informacion_destino)
        # Asociar el evento de escritura al buscador
        self.buscador_entry.bind("<KeyRelease>", self.filtrar_destinos)


    def obtener_destino_seleccionado(self):
        """
        Retorna el destino_id del destino seleccionado en la lista.
        """
        indice = self.listbox.curselection()
        print(indice)
        if indice:
            nombre_destino_seleccionado = self.listbox.get(indice[0])
            destino_seleccionado = next((destino for destino in self.controlador.obtener_destinos() if destino.nombre == nombre_destino_seleccionado), None)
            if destino_seleccionado:
                return destino_seleccionado.id
        return None   
    
    def filtrar_destinos(self, event):
        """
        Filtra los destinos en el Listbox según el término de búsqueda ingresado en el cuadro de texto.
        """
        termino_busqueda = self.buscador_entry.get().lower()
        destinos = self.controlador.destinos  # Usamos la lista de destinos del controlador

        # Filtrar destinos según el término de búsqueda
        destinos_filtrados = [destino for destino in destinos if termino_busqueda in destino.tipo_cocina.lower() or
                              any(termino_busqueda in actividad.nombre.lower() for actividad in self.controlador.actividades if actividad.destino_id == destino.id)]

        # Actualizar el Listbox con los destinos filtrados
        self.listbox.delete(0, ctk.END)
        for destino in destinos_filtrados:
            self.listbox.insert(ctk.END, destino.nombre)

    def mostrar_informacion_destino(self, event):        """ Muestra los ingredientes y el tipo de cocina del destino seleccionado en las etiquetas. """
        indice = obtener_destino_seleccionado(self)
        if indice is not None:
            destino_seleccionado = self.controlador.obtener_destinos()[indice -1]
#            ingredientes = ", ".join(destino_seleccionado.ingredientes)
            tipo_cocina = destino_seleccionado.tipo_cocina
            nombre = destino_seleccionado.nombre

            # Obtener actividades del destino seleccionado
            actividades_destino = [actividad.nombre for actividad in self.controlador.actividades if actividad.destino_id == destino_seleccionado.id]

            self.destino_label.config(text=f"{nombre}")
            #self.ingredientes_label.config(text=f"Ingredientes: {ingredientes}")
            self.tipo_cocina_label.config(text=f"Tipo de cocina: {tipo_cocina}")

            # Actualizar etiqueta con las actividades del destino
                self.actividades_label.config(text=f"Actividades: {', '.join(actividades_destino)}")
            else:
            # Si no se ha seleccionado ningún destino, borrar el 
            # contenido de las etiquetas
                self.destino_label.config(text="")
                self.tipo_cocina_label.config(text="")
                self.actividades_label.config(text="")

        def mostrar_informacion_destino(self, event):
        """
        Muestra los ingredientes y el tipo de cocina del destino 
        seleccionado en las etiquetas.
        """
            indice = self.obtener_destino_seleccionado()
            if indice is not None:
                destino_seleccionado = self.controlador.obtener_destinos()[indice -1]
#            ingredientes = ", ".join(destino_seleccionado.ingredientes)
                tipo_cocina = destino_seleccionado.tipo_cocina
                nombre = destino_seleccionado.nombre

            # Obtener actividades del destino seleccionado
                actividades_destino = [actividad.nombre for actividad in self.controlador.actividades if actividad.destino_id == destino_seleccionado.id]

                self.destino_label.config(text=f"{nombre}")
            #self.ingredientes_label.config(text=f"Ingredientes: {ingredientes}")
                self.tipo_cocina_label.config(text=f"Tipo de cocina: {tipo_cocina}")

            # Actualizar etiqueta con las actividades del destino
                self.actividades_label.config(text=f"Actividades: {', '.join(actividades_destino)}")
            else:
            # Si no se ha seleccionado ningún destino, borrar el 
            # contenido de las etiquetas
                self.destino_label.config(text="")
                self.tipo_cocina_label.config(text="")
                self.actividades_label.config(text="")
if __name__ == "__main__":
    app = VistaFiltro()
    app.mainloop()