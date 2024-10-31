import mysql.connector

class registro_tiempo:
    def __init__(self, database):
        self.db = database

    def insertar_registro(self, fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql ="INSERT INTO registro_tiempo (fecha, horasTrabajadas, descripcion, idEmpleado, idProyecto) VALUES (%s, %s, %s, %s, %s)"
            values = (fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
                print("Registro de tiempo realizado")
            except mysql.connector.Error as e:
                print(f"Error al registrar tiempo: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos.")

    def obtener_registros(self):    
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            try:
                cursor.execute("SELECT * FROM registro_tiempo")
                return cursor.fetchall()
            except mysql.connector.Error as e:
                print(f"Error al mostrar tiempo: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se pueden mostrar los tiempos.")
            return []

    def actualizar_tiempo(self, id_registro, fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto):

        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "UPDATE registro_tiempo SET fecha = %s, horasTrabajadas = %s, descripcion = %s, idEmpleado = %s, idProyecto = %s WHERE idRegistro = %s"
            try:
                cursor.execute(sql, (fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto, id_registro))
                self.db.connection.commit()
              
            except Exception as e:
                print(f"Error al actualizar el registro de tiempo: {e}")
        else:
            print("Error al conectar con la base de datos.")

    def eliminar_tiempo(self, id_registro):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "DELETE FROM registro_tiempo WHERE idRegistro = %s"
            try:
                cursor.execute(sql, (id_registro,))
                self.db.connection.commit()
                print("El registro de tiempo se ha eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar el registro de tiempo: {e}")
        else:
            print("Error al conectar con la base de datos.")
