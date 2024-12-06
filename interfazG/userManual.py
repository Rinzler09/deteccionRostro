from email.message import EmailMessage
import smtplib
from tkinter import *
from tkinter import messagebox
import os

"------------INTERFAZ TKINTER------------"
ventana = Tk()
ventana.title("ENVIAR PDF AL CORREO ELECTRÓNICO")
ventana.geometry("450x250")
ventana.resizable(0, 0)
ventana.config(bd=10)

Label(ventana, text="ENVIAR PDF VIA GMAIL", fg="black", font=("Arial", 15, "bold"), padx=5, pady=5).pack(pady=10)

# Variables
destinatario = StringVar(ventana)

Label(ventana, text="Correo destinatario:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).pack()
Entry(ventana, textvariable=destinatario, width=40).pack()

"------------ENVIO DE CORREO CON PDF------------"
def enviar_email():
    remitente = "techdata053@gmail.com"
    password = "cvec zfgp kfdh vvxt"  # Clave personal debe ser una contraseña de aplicación generada por Google
    destinatario_correo = destinatario.get()
    asunto = "Manual de Usuario - Reconocimiento de Rostros"
    mensaje = "El manual de usuario en formato PDF."

    # Crear el email
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario_correo
    email["Subject"] = asunto
    email.set_content(mensaje)

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
        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
        smtp.login(remitente, "hsunacfpeeadehlt")
        smtp.send_message(email)
        smtp.quit()
        messagebox.showinfo("MENSAJERIA", "PDF enviado correctamente")
    except Exception as e:
        messagebox.showerror("ERROR", f"No se pudo enviar el correo: {e}")

"------------BOTON------------"
Button(ventana, text="ENVIAR PDF", command=enviar_email, height=2, width=15, bg="#05365c", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

ventana.mainloop()
