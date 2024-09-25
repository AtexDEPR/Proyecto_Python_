from DataPack import datos
from DataPack import arte # Importa el módulo `arte` para las impresiones visuales.

def menu():
    while True:
        print('')
        arte.imprimir_mejor_texto("--------------------------------------------+", "cyan", True)
        arte.imprimir_mejor_texto("** MENU PRINCIPAL **                        |", "cyan", True)
        arte.imprimir_mejor_texto("                                            |", "cyan", True)
        arte.imprimir_mejor_texto("1) Registro de grupos                       |", "cyan", True)
        arte.imprimir_mejor_texto("2) Registro de módulos                      |", "cyan", True)
        arte.imprimir_mejor_texto("3) Registro de estudiantes                  |", "cyan", True)
        arte.imprimir_mejor_texto("4) Registro de docentes                     |", "cyan", True)
        arte.imprimir_mejor_texto("5) Registro de asistencia                   |", "cyan", True)
        arte.imprimir_mejor_texto("6) Consultas de información                 |", "cyan", True)
        arte.imprimir_mejor_texto("7) Generación de informes                   |", "cyan", True)
        arte.imprimir_mejor_texto("8) Cambio de contraseña                     |", "cyan", True)
        arte.imprimir_mejor_texto("9) Salir del sistema...                     |", "cyan", True)
        arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu          |", "cyan", True)
        arte.imprimir_mejor_texto("--------------------------------------------+", "cyan", True)
        arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

        
        try:
            opcion = int(input("")) # Solicita al usuario que ingrese una opción.
            massage =  "Cargando..."
            duration = 3
            arte.data_processing_animation(massage,  duration) # Muestra una animación de procesamiento.
            if opcion <1 or opcion > 9:
                print("Error. Opcion no valida.") # Mensaje de error si la opción no es válida.
                input("presione cualquier tecla para volver al menu ...")
                continue # Vuelve al inicio del menú.
            return opcion # Retorna la opción válida.
        except ValueError:
            print("Error. Opcion no valida.") # Mensaje de error si la entrada no es un número válido.
            input("presione cualquier tecla para volver al menu ...")
            
def menu_registro_grupos():
    arte.grupos()
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto("Registro de grupos                          |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto("1) Registrar un nuevo grupo                 |", "blanco", True)
    arte.imprimir_mejor_texto("2) Salir                                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu          |", "blanco", True)
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

    opcion = int(input(""))
    data = datos.load_data() # Carga los datos existentes.
    massage =  "Cargando..."
    duration = 3
    arte.data_processing_animation(massage,  duration)
    try:
        if opcion == 1:
            print('')
            datos.registrar_grupo(data) # Registra un nuevo grupo.
            print('')
            return menu_registro_grupos() # Vuelve al submenú de registro de grupos.
        if  opcion == 2:
            return opcion
        if opcion < 1 or opcion > 2:
            print("Error. Opcion no valida.")
            input("presione cualquier tecla para volver al menu ...")
            return menu_registro_grupos()
        return opcion # Vuelve al menú principal.
    except ValueError:
        print("Error. Opcion no valida.")
        input("presione cualquier tecla para volver al menu ...")
        return menu_registro_grupos()
    
    


def menu_registro_modulos():
    print('')
    arte.modulos()
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto("registro de modulos                         |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto("1) Registrar un nuevo modulo                |", "blanco", True)
    arte.imprimir_mejor_texto("2) Salir                                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu          |", "blanco", True)
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

    opcion = int(input(""))
    data = datos.load_data()

    massage =  "Cargando..."
    duration = 3
    arte.data_processing_animation(massage,  duration)
    try:
        if opcion == 1:
            print('')
            datos.registrar_modulo(data) # Registra un nuevo módulo.
            print('')
            return menu_registro_modulos()
        if opcion == 2:
            return opcion
        if opcion < 1 or opcion > 2:
            print("Error. Opcion no valida.")
            input("presione cualquier tecla para volver al menu ...")
            return menu_registro_modulos()
        return opcion
    except ValueError:
        print("Error. Opcion no valida.")
        input("presione cualquier tecla para volver al menu ...")
        return menu_registro_modulos()
    

    
