import mysql.connector 
from mysql.connector import Error


class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            # Intentar la conexión a la base de datos
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conexión a la base de datos exitosa")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None

    def close(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Conexión a la base de datos cerrada")
