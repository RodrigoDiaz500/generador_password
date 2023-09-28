import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password

while True:
    try:
        length = int(input("Ingresa la longitud deseada de la contraseña: "))
        if length < 1:
            print("La longitud debe ser mayor o igual a 1.")
        else:
            password = generate_password(length)
            print("Contraseña generada:", password)
            break  # Rompe el bucle cuando se genera una contraseña válida
    except ValueError:
        print("Debes ingresar un número entero válido para la longitud.")