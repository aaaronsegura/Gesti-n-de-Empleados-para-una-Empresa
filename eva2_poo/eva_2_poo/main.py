# Importación de módulos necesarios
import mysql.connector
import pwinput
from datetime import datetime
from cursor import Database
from usuario import Usuario
from administrador import Administrador
from Empleado import Empleado
from Departamento import Departamento
from informe import Informe
from proyecto import Proyecto
from registro_tiempo import registro_tiempo
from Autenticar_empleado import EmpleadoAutenticacion
from Cambiarcontrasena import CambiarContrasena

# Conexión a la base de datos MySQL
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="",           
        database="gestion_final"
    )

# Función para validar texto
def validar_texto(texto):
    return texto.isalpha()

# Función para validar números
def validar_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

# Función para validar fecha en formato YYYY-MM-DD
def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Función para insertar resultado en la base de datos
def guardar_validacion(tipo, valor, es_valido, id_empleado):
    conexion = conectar_db()
    cursor = conexion.cursor()

    query = """
        INSERT INTO ValidacionEntrada (tipoValidacion, valorIngresado, esValido, idEmpleado) 
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (tipo, valor, es_valido, id_empleado))
    conexion.commit()

    print(f"Validación de {tipo} guardada exitosamente.")
    cursor.close()
    conexion.close()

# Función principal para manejar la validación
def validar_entrada(tipo, valor, id_empleado):
    if tipo == 'Texto':
        es_valido = validar_texto(valor)
    elif tipo == 'Número':
        es_valido = validar_numero(valor)
    elif tipo == 'Fecha':
        es_valido = validar_fecha(valor)
    else:
        print("Tipo de validación no soportado.")
        return

    # Guardar el resultado de la validación en la base de datos
    guardar_validacion(tipo, valor, es_valido, id_empleado)

# Función principal del programa
def main():
    # Conectar a la base de datos
    db = Database(host="localhost", database="gestion_final", user="root", password="")
    db.connect()
    
    # Crear una instancia de EmpleadoAutenticacion
    autenticacion_instancia = EmpleadoAutenticacion(db)
    
    # Menú para seleccionar entre Usuario, Administrador, etc.
    while True:
        print("\nSeleccione una opción:")
        print("1. Autenticación de Empleado")
        print("2. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            print("\nAutenticación de Empleado:")
            email = input("Ingrese el email del empleado: ")
            password = input("Ingrese la contraseña: ")
            empleado = autenticacion_instancia.autenticar_empleado(email, password)
            
            if empleado:
                print(f"Bienvenido, {empleado[1]}!")  
                rol = empleado[2]

                # Menú según el rol
                if rol == 'Administrador':
                    mostrar_menu_administrador(db)
                elif rol == 'Empleado':
                    mostrar_menu_empleado(db)
                else:
                    print("Rol no reconocido.")
            else:
                print("Credenciales incorrectas.")

        elif opcion == "2":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Funciones para el menú de administrador y empleado
def mostrar_menu_administrador(db):
    while True:
        print("\nSeleccione una opción (Administrador):")
        print("1. Usuario")
        print("2. Administrador")
        print("3. Empleado")
        print("4. Departamento")
        print("5. Informe")
        print("6. Proyecto")
        print("7. Registro de Tiempo")
        print("8. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            gestionar_usuario(db)
        elif opcion == "2":
            gestionar_administrador(db)
        elif opcion == "3":
            gestionar_empleado(db)
        elif opcion == "4":
            gestionar_departamento(db)
        elif opcion == "5":
            gestionar_informe(db)
        elif opcion == "6":
            gestionar_proyecto(db)
        elif opcion == "7":
            gestionar_registro_tiempo(db)
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
# menú   empleado
def mostrar_menu_empleado(db):
    insertar_registro = registro_tiempo(db)
    
    while True:
        print("\nSeleccione una opción (Empleado):")
        print("1. Registrar tiempo trabajado")
        print("2. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_tiempo_trabajado(insertar_registro)
        elif opcion == "2":
            print("Saliendo del menú de empleado...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_tiempo_trabajado(registro_tiempo_instancia):
    # Solicitar los datos necesarios para el registro de tiempo
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    while not validar_fecha(fecha):
        print("Fecha no válida. Intente de nuevo.")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

    horas_trabajadas = input("Ingrese la cantidad de horas trabajadas: ")
    while not validar_numero(horas_trabajadas):
        print("Número no válido. Intente de nuevo.")
        horas_trabajadas = input("Ingrese la cantidad de horas trabajadas: ")

    descripcion = input("Ingrese una breve descripción de las tareas realizadas: ")
    while not descripcion:
        print("Descripción no puede estar vacía. Intente de nuevo.")
        descripcion = input("Ingrese una breve descripción de las tareas realizadas: ")

    id_empleado = int(input("Ingrese su ID de empleado: "))
    id_proyecto = int(input("Ingrese el ID del proyecto al que pertenece este trabajo: "))

    # Llamada a la función para registrar el tiempo en la base de datos
    registro_tiempo_instancia.insertar_registro( fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto)
    print("Registro de tiempo guardado exitosamente.")

# Funciones CRUD para cada entidad
def gestionar_usuario(db):
    usuario_instancia = Usuario(db) 
    print("\nOperaciones CRUD para Usuario:")
    print("1. Insertar")
    print("2. Ver todos")
    print("3. actualizar datos")
    print("4. Eliminar")
    opcion = input("Opción: ")

    if opcion == "1":
        username = input("Ingrese el nombre de usuario: ")
        password = pwinput.pwinput(prompt="Ingrese la contraseña: ")
        usuario_instancia.insertar_usuario(username, password)
        print("Usuario insertado exitosamente.")
    elif opcion == "2":
        usuarios = usuario_instancia.obtener_usuarios()
        for usr in usuarios:
            print(f"ID: {usr[0]}, Username: {usr[1]}")
    elif opcion == "3":
        cambiascontraseña_instancia = CambiarContrasena(db)
        id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
        username = input("Ingrese el nombre de usuario: ")
        while True:
            current_password = pwinput.pwinput(prompt="Ingrese su contraseña actual: ")
            if cambiascontraseña_instancia.verificar_usuario(id_usuario, username, current_password):
                new_username = input ("Ingrese el nuevo username: ")
                new_password = pwinput.pwinput(prompt="Ingrese su nueva contraseña: ")
                resultado = cambiascontraseña_instancia.cambiar_contrasena(id_usuario, username, current_password, new_password)
                print(resultado)
                resultado2 = cambiascontraseña_instancia.cambiar_username(id_usuario, username, current_password, new_username)
                print(resultado2)
                break
            else:
                print("Contraseña incorrecta")
        
    elif opcion == "4":
        id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
        usuario_instancia.eliminar_usuario(id_usuario)
        print("Usuario eliminado exitosamente.")
    else:
        print("Opción no válida.")

def gestionar_administrador(db):
    admin_instancia = Administrador(db)
    print("\nOperaciones CRUD para Administrador:")
    print("1. Insertar")
    print("2. Ver todos")
    print("3. Actualizar")
    print("4. Eliminar")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del administrador: ")
        permisos = input("Ingrese los permisos del administrador: ")
        email = input("Ingrese el email del administrador: ")
        admin_instancia.insertar_administrador(nombre, permisos, email)

    elif opcion == "2":
        administradores = admin_instancia.obtener_administradores()
        for adm in administradores:
            print(f"ID: {adm[0]}, Nombre: {adm[1]}, Permisos: {adm[2]}, Email: {adm[3]}")

    elif opcion == "3":
        id_admin = int(input("Ingrese el ID del administrador a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_email = input("Ingrese el nuevo email: ")
        nuevos_permisos = input("Ingrese los nuevos permisos: ")
        admin_instancia.actualizar_administrador(id_admin, nuevo_nombre, nuevo_email, nuevos_permisos)

    elif opcion == "4":
        id_admin = int(input("Ingrese el ID del administrador a eliminar: "))
        admin_instancia.eliminar_administrador(id_admin)

    else:
        print("Opción no válida.") 
def gestionar_empleado(db):
    empleado_instancia = Empleado(db)
    print("\nOperaciones CRUD para Empleado:")
    print("1. Insertar")
    print("2. Ver todos")
    print("3. Actualizar")
    print("4. Eliminar")
    opcion_empleado = input("Opción: ")

    if opcion_empleado == "1":
        nombre = input("Ingrese el nombre del empleado: ")
        password = pwinput.pwinput(prompt="Ingrese la contraseña: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")
        email = input("Ingrese el email: ")
        fecha_contratacion = input("Ingrese la fecha de contratación (YYYY-MM-DD): ")
        salario = float(input("Ingrese el salario: "))
        departamento_id = int(input("Ingrese el ID del departamento: "))
        empleado_instancia.insertar_empleado(
            nombre, password, direccion, telefono, email,
            fecha_contratacion, salario, departamento_id
        )
        print("Empleado insertado exitosamente.")

    elif opcion_empleado == "2":
        empleados = empleado_instancia.obtener_empleados()
        for emp in empleados:
            print(f"ID: {emp[0]}, Nombre: {emp[1]}, Email: {emp[4]}")

    elif opcion_empleado == "3":
        id_empleado = int(input("Ingrese el ID del empleado a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre del empleado: ")
        nuevo_email = input("Ingrese el nuevo email del empleado: ")

        # Preguntar si se desea cambiar la contraseña
        cambiar_password = input("¿Desea cambiar la contraseña? (s/n): ").lower()
        if cambiar_password == 's':
            username = input("Ingrese el username del empleado: ")
            while True:
                current_password = pwinput.pwinput(prompt="Ingrese su contraseña actual: ")
                if CambiarContrasena.verificar_usuario(id_empleado, username, current_password):
                    new_password = pwinput.pwinput(prompt="Ingrese su nueva contraseña: ")
                    CambiarContrasena.cambiar_contrasena(id_empleado, username, current_password, new_password)
                    print("Contraseña actualizada exitosamente.")
                    break
                else:
                    print("Contraseña incorrecta. Intente nuevamente.")
        else:
            print("La contraseña no fue cambiada.")

        empleado_instancia.actualizar_empleado(id_empleado, nuevo_nombre, nuevo_email)
        print("Empleado actualizado exitosamente.")

    elif opcion_empleado == "4":
        id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))
        empleado_instancia.eliminar_empleado(id_empleado)
        print("Empleado eliminado exitosamente.")

    else:
        print("Opción no válida.")


  
def gestionar_departamento(db):
    departamento_instancia = Departamento(db)
    print("\nOperaciones CRUD para Departamento:")
    print("1. Insertar")
    print("2. Ver todos")
    print("3. Actualizar")
    print("4. Eliminar")
    opcion_departamento = input("Opción: ")

    if opcion_departamento == "1":
        nombre = input("Ingrese el nombre del departamento: ")
        gerente = input("Ingrese el nombre del gerente: ")
        id_departamento = input("Ingrese el ID del departamento: ")

        # Validación del ID
        if not id_departamento.isdigit():
            print("ID del departamento inválido. Debe ser un número.")
            return  # Cancelar la operación si el ID es inválido

        id_departamento = int(id_departamento)
        departamento_instancia.insertar_departamento(nombre, gerente, id_departamento)
        print("Departamento insertado exitosamente.")

    elif opcion_departamento == "2":
        departamentos = departamento_instancia.obtener_departamento()
        for dept in departamentos:
            print(f"ID: {dept[0]}, Nombre: {dept[1]}, Gerente: {dept[2]}")

    elif opcion_departamento == "3":
        id_departamento = int(input("Ingrese el ID del departamento a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre del departamento: ")
        nuevo_gerente = input("Ingrese el nuevo gerente: ")
        departamento_instancia.actualizar_departamento(id_departamento, nuevo_nombre, nuevo_gerente)
        print("Departamento actualizado exitosamente.")

    elif opcion_departamento == "4":
        id_departamento = int(input("Ingrese el ID del departamento a eliminar: "))
        departamento_instancia.eliminar_departamento(id_departamento)
        print("Departamento eliminado exitosamente.")

    else:
        print("Opción inválida. Por favor, elija una opción válida.")


def gestionar_informe(db):
    informe_instancia = Informe(db)
    print("\nOperaciones CRUD para Informe:")
    print("1. Insertar")
    print("2. Ver todos")
    print("3. Actualizar")
    print("4. Eliminar")
    opcion_informe = input("Opción: ")

    if opcion_informe == "1":
        id_informe = int(input("Ingrese el ID del informe: "))
        tipo_informe = input("Ingrese el tipo de informe: ")
        fecha_generacion = input("Ingrese la fecha de generación (YYYY-MM-DD): ")
        id_administrador = int(input("Ingrese el ID del administrador: "))
        informe_instancia.insertar_informe(id_informe, tipo_informe, fecha_generacion, id_administrador)
        print("Informe insertado exitosamente.")
    elif opcion_informe == "2":
        informes = informe_instancia.obtener_informes()
        for inf in informes:
            print(f"ID Informe: {inf[0]}, Tipo: {inf[1]}, Fecha: {inf[2]}")
    elif opcion_informe == "3":
        id_informe = int(input("Ingrese el ID del informe a actualizar: "))
        nuevo_tipo = input("Ingrese el nuevo tipo de informe: ")
        informe_instancia.actualizar_informe(id_informe, nuevo_tipo)
        print("Informe actualizado exitosamente.")
    elif opcion_informe == "4":
        id_informe = int(input("Ingrese el ID del informe a eliminar: "))
        informe_instancia.eliminar_informe(id_informe)
        print("Informe eliminado exitosamente.")

from datetime import datetime

def gestionar_proyecto(db):
    proyecto_instancia = Proyecto(db)
    print("\nOperaciones CRUD para Proyecto:")
    print("1. Insertar")
    print("2. Ver todos")
    print("3. Actualizar")
    print("4. Eliminar")
    opcion_proyecto = input("Opción: ")

    if opcion_proyecto == "1":
        nombre = input("Ingrese el nombre del proyecto: ")
        descripcion = input("Ingrese la descripción del proyecto: ")
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_termino = input("Ingrese la fecha de fin (YYYY-MM-DD): ")

        # Validación de fechas
        try:
            # Verificar el formato de la fecha
            fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_termino_dt = datetime.strptime(fecha_termino, "%Y-%m-%d")
            if fecha_inicio_dt > fecha_termino_dt:
                print("La fecha de inicio debe ser anterior a la fecha de término.")
                return
        except ValueError:
            print("Formato de fecha inválido. Asegúrese de usar el formato YYYY-MM-DD.")
            return

        proyecto_instancia.insertar_proyecto(nombre, descripcion, fecha_inicio, fecha_termino)
        print("Proyecto insertado exitosamente.")

    elif opcion_proyecto == "2":
        proyectos = proyecto_instancia.obtener_proyectos()
        for proj in proyectos:
            print(f"ID Proyecto: {proj[0]}, Nombre: {proj[1]}, Descripción: {proj[2]}, Fecha Inicio: {proj[3]}, Fecha Término: {proj[4]}")

    elif opcion_proyecto == "3":
        id_proyecto = int(input("Ingrese el ID del proyecto a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre del proyecto: ")
        nueva_descripcion = input("Ingrese la nueva descripción del proyecto: ")
        nueva_fecha_termino = input("Ingrese la nueva fecha de término (YYYY-MM-DD): ")

        # Validación de la nueva fecha de término
        try:
            nueva_fecha_termino_dt = datetime.strptime(nueva_fecha_termino, "%Y-%m-%d")
            if fecha_inicio_dt > nueva_fecha_termino_dt:
                print("La nueva fecha de término debe ser posterior a la fecha de inicio.")
                return
        except ValueError:
            print("Formato de fecha inválido. Asegúrese de usar el formato YYYY-MM-DD.")
            return

        proyecto_instancia.actualizar_proyecto(id_proyecto, nuevo_nombre, nueva_descripcion, nueva_fecha_termino)
        print("Proyecto actualizado exitosamente.")

    elif opcion_proyecto == "4":
        id_proyecto = int(input("Ingrese el ID del proyecto a eliminar: "))
        proyecto_instancia.eliminar_proyecto(id_proyecto)
        print("Proyecto eliminado exitosamente.")

    else:
        print("Opción inválida. Por favor, elija una opción válida.")

def gestionar_registro_tiempo(db):
    registro_tiempo_instancia = registro_tiempo(db)
    print("\nOperaciones CRUD para Registro de Tiempo:")
    print("1. Insertar")
    print("2. Ver todos")
    print("3. Actualizar")
    print("4. Eliminar")
    opcion_registro = input("Opción: ")

    if opcion_registro == "1":
        id_empleado = int(input("Ingrese el ID del empleado: "))
        id_proyecto = int(input("Ingrese el ID del proyecto: "))
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        descripcion = input("Ingrese una descripción del trabajo: ")
        registro_tiempo_instancia.insertar_registro(fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto)
        print("Registro de tiempo insertado exitosamente.")
    elif opcion_registro == "2":
        registros = registro_tiempo_instancia.obtener_registros()
        for reg in registros:
            print(f"ID Registro: {reg[0]}, ID Empleado: {reg[1]}, ID Proyecto: {reg[2]}, Horas: {reg[3]}")
    elif opcion_registro == "3":
        id_registro = int(input("Ingrese el ID del registro a actualizar: "))
        fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
        nuevas_horas = float(input("Ingrese las nuevas horas trabajadas: "))
        descripcion = input("Ingrese la nueva descripción: ")
        id_empleado = int(input("Ingrese el nuevo ID del empleado: "))
        id_proyecto = int(input("Ingrese el nuevo ID del proyecto: "))
        
        # Llama al método correctamente con todos los parámetros
        registro_tiempo_instancia.actualizar_tiempo(id_registro, fecha, nuevas_horas, descripcion, id_empleado, id_proyecto)
        print("Registro actualizado exitosamente.")
    elif opcion_registro == "4":
        id_registro = int(input("Ingrese el ID del registro a eliminar: "))
        registro_tiempo_instancia.eliminar_tiempo(id_registro)  # Llama al método correcto
        print("Registro eliminado exitosamente.")
    else:
        print("Opción inválida.")



if __name__ == "__main__":
    main()
