class Administrador:
    def __init__(self, database):
        self.db = database

    def insertar_administrador(self, nombre, permisos, email):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = """
                INSERT INTO administrador (nombre, permisos, email) 
                VALUES (%s, %s, %s)
            """
            values = (nombre, permisos, email)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
                print("Administrador insertado exitosamente.")
            except Exception as e:
                print(f"Error al insertar administrador: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se puede insertar administrador.")

    def obtener_administradores(self):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM administrador")
            return cursor.fetchall()
        else:
            print("No hay conexión a la base de datos. No se pueden obtener administradores.")
            return []

    def actualizar_administrador(self, id_admin, nuevo_nombre, nuevo_email, nuevos_permisos):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = """
                UPDATE administrador 
                SET nombre = %s, email = %s, permisos = %s 
                WHERE idAdministrador = %s
            """
            values = (nuevo_nombre, nuevo_email, nuevos_permisos, id_admin)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
                print("Administrador actualizado correctamente.")
            except Exception as e:
                print(f"Error al actualizar administrador: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se puede actualizar administrador.")

    def eliminar_administrador(self, id_admin):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "DELETE FROM administrador WHERE idAdministrador = %s"
            try:
                cursor.execute(sql, (id_admin,))
                self.db.connection.commit()
                print("Administrador eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar administrador: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se puede eliminar administrador.")
