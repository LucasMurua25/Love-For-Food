from typing import Any
import customtkinter as ctk
from PIL import Image
import os
from tkintermapview import TkinterMapView
#from controladores.controller.Controlador_Inicio import ControladorInicio

ctk.set_appearance_mode("System")

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
        


        #caracteristicas del boton iniciar
        self.back_button = ctk.CTkButton(
            self.main_frame, text="Iniciar", command=self.iniciar, width=100,border_spacing=5,font=("bold",15)
        )
        self.back_button.grid(row=1, column=1, padx=20, pady=(15, 15))
        
        #DEFINICIONES
        
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
        ) 
        self.main_frame.place(relx=0.41, rely=0.66)# mostrar el frame principal
    def iniciar(self):
        print( "Presionó Iniciar!")
        self.main_frame.grid_forget()
        self.main_frame.place_forget()  # eliminar el frame de inicio
        #INCORPORAR MENU
        # Botón de inicio de sesión
        self.boton1=ctk.CTkButton(self, text="Destinos culinarios",  fg_color="#FA5F39",command=self.destinos_culinarios)
        self.boton1.place(x=50, y=200)
        self.boton2 = ctk.CTkButton(self, text="Busqueda y Filtrado",  fg_color="#FA5F39",command=self.busqueda_filtrado)
        self.boton2.place(x=50, y=350)
        self.boton3 = ctk.CTkButton(self, text="Planificar Visitas",  fg_color="#FA5F39",command=self.planificar_visitas)
        self.boton3.place(x=700, y=350)
        self.boton4 = ctk.CTkButton(self, text="Review y Calificaciones",  fg_color="#FA5F39",command=self.review_calificaciones)
        self.boton4.place(x=700, y=200)  # mostrar el frame del menu
        #IR A DESTINO CULINARIO(MAPA)
    def destinos_culinarios(self):
        print( "Presionó DestinoCulinario!")
        self.boton1.place_forget()
        self.boton2.place_forget()
        self.boton3.place_forget()
        self.boton4.place_forget()
        self.marker_list = []

        #Creacion de 2 Freams de trabajo
        #trabajaremos con dos columnas de frame, dentro de la columna derecha ira el mapa(frame_left)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #Caracteristicas de la columna izquierda
        self.frame_left = ctk.CTkFrame(master=self, width=150, corner_radius=0, fg_color="#EEEEEE")
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        #Caracteristicas de la columna derecha
        self.frame_right = ctk.CTkFrame(master=self, corner_radius=0,fg_color="#EEEEEE")
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        self.frame_right.grid()
        self.frame_left.grid()
        #Fream o Columna izquierda_left

        self.frame_left.grid_rowconfigure(2, weight=1)

        self.button_1 = ctk.CTkButton(master=self.frame_left,
                                                text="Marcadores",
                                                command=self.set_marker_event,fg_color="#FA5F39")
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        self.button_2 = ctk.CTkButton(master=self.frame_left,
                                                text="Borrar Marcadores",
                                                command=self.clear_marker_event,fg_color="#FA5F39")
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

        self.map_label = ctk.CTkLabel(self.frame_left, text="V i s t a  E n:", anchor="w")
        self.map_label.grid(row=2, column=0, padx=(20, 20), pady=(65, 0))
        self.map_option_menu = ctk.CTkOptionMenu(self.frame_left,fg_color="#FA5F39", values=["OpenStreetMap", "Google Maps"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=3, column=0, padx=(20, 20), pady=(0, 100))
        self.map_option_menu.grid()
        # Frame Derecho, configuracion

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = ctk.CTkEntry(master=self.frame_right,
                                            placeholder_text=" ")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = ctk.CTkButton(master=self.frame_right,
                                                text="Buscar",
                                                width=90,
                                                command=self.search_event,fg_color="#FA5F39")
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        
         # Valores Predeterminados
        self.map_widget.set_address("Salta")
        self.map_option_menu.set("OpenStreetMap")
                #self.map_widget.grid()
                #self.map_option_menu.grid()
    #Buscar Lugares por nombre o direccion   ####Falllaaaaaaa
    def search_event(self):
            self.map_widget.set_address(self.entry.get())
         #Mostrar marcadores
    def set_marker_event(self):
            current_position = self.map_widget.get_position()
            self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))
          #Limpiar seccion Marcadores
    def clear_marker_event(self):
            for marker in self.marker_list:
                 marker.delete()

         #Modificar Vista del mapa
    def change_map(self, new_map: str):
            if new_map == "OpenStreetMap":
                 self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
            elif new_map == "Google Maps":
                 self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
       
    def busqueda_filtrado(self):
       print( "Presionó filtrado!")
    def planificar_visitas(self):
       print( "Presionó visitas!")
    def review_calificaciones(self):
       print( "Presionó calificaciones!")

if __name__ == "__main__":
 app = App()
 app.mainloop()


