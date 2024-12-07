from email.message import EmailMessage
import smtplib
from tkinter import *
from tkinter import messagebox
import os
import subprocess
import re

"------------INTERFAZ TKINTER------------"
ventana = Tk()
ventana.title("ENVIAR PDF AL CORREO ELECTRÓNICO")
ventana.geometry("450x250")
ventana.resizable(0, 0)
ventana.config(bd=10)

# Centrar la ventana en la pantalla
ancho_ventana = 450
alto_ventana = 250
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
pos_y = int((alto_pantalla / 2) - (alto_ventana / 2))

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

Label(ventana, text="ENVIAR PDF VIA GMAIL", fg="black", font=("Arial", 15, "bold"), padx=5, pady=5).pack(pady=10)

# Variables
destinatario = StringVar(ventana)

Label(ventana, text="Correo destinatario:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).pack()
Entry(ventana, textvariable=destinatario, width=40).pack()

# Añadir un nuevo botón en la esquina superior derecha
def opcionesManualUsuarios():
    subprocess.Popen(['python', 'deteccionRostro\\interfazG\\opcionesManual.py'])
    exit()

boton = Button(ventana, text="Menu PDF", command=opcionesManualUsuarios, bg="#5d26c3", fg="white", font=("Arial", 8, "bold"))
boton.place(x=365, y=10)  # Posiciona el botón en la esquina superior derecha

"------------ENVIO DE CORREO CON PDF------------"
def enviar_email():
    remitente = "techdata053@gmail.com"
    password = "cvec zfgp kfdh vvxt"  # Clave personal debe ser una contraseña de aplicación generada por Google
    destinatario_correo = destinatario.get()
    
    # Validar el correo electrónico
    patron_correo = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(patron_correo, destinatario_correo):
        messagebox.showerror("ERROR", "El correo electrónico no es válido. Por favor, ingrese un correo válido.")
        return

    asunto = "Manual de Usuario - Reconocimiento de Rostros"
    
    # Crear el email
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario_correo
    email["Subject"] = asunto

    # Crear el contenido del correo con HTML
    mensaje_html = """
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #ddcdfc; padding: 20px;">
        <div style="max-width: 800px; margin: auto; background: #f4f4f4; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
            <h2 style="color: #05365c;">Manual de Usuario - Reconocimiento de Rostros</h2>
            <p>Estimado/a usuario/a,</p>
            <p>Adjunto a este correo encontrará el manual de usuario en formato PDF. Esperamos que le sea de gran utilidad.</p>
            <img src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg" alt="Manual de Reconocimiento de Rostros" style="width: 100%; height: auto; border-radius: 10px;">
            <p style="margin-top: 20px;">Para cualquier consulta adicional, no dude en ponerse en contacto con nosotros.</p>
            <p style="color: #888;">Saludos cordiales,<br>El equipo de Reconocimiento de Rostros</p>
        </div>
    </body>
    </html>
    """

    # Adjuntar el contenido HTML al email
    email.add_alternative(mensaje_html, subtype="html")

    # Adjuntar el PDF
    pdf_path = os.path.join(os.path.dirname(__file__), "..", "ManualPDF", "Informe - Reconocimiento facial.pdf")  # Ruta relativa al archivo PDF
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            email.add_attachment(pdf_file.read(), maintype="application", subtype="pdf", filename=os.path.basename(pdf_path))
    else:
        messagebox.showerror("ERROR", "El archivo PDF no se encuentra en la ubicación especificada.")
        return

    try:
        # Enviar el email
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(remitente, "hsunacfpeeadehlt")
        smtp.send_message(email)
        smtp.quit()
        messagebox.showinfo("MENSAJERIA", "PDF enviado correctamente")
    except Exception as e:
        messagebox.showerror("ERROR", f"No se pudo enviar el correo: {e}")

"------------BOTON------------"
Button(ventana, text="ENVIAR PDF", command=enviar_email, height=2, width=15, bg="#05365c", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

ventana.mainloop()
