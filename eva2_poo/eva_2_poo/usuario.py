class Usuario:
    def __init__(self, database):
        self.db = database

    def insertar_usuario(self, username, password):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
            values = (username, password)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
            except Exception as e:
                print(f"Error al insertar usuario: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se puede insertar usuario.")

    def obtener_usuarios(self):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM usuario")
            return cursor.fetchall()
        else:
            print("No hay conexión a la base de datos. No se pueden obtener usuarios.")
            return []

    def actualizar_usuario(self, id_usuario, nuevo_username, nuevo_password):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "UPDATE usuario SET username = %s, password = %s WHERE idUsuario = %s"
            values = (nuevo_username, nuevo_password, id_usuario)
            try:
                cursor.execute(sql, values)
                self.db.connection.commit()
                
            except Exception as e:
                print(f"Error al actualizar usuario: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se puede actualizar usuario.")

    def eliminar_usuario(self, id_usuario):
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            sql = "DELETE FROM usuario WHERE idUsuario = %s"
            try:
                cursor.execute(sql, (id_usuario,))
                self.db.connection.commit()
                print("Usuario eliminado correctamente")
            except Exception as e:
                print(f"Error al eliminar usuario: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos. No se puede eliminar usuario.")
