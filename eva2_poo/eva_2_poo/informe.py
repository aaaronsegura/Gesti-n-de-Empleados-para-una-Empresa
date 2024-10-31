from mysql.connector import Error

class Informe:
    def __init__(self, database):
        self.db = database

    def insertar_informe(self, idInforme, tipoInforme, fechaGeneracion, idAdministrador):
        if self.db.connection is not None:  # Verificar que la conexión esté establecida
            cursor = self.db.connection.cursor()
            sql = "INSERT INTO informe (idInforme, tipoInforme, fechaGeneracion, idAdministrador) VALUES (%s, %s, %s, %s)"
            values = (idInforme, tipoInforme, fechaGeneracion, idAdministrador)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
            except Error as e:
                print(f"Error al crear informe: {e}")
            finally:
                cursor.close()  # Cerrar el cursor siempre
        else:
            print("No hay conexión a la base de datos. No se puede insertar informe.")

    def obtener_informes(self):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM informe")
            resultados = cursor.fetchall()
            cursor.close()  # Cerrar el cursor después de usarlo
            return resultados
        else:
            print("No hay conexión a la base de datos. No se pueden mostrar los informes.")
            return []

    def actualizar_informe(self, nuevo_tipo, id_informe):
        if self.db.connection is not None:  # Verificar que la conexión esté establecida
            cursor = self.db.connection.cursor()
            sql = "UPDATE informe SET tipoInforme=%s WHERE idInforme=%s"
            try:
                cursor.execute(sql, (nuevo_tipo, id_informe))
                self.db.connection.commit()
                print("El informe se ha actualizado correctamente.")
            except Error as e:
                print(f"Error al actualizar el informe: {e}")
            finally:
                cursor.close()  # Cerrar el cursor siempre
        else:
            print("Error al conectar con la base de datos.")

    def eliminar_informe(self, id_informe):
        if self.db.connection is not None:  # Verificar que la conexión esté establecida
            cursor = self.db.connection.cursor()
            sql = "DELETE FROM informe WHERE idInforme = %s"
            try:
                cursor.execute(sql, (id_informe,))
                self.db.connection.commit()
                
            except Error as e:
                print(f"Error al eliminar el informe: {e}")
            finally:
                cursor.close()  # Cerrar el cursor siempre
        else:
            print("Error al conectar con la base de datos.")
