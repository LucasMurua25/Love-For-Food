
import customtkinter as ctk

class PantallaInfo(ctk.CTk):
  width = 900
  height = 600
  def __init__(self,master=None,controlador=None):
      super().__init__(master)
      self.master = master
      self.controlador = controlador
      self.actividad_label = ctk.CTkLabel(self, text="")
      self.actividad_label.pack(pady=50)
      self.actividad_label.config(justify=ctk.LEFT)
      self.boton_regresar = ctk.CTkButton(
            self,
            text="Regresar al menu",
            command=self.controlador.regresar_menu,  fg_color="#FA5F39")
      self.boton_regresar.pack(pady=10)

                # Mostrar la informacion del destino
  def mostrar_info_destino(self, Actividad):
      info=f"Numero de actividad : {Actividad.id}\n Actividad: {Actividad.nombre}\n Destino: {Actividad.destino_id}\n Hora de Inicio: {Actividad.hora_inicio}"
      #self.actividad_label=[""]=info
