import os
import webbrowser

def abrir_ayuda():
    try:
        pdf_path = os.path.join(os.path.dirname(__file__), "..", "ManualPDF", "Informe - Reconocimiento facial.pdf")  # Ruta del PDF

        # Verificar si el archivo existe
        if not os.path.exists(pdf_path):
            print(f"Error: No se encontró el archivo PDF en la ruta: {pdf_path}")
            return

        # Abrir el archivo PDF con la aplicación predeterminada
        webbrowser.open(pdf_path)
    except Exception as e:
        print(f"Error al intentar abrir el archivo: {e}")

# Llamada a la función para abrir el PDF
abrir_ayuda()
