import click
import customtkinter as ctk
from tkintermapview import TkinterMapView



lista=[]

class MapRut(ctk.CTk):

    APP_NAME = "Destinos en el Mapa"
    WIDTH = 600
    HEIGHT = 400
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(MapRut.APP_NAME)
        self.geometry(str(MapRut.WIDTH) + "x" + str(MapRut.HEIGHT))
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)
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

        #Fream o Columna izquierda_left

        self.frame_left.grid_rowconfigure(2, weight=1)

        self.button_1 = ctk.CTkButton(master=self.frame_left,
                                                text="Destinos señalados",
                                                command=self.set_marker_event,fg_color="#FA5F39")
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        self.button_2 = ctk.CTkButton(master=self.frame_left,
                                                text="Borrar Destinos",
                                                command=self.clear_marker_event,fg_color="#FA5F39")
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)
        self.button_3 = ctk.CTkButton(master=self.frame_left,
                                                text="Crear Ruta",command=self.create_route,fg_color="#FA5F39")
        self.button_3.grid(pady=(5, 0), padx=(20, 20), row=2, column=0)
        self.button_4 = ctk.CTkButton(master=self.frame_left,
                                                text="Borrar Ruta",command=self.delete_route,fg_color="#FA5F39")
        self.button_4.grid(pady=(0, 0), padx=(20, 20), row=4, column=0)

        self.map_label = ctk.CTkLabel(self.frame_left, text="V i s t a  E n:", anchor="w")
        self.map_label.grid(row=5, column=0, padx=(20, 20), pady=(50, 0))
        self.map_option_menu = ctk.CTkOptionMenu(self.frame_left,fg_color="#FA5F39", values=["OpenStreetMap", "Google Maps"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=6, column=0, padx=(20, 20), pady=(0, 100))


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

    #Buscar Lugares por nombre o direccion
    def search_event(self):
        self.map_widget.set_address(self.entry.get())
    #Mostrar marcadores
    def set_marker_event(self):
        click_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(click_position[0], click_position[1]))
        for direc in lista:
            if click_position== direc:
                lista.remove(direc)
        lista.append(click_position)
    #Limpiar seccion Marcadores
    def clear_marker_event(self):
        lista.clear()
        for marker in self.marker_list:
            marker.delete()

    #Modificar Vista del mapa
    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google Maps":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    #Crear Ruta Personalizada
    def create_route(self):
        path_1 = self.map_widget.set_path(lista)
    
    #Borrar Ruta
    def delete_route(self):
        self.map_widget.delete_all_path()

    def on_closing(self):
        self.destroy()

    def start(self):
        self.mainloop()
