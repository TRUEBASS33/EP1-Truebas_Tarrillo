import os

# Clase para representar a una persona
class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.dni}\t{self.nombre}\t{self.apellido}"

# Función para leer el archivo de texto
def leer_archivo(nombre_archivo):
    ruta_archivo = os.path.join('C:/Users/LENOVO/EP-Parte01', nombre_archivo)
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read().strip()  # Elimina los espacios y saltos de línea
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return None
    except UnicodeDecodeError:
        print(f"Error: No se puede decodificar el archivo {nombre_archivo}.")
        return None

# Función para leer un archivo y devolver su contenido en una lista
def leer_archivo_en_lista(nombre_archivo):
    ruta_archivo = os.path.join('C:/Users/LENOVO/EP-Parte01', nombre_archivo)
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return [linea.strip() for linea in archivo.readlines()]  # Elimina espacios y saltos de línea
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return []
    except UnicodeDecodeError:
        print(f"Error: No se puede decodificar el archivo {nombre_archivo}.")
        return []

# Función para validar login y clave
def validar_login():
    login_correcto = leer_archivo('login.txt')
    clave_correcta = leer_archivo('clave.txt')

    if login_correcto is None or clave_correcta is None:
        print("No se pueden validar los credenciales. Archivos faltantes.")
        return False

    intentos = 0
    while intentos < 2:
        login = input("Ingrese su login: ")
        clave = input("Ingrese su clave: ")

        if login == login_correcto and clave == clave_correcta:
            return True
        else:
            print("Login o clave incorrectos. Intente nuevamente.")
            intentos += 1

    print("Se han agotado los intentos. El programa ha terminado.")
    return False

# Función para listar personas
def listar_personas():
    personas = []
    dni_list = leer_archivo_en_lista('dni.txt')
    nombre_list = leer_archivo_en_lista('nombre.txt')
    apellido_list = leer_archivo_en_lista('apellido.txt')

    print("\nListado de Personas:")
    print("DNI\t\tNombre\t\tApellido")
    print("-" * 40)

    # Asegurando que las listas tengan la misma longitud
    for dni, nombre, apellido in zip(dni_list, nombre_list, apellido_list):
        persona = Persona(dni, nombre, apellido)
        personas.append(persona)
        print(f"{persona.dni:<12}{persona.nombre:<15}{persona.apellido:<15}")

    print("\n")  # Línea en blanco para mayor claridad

# Función para agregar personas
def agregar_personas():
    dni = input("Ingrese el DNI de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")

    with open('C:/Users/LENOVO/EP-Parte01/dni.txt', 'a', encoding='utf-8') as dni_file, \
         open('C:/Users/LENOVO/EP-Parte01/nombre.txt', 'a', encoding='utf-8') as nombre_file, \
         open('C:/Users/LENOVO/EP-Parte01/apellido.txt', 'a', encoding='utf-8') as apellido_file:
        dni_file.write(dni + '\n')
        nombre_file.write(nombre + '\n')
        apellido_file.write(apellido + '\n')

    print("Persona agregada correctamente.\n")

# Función para mostrar el menú
def mostrar_menu():
    while True:
        print("Datos Persona")
        print("1. Listar personas")
        print("2. Agregar personas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_personas()
        elif opcion == '2':
            agregar_personas()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Programa principal
if __name__ == "__main__":
    if validar_login():
        mostrar_menu()
