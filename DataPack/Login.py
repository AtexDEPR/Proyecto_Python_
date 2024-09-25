import hashlib
import json
import os

# Archivo donde se guardarán los usuarios y contraseñas
USERS_FILE = 'Json/users.json'

# Función para inicializar el archivo de usuarios si no existe
def first_attempt():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

# Función para guardar usuarios en el archivo JSON
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file)

# Función para encriptar contraseñas con SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#esta es la función principal para manejar el inicio de sesión, se pide el ususario y la contrasena
def login():
    user_data = first_attempt()
    
    while True:
        username = input('Ingrese su nombre de usuario: ')
        
        # Si es la primera vez que se ejecuta, se establece una contraseña por defecto
        if not user_data:
            user_data[username] = hash_password("SISGESA")
            save_users(user_data)
            print("Usuario creado con la contraseña predeterminada 'SISGESA'.")
            break
        
        password = input('Ingrese su contraseña: ')
        hashed_password = hash_password(password)

        if username in user_data and user_data[username] == hashed_password:
            print("Inicio de sesión exitoso.\n")
            break
        else:
            print("Error. Nombre de usuario o contraseña incorrectos.\n")
            continue
        



#esta función es para cambiar la contraseña del usuario
def cambiar_password(user_data, username):
    while True:
        old_password = input('Ingrese su contraseña actual: ')
        hashed_old_password = hash_password(old_password)
        if user_data[username] == hashed_old_password:
            new_password = input('Ingrese su nueva contraseña: ')
            confirm_password = input('Confirme su nueva contraseña: ')
            if new_password == confirm_password:
                user_data[username] = hash_password(new_password)
                save_users(user_data)
                print('Contraseña cambiada con éxito.\n')
                return
            else:
                print('Error: Las contraseñas no coinciden. Inténtelo de nuevo.\n')
        else:
            print('Error: Contraseña actual incorrecta. Inténtelo de nuevo.\n')
            