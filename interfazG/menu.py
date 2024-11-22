import tkinter as tk


root = tk.Tk() #creamos la ventana principal
root.title("Monitoreo de Empleados") # Se coloca el titulo en la ventana
window_height = 500 # se inicializa la altura
window_width = 320 #se inicializa el ancho

screen_width = root.winfo_screenwidth() #obtenemos el ancho de la pantalla
screen_height = root.winfo_screenheight() #obtenemos el alto de la pantalla

x = (screen_width // 2) - (window_width // 2) # En x se guarda el valor de la mitad de la pantalla - la mitad de el ancho de la ventana
y = (screen_height // 2) - (window_height // 2) # En y se guarda el valor de la mitad de la pantalla - la mitad de la altura de la ventana

root.geometry(f"{window_height}x{window_width}+{x}+{y}") # se establece la geometria de la ventana

#COMPONENTES DE LA PANTALLA PRINCIPAL

etiqueta = tk.Label(root, text="Seleccione una opcion")
etiqueta.pack(pady=(10,0))

botonRostros = tk.Button(root, text="Monitoreo de Rostros", command=lambda: print("Boton 1"))
botonRostros.pack(pady=(30,20))

botonUsuario = tk.Button(root, text="Manual de Usuario", command=lambda: print("Boton 2"))
botonUsuario.pack(pady=(20,20))

botonSalir = tk.Button(root, text="Salir", command=lambda: print("Boton 3"))
botonSalir.pack(pady=(20,20))
root.mainloop()