def menu_registro_estudiantes():
    print('')
    arte.estudiantes()
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(" Registro de estudiantes                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto("1) Registrar un nuevo estudiante            |", "blanco", True)
    arte.imprimir_mejor_texto("2) Salir                                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu          |", "blanco", True)
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

    
    opcion = int(input(""))
    data = datos.load_data()
    
    massage =  "Cargando..."
    duration = 3
    arte.data_processing_animation(massage,  duration)
    try:
        if opcion == 1:
            print('')
            datos.registrar_estudiante(data) # Registra un nuevo estudiante.
            print('')
            return menu_registro_estudiantes()
        if opcion == 2:
            return opcion
        if opcion < 1 or opcion > 2:
            print("Error. Opcion no valida.")
            input("presione cualquier tecla para volver al menu ...")
            return menu_registro_estudiantes()
        return opcion
    except ValueError:
        print("Error. Opcion no valida.")
        input("presione cualquier tecla para volver al menu ...")
        return menu_registro_estudiantes()
    

    
def menu_registro_docentes():
    print('')
    arte.docentes()
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(" Registro de docentes                       |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto("1) Registrar un nuevo docente               |", "blanco", True)
    arte.imprimir_mejor_texto("2) Salir                                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu          |", "blanco", True)
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    
    arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

    opcion = int(input(""))
    data = datos.load_data()

    massage =  "Cargando..."
    duration = 3
    arte.data_processing_animation(massage,  duration)
    try:
        if opcion == 1:
            print('')
            datos.registrar_docente(data) # Registra un nuevo docente.
            print('')
            return menu_registro_docentes()
        if opcion == 2:
            return opcion
        if opcion < 1 or opcion > 2:
            print("Error. Opcion no valida.")
            input("presione cualquier tecla para volver al menu ...")
            return menu_registro_docentes()
        return opcion
    except ValueError:
        print("Error. Opcion no valida.")
        input("presione cualquier tecla para volver al menu ...")
        return menu_registro_docentes()
    
    
def menu_registro_asistencia():
    print('')
    arte.asistencia()
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(" Registro de asistencias                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto("1) Registrar asistencia de un estudiante    |", "blanco", True)
    arte.imprimir_mejor_texto("2) Salir                                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu          |", "blanco", True)
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

    
    opcion = int(input(""))
    data = datos.load_data()
    
    massage =  "Cargando..."
    duration = 3
    arte.data_processing_animation(massage,  duration)
    try:
        if opcion == 1:
            print('')
            codigo_modulo = input('Ingrese el codigo del modulo (de 4 - 10 digitos): ') # Solicita el código del módulo.
            datos.registrar_asistencia(data, codigo_modulo)  # Registra la asistencia para el módulo especificado.
            print('')
            return menu_registro_asistencia()
        if opcion == 2:
            return opcion
        if opcion < 1 or opcion > 2:
            print("Error. Opcion no valida.")
            input("presione cualquier tecla para volver al menu ...")
            return menu_registro_asistencia()
        return opcion
    except ValueError:
        print("Error. Opcion no valida.")
        input("presione cualquier tecla para volver al menu ...")
        return menu_registro_asistencia()
    


