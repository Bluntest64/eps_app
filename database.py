import mysql.connector
from mysql.connector import Error
from config import Config

def get_connection():
    try:
        print("HOST:", Config.MYSQL_HOST)
        print("USER:", Config.MYSQL_USER)
        print("DB:", Config.MYSQL_DB)
        print("PORT:", Config.MYSQL_PORT)

        conexion = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT
        )
        if conexion.is_connected():
            print("Conexión a MySQL exitosa")
            return conexion
    except Error as e:
        # Aquí imprimimos el error para que Railway lo muestre en el Deploy Log
        print(f"Error al conectar con MySQL: {e}")
        # Lanza una excepción para que Flask sepa que falló la conexión
        raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")