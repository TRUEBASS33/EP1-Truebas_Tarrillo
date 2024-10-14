# aplicacion.py

# Función para leer el archivo de texto
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return archivo.read().strip()  # Elimina los espacios y saltos de línea
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return None

# Función para validar login y clave
def validar_login():
    login_correcto = leer_archivo('C:/Users/LENOVO/EP-Parte01/login.txt')
    clave_correcta = leer_archivo('C:/Users/LENOVO/EP-Parte01/clave.txt')

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

# Función para mostrar el menú
def mostrar_menu():
    print("\nDatos Persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

# Programa principal
if __name__ == "__main__":
    if validar_login():
        mostrar_menu()
