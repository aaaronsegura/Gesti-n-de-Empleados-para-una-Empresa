import hashlib


class CambiarContrasena:
    def __init__(self, database):
        self.db = database
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verificar_usuario(self, id_usuario, username, password):
        """Verifica si el ID o nombre de usuario y la contraseña coinciden con la base de datos."""
        cursor = self.db.connection.cursor()
        try:
            # Consulta para obtener la contraseña hasheada del usuario
            cursor.execute("SELECT password FROM usuario WHERE idUsuario = %s AND username = %s", (id_usuario, username))
            resultado = cursor.fetchone()
            
            if resultado:
                # Verificar el hash de la contraseña ingresada con la almacenada
                password_hash = resultado[0]
                return password_hash == self.hash_password(password)
            else:
                return False
        finally:
            cursor.close()
        
    def cambiar_contrasena(self, id_usuario, username, current_password, new_password):
        """Permite cambiar la contraseña si la contraseña actual es correcta."""
        if self.verificar_usuario(id_usuario, username, current_password):
            # Actualizar la nueva contraseña hasheada en la base de datos
            new_password_hash = self.hash_password(new_password)
            cursor = self.db.connection.cursor()
            try:
                cursor.execute("UPDATE usuario SET password = %s WHERE idUsuario = %s AND username = %s", (new_password_hash, id_usuario, username))
                self.db.connection.commit()
                return "Contraseña actualizada exitosamente."
            finally:
                cursor.close()
        else:
            return "Error: la contraseña actual no es correcta."     
        
    def cambiar_username(self, id_usuario, current_username, password, new_username):
        if self.verificar_usuario(id_usuario, current_username, password):
            cursor = self.db.connection.cursor()
            try:
                cursor.execute("UPDATE usuario SET username = %s WHERE idUsuario = %s AND username = %s",
                             (new_username, id_usuario, current_username))
                self.db.connection.commit()
                return "Username actualizado correctamente."
            finally:
                cursor.close()
        else:
            return "Error: la contraseña no es correcta."
