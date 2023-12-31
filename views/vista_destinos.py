import customtkinter as ctk
from tkintermapview import TkinterMapView


class Mapa(ctk.CTk):

    APP_NAME = "Destinos en el Mapa"
    WIDTH = 900
    HEIGHT = 600

    def __init__(self,master=None,controlador=None, destinos=None, ubicaciones=None,markers=None):
        super().__init__(master)
        self.master=master
        self.controlador=controlador
        self.destinos=destinos
        self.ubicaciones=ubicaciones
        self.markers=ubicaciones
        self.destino_selec={}
        self.title(Mapa.APP_NAME)
        self.geometry(str(Mapa.WIDTH) + "x" + str(Mapa.HEIGHT))
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
        self.button_0 = ctk.CTkButton(master=self.frame_left,
                                                text="Volver al Menu",command=self.controlador.regresar_menu,fg_color="#FA5F39")
        self.button_0.grid(pady=(20,0), padx=(20, 20), row=3, column=0)

        self.button_1 = ctk.CTkButton(master=self.frame_left,
                                                text="Marcadores",
                                                command=self.set_marker_event,fg_color="#FA5F39")
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        self.map_label = ctk.CTkLabel(self.frame_left, text="V i s t a  E n:", anchor="w")
        self.map_label.grid(row=2, column=0, padx=(20, 20), pady=(65, 0))
        self.map_option_menu = ctk.CTkOptionMenu(self.frame_left,fg_color="#FA5F39", values=["OpenStreetMap", "Google Maps"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=3, column=0, padx=(20, 20), pady=(0, 100))


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
        for ubicacion in (self.markers):
            self.agregar_marcador(ubicacion.coordenadas, '')
            
        #agregar marcador

    def agregar_marcador(self,coordenadas, texto):
        self.Disponiblidad = ctk.CTkLabel(self, width=30, height=1)
        self.Popularidad = ctk.CTkLabel(self, width=30, height=1)
        if self.destino_selec.disponibilidad == 1:
            f=self.Disponiblidad.config(texto='Abierto')    
        else:
            f=self.Disponiblidad.config(texto='Cerrado')
        texto=self.Popularidad.config(text=f'{self.destino_selec.popularidad} estrellas, Disponibilidad: {f}')
        
        return self.map_widget.set_marker(coordenadas, text=texto)


    #Modificar Vista del mapa
    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google Maps":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def on_closing(self):
        self.destroy()

    def start(self):
        self.mainloop()
