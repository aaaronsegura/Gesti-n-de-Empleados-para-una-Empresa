from mysql.connector import Error

class Departamento:
    def __init__(self, database):
        self.db = database

    def insertar_departamento(self, nombre, gerente, id_departamento):
        if not self.db.connection:
            print("No hay conexión a la base de datos.")
            return False  # Devolver falso si no hay conexión

        cursor = self.db.connection.cursor()
        sql = "INSERT INTO departamento (nombre, gerente, id_departamento) VALUES (%s, %s, %s)"
        values = (nombre, gerente, id_departamento)

        try:
            cursor.execute(sql, values)
            self.db.connection.commit()
            return True  # Devolver True si la inserción fue exitosa
        except Error as e:
            print(f"Error al registrar departamento: {e}")
            return False  # Devolver False si hubo un error
        finally:
            cursor.close()

    def actualizar_departamento(self, id_departamento, nombre=None, gerente=None):
        if not self.db.connection:
            print("No hay conexión a la base de datos.")
            return False

        cursor = self.db.connection.cursor()
        sql = "UPDATE departamento SET "
        values = []

        if nombre:
            sql += "nombre = %s, "
            values.append(nombre)
        if gerente:
            sql += "gerente = %s, "
            values.append(gerente)

        if not values:
            print("No se proporcionaron datos para actualizar")
            return False

        sql = sql.rstrip(', ') + " WHERE id_departamento = %s"
        values.append(id_departamento)

        try:
            cursor.execute(sql, tuple(values))
            self.db.connection.commit()
            return cursor.rowcount > 0  # Devuelve True si se actualizó
        except Error as e:
            print(f"Error actualizando el departamento: {e}")
            return False
        finally:
            cursor.close()

    def eliminar_departamento(self, id_departamento):
        if not self.db.connection:
            print("No hay conexión a la base de datos.")
            return False

        cursor = self.db.connection.cursor()
        sql = "DELETE FROM departamento WHERE id_departamento = %s"

        try:
            cursor.execute(sql, (id_departamento,))
            self.db.connection.commit()
            return cursor.rowcount > 0  # Devuelve True si se eliminó
        except Error as e:
            print(f"Error eliminando el departamento: {e}")
            return False
        finally:
            cursor.close()

    def obtener_departamento(self):
        if not self.db.connection:
            print("No hay conexión a la base de datos. No se puede obtener departamento.")
            return []

        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM departamento")
        return cursor.fetchall()
