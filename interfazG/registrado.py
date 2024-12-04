import tkinter as tk
import subprocess
import sys

usuario = ""
fechaHora = ""


def get_EmpleadoInfo():

    empleado = sys.argv[1]
    date = sys.argv[2]
    return empleado, date


def regresarMenu():
    subprocess.Popen(['python', 'deteccionRostro\\interfazG\\menu.py'])
    exit()


usuario, fechaHora = get_EmpleadoInfo()

root = tk.Tk()

root.title("Empleado Reconocido Exitosamente")
window_height = 450
window_width = 220
root.minsize(window_height, window_width)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_height}x{window_width}+{x}+{y}")

fontTitulo = ("Helvetica", 14, "bold")  # se define la fuente tipo tupla
etiqueta = tk.Label(root, text=f"Bienvenid@ {usuario}", font=fontTitulo)
etiqueta.pack(pady=(20, 30))

etiqueta2 = tk.Label(
    root, text=f"Fecha y dia de Ingreso: {fechaHora}", font=fontTitulo)
etiqueta2.pack(pady=(20, 30))

botonMenu = tk.Button(root, text="Ir al Menu", bg="#611504", fg="white",
                      width=17, command=lambda: regresarMenu())
botonMenu.pack(padx=(50, 20), pady=(15, 0))

root.mainloop()
