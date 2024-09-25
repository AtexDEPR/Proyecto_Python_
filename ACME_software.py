from DataPack.arte import bienvenido, adios,imprimir_mejor_texto
from DataPack.Login import login, cambiar_password
from DataPack import menus
from DataPack.datos import load_data

def clear_screen():
    print('\n' *  50)

data = load_data
login() 

while True:
    
    while True:
        clear_screen()
        bienvenido()
        op = menus.menu()
        match op:
            case 1:
             clear_screen()
             menus.menu_registro_grupos() #sirve correctamete
            case 2:
             clear_screen()   
             menus.menu_registro_modulos() #sirve correctamete
            case 3:
             clear_screen()   
             menus.menu_registro_estudiantes() #sirve correctamete
            case 4:
             clear_screen()   
             menus.menu_registro_docentes() #sirve correctamete
            case 5:
             clear_screen()   
             menus.menu_registro_asistencia() #sirve correctamete
            case 6:
             clear_screen()   
             menus.menu_consultas_informacion() #sirve correctamete
            case 7:
             clear_screen()   
             menus.menu_generacion_informes() #No sirve correctamente
            case 8:
             clear_screen()   
             cambiar_password()
            case 9:
             clear_screen()
             imprimir_mejor_texto('Gracias por usar el software . . .', 'amarillo', True)

             break

    break



adios()    