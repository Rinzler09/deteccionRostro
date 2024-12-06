
# Conexion.py
import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        connection = mysql.connector.connect(
            host='108.181.157.239',
            port='10001',
            database='reconocimientofacial',
            user='reconocimiento',
            password='Reconocimiento',
        )
        if connection.is_connected():
            print("Conexion exitosa a la base de datos")
            return connection
    except Error as e:
        print("Error al conectar con la base de datos:", e)
        return None

crear_conexion()