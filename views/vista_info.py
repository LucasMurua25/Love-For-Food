import tkinter as tk


class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un destino.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.destino_label = tk.Label(self, text="")
        self.destino_label.pack(pady=50)
        self.destino_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar al menú de búsqueda",
            command=self.controlador.regresar_destino,
        )
        self.boton_regresar.pack(pady=10)

    def mostrar_info_destino(self, DestinoCulinario):
        """
        Muestra la información del destino recibido como parámetro.
        """
        info = f"Nombre : {DestinoCulinario.nombre}\n Ubicación: {DestinoCulinario.id}\n Tipo De Cocina: {DestinoCulinario.tipo_cocina}\n Popularidad: {DestinoCulinario.popularidad}\n Ingredientes Ocupados: {DestinoCulinario.ingredientes} \n Disponibilidad: {DestinoCulinario.disponibilidad}\nDireccion: {DestinoCulinario.id_ubicacion}\n Precio Maximo: $ {DestinoCulinario.precio_maximo} Precio Minimo: ${DestinoCulinario.precio_minimo} \n{DestinoCulinario.imagen} "
