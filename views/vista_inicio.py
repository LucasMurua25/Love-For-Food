import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Love For Food")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(
            Image.open(os.path.join(current_path,"image","tkinterlogo.png")),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=1, column=5)

       # crear el frame de Inicio
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=1, column=5)
        
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="INICIO", command=self.iniciar, width=75,
        )
        self.login_button.grid(row=0, column=0, padx=0, pady=(0, 0))

    def iniciar(self):
        self.login_frame.grid_forget()  # eliminar el frame de inicio
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # mostrar el frame de login  

if __name__ == "__main__":
    app = App()
    app.mainloop()

