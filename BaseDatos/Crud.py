import argparse
from Conexion import conexion

def guardar_empleado_en_db(usuario, Hora):
    connection = conexion()
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
            print("Conexión cerrada")

# Función principal para manejar argumentos
def main():
    # Crear un analizador de argumentos
    parser = argparse.ArgumentParser(description="Guardar información de empleado en la base de datos.")
    parser.add_argument('usuario', type=str, help="Nombre del usuario")
    parser.add_argument('Hora', type=str, help="Hora de ingreso")

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función con los argumentos recibidos
    guardar_empleado_en_db(args.usuario, args.Hora)

if __name__ == "__main__":
    main()
