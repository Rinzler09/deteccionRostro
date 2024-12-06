import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importar la función crear_conexion del módulo Conexion
from deteccionRostro.Conexion.conexion import crear_conexion

def guardar_empleado_en_db(usuario=None, Hora=None):
    # Utilizar la función `crear_conexion` para obtener la conexión
    connection = crear_conexion()
    if connection is None:
        return

    try:
        if connection.is_connected():
            cursor = connection.cursor()
            # Insertar los datos del empleado
            insert_query = """
                INSERT INTO gestionUsuarios (nombre, Hora) 
                VALUES (%s, %s)
            """
            cursor.execute(insert_query, (usuario, Hora))
            connection.commit()
            print("Datos insertados correctamente en la base de datos")
    except Exception as e:
        print("Error al insertar datos:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexion cerrada")

# Llamar a la función `guardar_empleado_en_db` con los argumentos requeridos
guardar_empleado_en_db(usuario=None, Hora=None)
