import hashlib

class EmpleadoAutenticacion:
    def __init__(self, database):
        self.db = database

    @staticmethod
    def _hash_password(password):
        """Genera un hash SHA-256 de la contraseña proporcionada."""
        return hashlib.sha256(password.encode()).hexdigest()

    def autenticar_empleado(self, email, password):
        """Autentica al empleado verificando el email y la contraseña hasheada."""
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            try:
                # Consulta el empleado por email
                cursor.execute("SELECT idEmpleado, nombre, password, idRol FROM empleado WHERE email = %s", (email,))
                resultado = cursor.fetchone()
                
                if resultado:
                    password_encriptada = resultado[2]
                    password_ingresada_encriptada = self._hash_password(password.strip())  # Limpiar contraseña
                    
                    # Verifica si la contraseña es correcta
                    if password_ingresada_encriptada == password_encriptada:
                        # Obtiene el rol del empleado autenticado
                        rol = self.obtener_rol_del_empleado(email)
                        print(f"Rol del empleado autenticado: {rol}")
                        
                        # Retorna el resultado incluyendo el rol
                        return resultado[0], resultado[1], rol
                    else:
                        print("Contraseña incorrecta.")
                        return False
                else:
                    print("El email no está registrado.")
                    return False
            except Exception as e:
                print(f"Error al autenticar empleado: {e}")
                return False
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos.")
            return False

    def obtener_rol_del_empleado(self, email):
        """Obtiene el rol del empleado basándose en su email."""
        if self.db.connection is not None:
            cursor = self.db.connection.cursor()
            try:
                consulta = """
                SELECT rol.nombreRol 
                FROM empleado
                JOIN rol ON empleado.idRol = rol.idRol
                WHERE empleado.email = %s
                """
                cursor.execute(consulta, (email,))
                resultado = cursor.fetchone()
                
                if resultado:
                    return resultado[0]  # Retorna el nombre del rol
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener el rol del empleado: {e}")
                return None
            finally:
                cursor.close()
