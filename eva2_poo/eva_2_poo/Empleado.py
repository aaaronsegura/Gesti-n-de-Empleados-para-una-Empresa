import hashlib
from mysql.connector import Error

class Empleado:
    def __init__(self, database):
        self.db = database

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def insertar_empleado(self, nombre, password, direccion, telefono, email, fecha_contratacion, salario, departamento_id):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = """INSERT INTO empleado 
                     (nombre, password, direccion, telefono, email, fechaInicioContrato, salario, idDepartamento) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            password_encriptada = Empleado.hash_password(password)
            values = (nombre, password_encriptada, direccion, telefono, email, fecha_contratacion, salario, departamento_id)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
                return True, "Empleado insertado con éxito"
            except Error as e:
                return False, f"Error al insertar empleado: {e}"
            finally:
                cursor.close()
        else:
            return False, "No hay conexión a la base de datos."

    def actualizar_empleado(self, id_empleado, nombre=None, password=None, direccion=None, 
                            telefono=None, email=None, fecha_contratacion=None, 
                            salario=None, departamento_id=None):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "UPDATE empleado SET "
            values = []

            updates = {
                'nombre': nombre,
                'direccion': direccion,
                'telefono': telefono,
                'email': email,
                'fechaInicioContrato': fecha_contratacion,
                'salario': salario,
                'idDepartamento': departamento_id
            }

            if password:
                sql += "password = %s, "
                values.append(Empleado.hash_password(password))

            for field, value in updates.items():
                if value is not None:
                    sql += f"{field} = %s, "
                    values.append(value)

            if not values:
                return False, "No se proporcionaron datos para actualizar"

            sql = sql.rstrip(', ')  # Elimina la última coma
            sql += " WHERE idEmpleado = %s"
            values.append(id_empleado)

            try:
                cursor.execute(sql, tuple(values))
                self.db.connection.commit()
                if cursor.rowcount > 0:
                    return True, "Empleado actualizado con éxito"
                else:
                    return False, "No se encontró el empleado o no hubo cambios"
            except Error as e:
                return False, f"Error actualizando el empleado: {e}"
            finally:
                cursor.close()
        else:
            return False, "No hay conexión a la base de datos."

    def eliminar_empleado(self, id_empleado):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "DELETE FROM empleado WHERE idEmpleado = %s"
            try:
                cursor.execute(sql, (id_empleado,))
                self.db.connection.commit()
                if cursor.rowcount > 0:
                    return True, "Empleado eliminado con éxito"
                else:
                    return False, "No se encontró el empleado"
            except Error as e:
                return False, f"Error eliminando el empleado: {e}"
            finally:
                cursor.close()
        else:
            return False, "No hay conexión a la base de datos."

    def obtener_empleados(self):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM empleado")
            return cursor.fetchall(), "Empleados obtenidos con éxito"
        else:
            return [], "No hay conexión a la base de datos."
