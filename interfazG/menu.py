import tkinter as tk
import subprocess


def monitoreoRostro():
    # ejecuta en el CMD el comando como un subproceso
    subprocess.Popen(['python', 'deteccionRostro\\interfazG\\validateUser.py'])
    exit()

#Metodo de ejecucion del boton de manual de usuario
def opcionesManualUsuarios():
    subprocess.Popen(['python', 'deteccionRostro\\interfazG\\opcionesManual.py'])
    exit()

# CREACION DE VENTANA PRINCIPAL

root = tk.Tk()  # instanciamos en root la ventana principal
root.title("Monitoreo de Empleados")  # Se coloca el titulo en la ventana
window_height = 500  # se inicializa la altura
window_width = 320  # se inicializa el ancho

screen_width = root.winfo_screenwidth()  # obtenemos el ancho de la pantalla
screen_height = root.winfo_screenheight()  # obtenemos el alto de la pantalla

# En x se guarda el valor de la mitad de la pantalla - la mitad de el ancho de la ventana
x = (screen_width // 2) - (window_width // 2)
# En y se guarda el valor de la mitad de la pantalla - la mitad de la altura de la ventana
y = (screen_height // 2) - (window_height // 2)

# se establece la geometria de la ventana
root.geometry(f"{window_height}x{window_width}+{x}+{y}")

# COMPONENTES DE LA PANTALLA PRINCIPAL

fontTitulo = ("Helvetica", 14, "bold")  # se define la fuente tipo tupla
etiqueta = tk.Label(root, text="Seleccione una opcion", font=fontTitulo)
etiqueta.pack(pady=(10, 0))

botonRostros = tk.Button(root, text="Monitoreo de Rostros", bg="#05365c", fg="white", width=17,
                         command=lambda: monitoreoRostro())
botonRostros.pack(pady=(30, 20))

botonUsuario = tk.Button(root, text="Manual de Usuario", bg="#013d24", fg="white", width=17,
                         command=lambda: opcionesManualUsuarios())
botonUsuario.pack(pady=(20, 20))

botonSalir = tk.Button(root, text="Salir", bg="#611504",  width=17,
                       fg="white", command=lambda: exit())
botonSalir.pack(pady=(20, 20))
root.mainloop()
