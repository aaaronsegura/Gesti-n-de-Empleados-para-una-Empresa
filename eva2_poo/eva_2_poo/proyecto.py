import mysql.connector

class Proyecto:
    def __init__(self, database):
        self.db = database

    def insertar_proyecto(self, nombre, descripcion, fecha_inicio, fecha_termino):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "INSERT INTO proyecto (nombre, descripcion, fechaInicio, fechaTermino) VALUES (%s, %s, %s, %s)"
            values = (nombre, descripcion, fecha_inicio, fecha_termino)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
            except mysql.connector.Error as e:
                print(f"Error al registrar el proyecto: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos.")

    def obtener_proyectos(self):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            try:
                cursor.execute("SELECT * FROM proyecto")
                return cursor.fetchall()
            except mysql.connector.Error as e:
                print(f"Error al obtener proyectos: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se pueden obtener proyectos.")
            return []

    def actualizar_proyecto(self, id_proyecto, nuevo_nombre, nueva_descripcion, nueva_fecha_termino):
        if self.db.connection is not None:  # Verificar que la conexión esté establecida
            cursor = self.db.connection.cursor()
            sql = "UPDATE proyecto SET nombre = %s, descripcion = %s, fechaTermino = %s WHERE idProyecto = %s"
            values = (nuevo_nombre, nueva_descripcion, nueva_fecha_termino, id_proyecto)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
                if cursor.rowcount > 0:
                    print("El proyecto se ha actualizado correctamente.")
                else:
                    print("No se encontró el proyecto o no hubo cambios.")
            except mysql.connector.Error as e:
                print(f"Error al actualizar el proyecto: {e}")
        else:
            print("Error al conectar con la base de datos.")

    def eliminar_proyecto(self, id_proyecto):
        if self.db.connection is not None:  # Verificar que la conexión esté establecida
            cursor = self.db.connection.cursor()
            sql = "DELETE FROM proyecto WHERE idProyecto = %s"
            try:
                cursor.execute(sql, (id_proyecto,))
                self.db.connection.commit()
                if cursor.rowcount > 0:
                    print("El proyecto se ha eliminado correctamente.")
                else:
                    print("No se encontró el proyecto especificado.")
            except mysql.connector.Error as e:
                print(f"Error al eliminar el proyecto: {e}")
            finally:
                cursor.close()
        else:
            print("Error al conectar con la base de datos.")
