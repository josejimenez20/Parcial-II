import mysql.connector

config = {
    'user': 'root',            # Reemplaza con tu usuario de MySQL
    'password': '', # Reemplaza con tu contraseña de MySQL
    'host': 'localhost',
    'database': 'db_academica'
}

def registrar_usuario(usuario, clave, nombre, direccion, telefono):
    conexion = None
    cursor = None
    try:
      
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        query = '''
            INSERT INTO Usuarios (usuario, clave, nombre, direccion, telefono)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (usuario, clave, nombre, direccion, telefono))
        conexion.commit()

        print("Usuario registrado con éxito.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# Función para recoger los datos del usuario desde la consola
def pedir_datos_usuario():
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese la clave: ")
    nombre = input("Ingrese el nombre completo: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")

    return usuario, clave, nombre, direccion, telefono

# Ejecución del registro de usuario
if __name__ == '__main__':
    usuario, clave, nombre, direccion, telefono = pedir_datos_usuario()
    registrar_usuario(usuario, clave, nombre, direccion, telefono)
