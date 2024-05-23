import osmnx as ox
import tkinter as tk
from tkinter import messagebox
import graph
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(800, 600)
        self.attributes('-fullscreen', True)
        self.graph_content = None
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.title("")
        self.iconbitmap("tomboicono.ico")

        # Cargar la imagen de fondo
        self.original_image = Image.open("patrulleros.jpg")
    
        # Crear el Frame que ocupará todo el fondo
        self.background_frame = tk.Frame(self)
        self.background_frame.place(
            x=0, 
            y=0, 
            relwidth=1, 
            relheight=1
        )

        # Crear el Label para la imagen de fondo
        self.background_label = tk.Label(self.background_frame)
        self.background_label.pack(fill = tk.BOTH, expand=1)
        
        # Llamar a resize_background cuando la ventana cambie de tamaño
        self.bind("<Configure>", self.resize_background)
        # Asignar el evento de teclado F11 para alternar pantalla completa
        self.bind('<F11>', self.toggle_fullscreen)

        # Asignar el evento de teclado ESC para salir de pantalla completa
        self.bind('<Escape>', self.fullscreen_false)
        self.start_menu()

    def start_menu(self):
        # Crear el marco para contener el botón
        self.frame_start = tk.Frame(self.background_frame)
        self.frame_start.place(relx=0.5, rely=0.5, anchor='center')

        # Crear el botón
        self.button = tk.Button(self.frame_start, text="INICIAR", command=self.show_graph, cursor="hand2", highlightbackground=self['bg'])
        self.button.pack(expand=True)
  
    def resize_background(self, event):
        # Obtener el nuevo tamaño de la ventana
        new_width = self.background_frame.winfo_width()
        new_height = self.background_frame.winfo_height()

        # Redimensionar la imagen para ajustarla al nuevo tamaño de la ventana
        resized_image = self.original_image.resize((new_width, new_height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(resized_image)

        # Actualizar la imagen en el Label
        self.background_label.config(image=self.background_photo)
        self.background_label.image = self.background_photo
        
    def toggle_fullscreen(self, event=None):
        # Verifica si la ventana está en modo de pantalla completa
        if self.attributes('-fullscreen'):
            # Si está en modo de pantalla completa, cambia a modo normal
            self.attributes('-fullscreen', False)
            # Devuelve el botón F11 al estado original
            self.unbind('<F11>')
            self.bind('<F11>', self.toggle_fullscreen)
        else:
            # Si no está en modo de pantalla completa, cambia a pantalla completa
            self.attributes('-fullscreen', True)
            # Desactiva el botón F11 para evitar problemas al intentar salir de pantalla completa
            self.unbind('<F11>')
            # Vuelve a vincular la tecla F11 al método toggle_fullscreen
            self.bind('<F11>', self.toggle_fullscreen)
            
    def fullscreen_false(self, event=None):
        # Verifica si la ventana no está en modo de pantalla completa
        if self.attributes('-fullscreen'):
            # Si está en modo de pantalla completa, cambia a modo normal
            self.attributes('-fullscreen', False)
            # Devuelve el botón Escape al estado original
            self.unbind('<Escape>')
            self.bind('<Escape>', self.fullscreen_false)
    
    def show_graph(self):
        #Eliminar el boton
        self.button.destroy()
        # Cargar el grafo desde el archivo GraphML
        G = ox.load_graphml(graph.file_path)
        print(f"Grafo cargado desde el archivo: {graph.file_path}")
        
        # Dibujar el grafo solo si no está en caché
        if self.graph_content is None:
            fig, _ = ox.plot_graph(
                G, 
                show=False, 
                close=False,
                bgcolor = "#061100", 
                node_size=0, 
                node_edgecolor="#FFFFFF", 
                edge_alpha=0.2, 
                edge_linewidth=0.5
            )
            self.graph_content = fig
        else:
            fig = self.graph_content
        
        frame_map = tk.Frame()
        frame_map.place(
            relx=0.25,
            rely=0,
            relheight=0.75,
            relwidth=0.5
        )
        
        # Mostrar el gráfico en una ventana de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_map)
        canvas.draw()
        
        # Crear el widget para Tk y establecer su tamaño
        widget = canvas.get_tk_widget()
        widget.config(bg="#061100")
        widget.pack(fill = tk.BOTH, expand=1)
        
        # Cambiar el cursor al pasar sobre el widget del botón
        widget.bind("<Enter>", lambda event: widget.config(cursor="cross"))
        widget.bind("<Leave>", lambda event: widget.config(cursor=""))
        self.text_box()
        
    def text_box(self):
        frame_text = tk.Frame()
        frame_text.place(
            relx=0.25,
            rely=0.75,
            relwidth=0.5,
            relheight=0.25
        )
        
        self.display_label = tk.Label(frame_text, text="Bienvenido, este es el mapa de Villavicencio, con los CAIS", bg="#0F8D00")
        self.display_label.pack(fill = tk.BOTH, expand=1)
        
    def close_window(self):
        # MOstrar ventana para confirmar salida
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            # Salir de la aplicación de forma limpia
            self.destroy()
            sys.exit()
            