def menu_consultas_informacion():
    print('')
    arte.consultas()
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(" Consultas de informacion                   |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto("1) Consultar informacion de un estudiante   |", "blanco", True)
    arte.imprimir_mejor_texto("2) Consultar informacion de un docente      |", "blanco", True)
    arte.imprimir_mejor_texto("3) Consultar informacion de un grupo        |", "blanco", True)
    arte.imprimir_mejor_texto("4) Consultar informacion de un modulo       |", "blanco", True)
    arte.imprimir_mejor_texto("5) Salir                                    |", "blanco", True)
    arte.imprimir_mejor_texto("                                            |", "blanco", True)
    arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu          |", "blanco", True)
    arte.imprimir_mejor_texto("--------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

    opcion = int(input(""))
    data = datos.load_data()
    massage =  "Cargando..."
    duration = 3
    arte.data_processing_animation(massage,  duration)
    try:
        if opcion == 1:
            print('')
            codigo_a_buscar = input('Ingrse el codigo de el estudiante a buscar (de 3 - 10 digitos): ') # Solicita el código del estudiante.
            estudiante = datos.buscar_estudiante_por_codigo(data, codigo_a_buscar) # Busca al estudiante.
            if estudiante:
             print(f"Estudiante encontrado: {estudiante}") # Imprime los datos del estudiante.
            else:
             print("Estudiante no encontrado.")
            print('')
            return menu_consultas_informacion()
        if opcion == 2:
            print('')
            cedula = input('Ingrse la cedula de el docente a buscar (de 4 - 10 digitos): ') # Solicita la cedula del docente.
            docente = datos.buscar_docente_por_cedula(data, cedula) # Busca al docente
            if docente:
             print(f"Docente encontrado: {docente}") # Imprime los datos del docente
            else:
             print("Docente no encontrado.")
            print('')
            return menu_consultas_informacion()
        if opcion == 3:
            print('')
            codigo_a_buscar = input('Ingrse el codigo de el grupo a buscar (de 4 - 10 digitos): ') # Solicita el codigo del grupo.
            grupo = datos.buscar_grupo_por_codigo(data, codigo_a_buscar) # Busca el grupo.
            if grupo:
             print(f"Grupo encontrado: {grupo}") # Imprime los datos del grupo
            else:
             print("Grupo no encontrado.")
            print('')
            return menu_consultas_informacion()
        if opcion == 4:
            print('')
            codigo_a_buscar = input('Ingrse el codigo de el modulo a buscar (de 4 - 10 digitos): ') # Solicita el codigo del modulo.
            modulo = datos.buscar_modulo_por_codigo(data, codigo_a_buscar) # Busca el modulo
            if modulo:
             print(f"Modulo encontrado: {modulo}") # Imprime los datos del modulo
            else:
             print("Modulo no encontrado.")
            print('')
            return menu_consultas_informacion()
        if opcion == 5:
          return opcion
        if opcion < 1 or opcion > 5:
            print("Error. Opcion no valida.")
            input("presione cualquier tecla para volver al menu ...")
            return menu_consultas_informacion()
        return opcion
    except ValueError:
        print("Error. Opcion no valida.")
        input("presione cualquier tecla para volver al menu ...")
        return menu_consultas_informacion()

    
def menu_generacion_informes():
    print('')
    arte.informes()
    arte.imprimir_mejor_texto("----------------------------------------------------------------------------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(" Generacion de informes                                                                                         |", "blanco", True)
    arte.imprimir_mejor_texto("                                                                                                                |", "blanco", True)
    arte.imprimir_mejor_texto("1) Generar informe de estudiantes que han llegado tarde a un modulo                                             |", "blanco", True)
    arte.imprimir_mejor_texto("2) Generar informe de estudiantes que se retiraron antes de la finalizacion de una sesion en un mes determinado |", "blanco", True)
    arte.imprimir_mejor_texto("3) Generar informe de estudiantes que no han faltado a ninguna sesion de un modulo durante un mes determinado   |", "blanco", True)
    arte.imprimir_mejor_texto("4) Generar porcentaje de asistencia por módulo                                                                  |", "blanco", True)
    arte.imprimir_mejor_texto("5) Salir                                                                                                        |", "blanco", True)
    arte.imprimir_mejor_texto("                                                                                                                |", "blanco", True)
    arte.imprimir_mejor_texto(">>> Seleccione una opcion del menu                                                                              |", "blanco", True)
    arte.imprimir_mejor_texto("----------------------------------------------------------------------------------------------------------------+", "blanco", True)
    arte.imprimir_mejor_texto(">>> opcion? ", "cyan", True)

    opcion = int(input(""))
    data = datos.load_data()
    
    massage =  "Cargando..."
    duration = 3
    arte.data_processing_animation(massage,  duration)
    try:
        if opcion == 1:
            print('')
            informe = datos.generar_informe_estudiantes_llegaron_tarde(data)
            print(informe)
            
            return menu_generacion_informes()
        if opcion == 2:
            print('')
            datos.generar_informe_estudiantes_retitaron_finalizacion_sesion(data)
            print('')
            return menu_generacion_informes()
        if opcion == 3:
            print('')
            datos.generar_informe_estudiantes_no_faltaron_sesion(data)
            print('')
            return menu_generacion_informes()
        if opcion == 4:
            print('')
            print(datos.generar_porcentaje_asistencia_modulo(data))
            print('')
            return menu_generacion_informes()
        if opcion == 5:
            print('')
            return opcion
        if opcion < 1 or opcion > 5:
            print("Error. Opcion no valida.")
            input("presione cualquier tecla para volver al menu ...")
            return menu_generacion_informes()
        return opcion
    except ValueError:
        print("Error. Opcion no valida.")
        input("presione cualquier tecla para volver al menu ...")
        return menu_generacion_informes()