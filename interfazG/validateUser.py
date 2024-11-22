import tkinter as tk

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

etiqueta = tk.Label(root, text="Validacion De Empleado")
etiqueta.pack(pady=(20,10))

etiqueta2 = tk.Label(root, text="Ingrese su numero de empleado")
etiqueta2.pack(pady=(20,10))

botonIngresar= tk.Button(root, text="Ingresar", command=lambda: print("Boton 2"))
botonIngresar.pack(pady=(20,20))

botonAtras = tk.Button(root, text="Atras", command=lambda: print("Boton 3"))
botonAtras.pack(pady=(20,20))


root.mainloop()
