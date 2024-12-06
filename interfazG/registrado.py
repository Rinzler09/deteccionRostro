import tkinter as tk
import subprocess
import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH para facilitar las importaciones
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Luego de esto, puedes importar `guardar_empleado_en_db` sin problema
from deteccionRostro.interfazG.Crud import guardar_empleado_en_db

# Definición de variables
usuario = ""
fechaHora = ""

# Función para obtener información del empleado desde los argumentos de línea de comandos
def get_EmpleadoInfo():
    empleado = sys.argv[1]
    date = sys.argv[2]
    return empleado, date

# Función para regresar al menú principal ejecutando el script `menu.py`
def regresarMenu():
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'menu.py'))
    subprocess.Popen(['python', script_path])
    exit()

# Obtener la información del empleado para la base de datos
usuario, fechaHora = get_EmpleadoInfo()

# Guardar los datos del empleado en la base de datos
guardar_empleado_en_db(usuario, fechaHora)

# Configuración de la interfaz gráfica de Tkinter
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

# Etiqueta de bienvenida
fontTitulo = ("Helvetica", 14, "bold")
etiqueta = tk.Label(root, text=f"Bienvenid@ {usuario}", font=fontTitulo)
etiqueta.pack(pady=(20, 30))

# Etiqueta con fecha y hora de ingreso
etiqueta2 = tk.Label(root, text=f"Fecha y dia de Ingreso: {fechaHora}", font=fontTitulo)
etiqueta2.pack(pady=(20, 30))

# Botón para regresar al menú
botonMenu = tk.Button(root, text="Ir al Menu", bg="#611504", fg="white",
                      width=17, command=lambda: regresarMenu())
botonMenu.pack(padx=(50, 20), pady=(15, 0))

root.mainloop()
