import tkinter as tk
import subprocess


def regresar():
    subprocess.Popen(['python', 'deteccionRostro\\interfazG\\menu.py'])
    exit()


def validarEmpleado(idEmpleado):
    match idEmpleado:
        case (202130060109 | 202110060173 | 201920060176 | 201920130058):
            subprocess.Popen(['python', 'deteccionRostro\\reconocimiento.py'])
            exit()
        case _:
            lblError.configure(fg="red")


def getNumEmpleado():

    entradaUser = int(txtNumEmpleado.get().strip())
    validarEmpleado(entradaUser)
    txtNumEmpleado.delete(0, tk.END)


root = tk.Tk()

root.title("Monitoreo de Empleados")
window_height = 500
window_width = 320
root.geometry(f"{window_height}x{window_width}")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_height}x{window_width}+{x}+{y}")

fontTitulo = ("Helvetica", 14, "bold")  # se define la fuente tipo tupla
etiqueta = tk.Label(root, text="Validacion De Empleado", font=fontTitulo)
etiqueta.pack(pady=(20, 10))

etiqueta2 = tk.Label(root, text="Ingrese su numero de empleado")
etiqueta2.pack(pady=(20, 10))

lblError = tk.Label(
    root, text="El Empleado no esta registrado", fg="#F0F0F0")
lblError.pack(pady=(20, 10))

txtNumEmpleado = tk.Entry(root)
txtNumEmpleado.pack(pady=20)

botonIngresar = tk.Button(root, text="Ingresar", bg="#00FF00", fg="black", width=17,
                          command=lambda: getNumEmpleado())
botonIngresar.pack(side="left", padx=(100, 20))

botonAtras = tk.Button(root, text="Atras", bg="#611504", fg="white",
                       width=17, command=lambda: regresar())
botonAtras.pack(side="left", padx=20)

root.mainloop()
