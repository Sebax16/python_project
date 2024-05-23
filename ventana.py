import tkinter as tk

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    raiz.attributes("-fullscreen", fullscreen)

def end_fullscreen(event=None):
    global fullscreen
    fullscreen = False
    raiz.attributes("-fullscreen", fullscreen)
    
# def set_alpha(event=None):
#     raiz.attributes("-alpha", 0.5)

raiz=tk.Tk()
fullscreen = False

# Configuracion, aspectos visuales de la ventana
raiz.geometry("1920x1080+0+0")
raiz.minsize(width=600, height=400)
    # Icono de la ventana
raiz.iconbitmap("tomboicono.ico")
    # Titulo de la ventana
raiz.title("Proyecto")
    # Fondo de la ventana
raiz.configure(bg = "green")

# Asignacion de botones
    # Asigna la función para alternar pantalla completa al presionar 'F11'
raiz.bind("<F11>", toggle_fullscreen)
    # Asigna la función para salir de pantalla completa al presionar 'Escape'
raiz.bind("<Escape>", end_fullscreen)
    # Asigna la función para salir de pantalla completa al presionar 'Escape'
raiz.bind("<Escape>", end_fullscreen)
toggle_button = tk.Button(raiz, text="Hola!", command=print("hola"))
toggle_button.pack(pady=400)

raiz.mainloop()