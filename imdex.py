import tkinter as tk
from tkinter import Label, Button, Frame

# Configura la ventana principal
app = tk.Tk()
app.title("Reproductor de Música")
app.geometry('800x600')  # Ajusta el tamaño de la ventana

# Configura el marco del título
titulo = Frame(app, background="black", height=70)
titulo.pack(fill=tk.X)

def menu():
    print('hi')
    
# Función para borrar el texto de ejemplo cuando el campo recibe enfoque
def on_focus_in(event):
    if ct.get() == 'Buscar canción o artista':
        ct.delete(0, tk.END)  # Borra el texto de ejemplo

# Función para restaurar el texto de ejemplo si el campo queda vacío
def on_focus_out(event):
    if ct.get() == '':
        ct.insert(0, 'Buscar canción o artista')  # Restaura el texto de ejemplo

# Campo de entrada para la búsqueda
ct = tk.Entry(app, font=("Arial", 14))
ct.place(x=50, y=20, height=30, width=400)
ct.insert(0, "Buscar canción o artista")

# Configura los eventos de enfoque
ct.bind('<FocusIn>', on_focus_in)
ct.bind('<FocusOut>', on_focus_out)

# Ejecuta la aplicación
app.mainloop()
