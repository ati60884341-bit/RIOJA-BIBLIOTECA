import mysql.connector


class ConexionBD:

    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="bd_libros"
        )
