import json  # Importa el módulo para manejar archivos JSON
from datetime import datetime  # Importa la clase datetime para trabajar con fechas y horas

DATA_FILE = 'Json/sisgesa_data.json'  # Define el archivo donde se almacenarán los datos

# Función para cargar los datos del sistema
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)  # Carga los datos desde el archivo JSON
            return data  # Devolver los datos cargados
    except FileNotFoundError:
        # Si el archivo no existe, devolver un diccionario con las estructuras necesarias
        return {
            "grupos": [],
            "modulos": [],
            "estudiantes": [],
            "docentes": [],
            "asistencia": []
        }
    except json.JSONDecodeError:
        # Si el archivo está corrupto, devolver la estructura por defecto
        print("Error: El archivo de datos está corrupto. Se utilizarán valores predeterminados.")
        return {
            "grupos": [],
            "modulos": [],
            "estudiantes": [],
            "docentes": [],
            "asistencia": []
        }

data = load_data()  # Carga los datos al iniciar el programa

# Función para guardar los datos del sistema
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)  # Guarda los datos en el archivo JSON

# Función para registrar grupos
def registrar_grupo(data):
    codigo = input('Ingrese el código del grupo (de 4 - 10 digitos): ')  # Solicita el código del grupo
    nombre = input('Ingrese el nombre del grupo (de 3 - 26 caracteres): ')  # Solicita el nombre del grupo
    sigla = input('Ingrese la sigla del grupo (de 1 - 4 caracteres): ')  # Solicita la sigla del grupo
    grupo = {"codigo": codigo, "nombre": nombre, "sigla": sigla}  # Crea un diccionario para el grupo
    data["grupos"].append(grupo)  # Añade el grupo a la lista de grupos
    save_data(data)  # Guarda los datos actualizados

def validar_hora(hora):
    try:
        # Intenta convertir la cadena en un objeto datetime
        datetime.strptime(hora, "%H:%M")
        return True  # Retorna True si la hora es válida
    except ValueError:
        return False  # Retorna False si la hora no es válida

# Función para registrar módulos
def registrar_modulo(data):
    codigo = input('Ingrese el código del módulo (de 4 - 10 digitos): ')  # Solicita el código del módulo
    nombre = input('Ingrese el nombre del módulo (de 3 - 56 carecteres): ')  # Solicita el nombre del módulo
    duracion = input('Ingrese la duración en semanas (1 o 2 digitos): ')  # Solicita la duración del módulo
    # Validación de la hora de entrada
    while True:
        H_entrada = input('Ingrese la hora de entrada del modulo (formato HH:MM): ')
        if validar_hora(H_entrada):
            break  # Sale del bucle si la hora es válida
        else:
            print("Formato incorrecto. Asegúrese de ingresar la hora en formato HH:MM.")
    # Validación de la hora de salida
    while True:
        H_salida = input('Ingrese la hora de salida del modulo (formato HH:MM): ')
        if validar_hora(H_salida):
            break  # Sale del bucle si la hora es válida
        else:
            print("Formato incorrecto. Asegúrese de ingresar la hora en formato HH:MM.")
    modulo = {"codigo": codigo, "nombre": nombre, "duracion": duracion, 'H_entrada': H_entrada, 'H_salida': H_salida }
    data["modulos"].append(modulo)  # Añade el módulo a la lista de módulos
    save_data(data)  # Guarda los datos actualizados

# Función para registrar estudiantes
def registrar_estudiante(data):
    codigo = input('Ingrese el código del estudiante (de 3 - 10 digitos): ')  # Solicita el código del estudiante
    nombre = input('Ingrese el nombre del estudiante (de 3 - 56 caracteres): ')  # Solicita el nombre del estudiante
    sexo = input('Ingrese el sexo del estudiante (F o M): ')  # Solicita el sexo del estudiante
    edad = input('Ingrese la edad del estudiante : ')  # Solicita la edad del estudiante
    estudiante = {"codigo": codigo, "nombre": nombre, "sexo": sexo, "edad": edad}  # Crea un diccionario para el estudiante
    data["estudiantes"].append(estudiante)  # Añade el estudiante a la lista de estudiantes
    save_data(data)  # Guarda los datos actualizados

# Función para registrar docentes
def registrar_docente(data):
    cedula = input('Ingrese la cédula del docente (de 4 - 10 digitos): ')  # Solicita la cédula del docente
    nombre = input('Ingrese el nombre del docente (de 4 - 56 carecteres): ')  # Solicita el nombre del docente
    docente = {"cedula": cedula, "nombre": nombre}  # Crea un diccionario para el docente
    data["docentes"].append(docente)  # Añade el docente a la lista de docentes
    save_data(data)  # Guarda los datos actualizados

# Función para obtener el horario de un módulo
def horario_modulo(data, codigo_modulo):
    modulos = data.get("modulos", [])  # Obtiene la lista de módulos
    for modulo in modulos:
        if modulo["codigo"] == codigo_modulo:
            return modulo["H_entrada"], modulo["H_salida"]  # Devuelve la hora de entrada y salida
    return None, None  # Si no se encuentra el módulo

# Función para registrar asistencia de estudiantes
def registrar_asistencia(data, codigo_modulo):
    fecha = datetime.today().strftime("%Y-%m-%d")  # Obtiene la fecha actual
    
    # Obtener horario del módulo
    hora_entrada, hora_salida = horario_modulo(data, codigo_modulo)

    if hora_entrada is None:
        print("Módulo no encontrado.")  # Mensaje si el módulo no existe
        return

    asistencia = {
        "fecha": fecha,
        "modulo": codigo_modulo,
        "detalles": []  # Detalles de la asistencia
    }

    while True:
        codigo = input('Ingrese el código del estudiante (o "fin" para terminar): ').strip()
        if codigo.lower() == "fin":
            break  # Termina el registro de asistencia si se ingresa "fin"
        
        hora_actual = datetime.now().strftime("%H:%M")  # Obtiene la hora actual

        # Verificar si el estudiante llegó a tiempo o no
        if hora_actual > hora_entrada:
            estado_entrada = "Llego tarde"  # El estudiante llegó tarde
        elif hora_entrada <= hora_actual:
            estado_entrada = "Presente"  # El estudiante llegó a tiempo
        else:
            estado_entrada = "Inasistencia"  # El estudiante no llegó

        # Solicitar la hora de salida
        hora_salida_estudiante = input(f'Ingrese la hora de salida para el estudiante {codigo} (HH:MM): ').strip()

        # Verificar la hora de salida
        if hora_salida_estudiante < hora_entrada:
            estado_salida = "Inasistencia"  # No asistió
        elif hora_salida_estudiante < hora_salida:
            estado_salida = "Salió antes"  # Salió antes de tiempo
        elif hora_salida_estudiante >= hora_salida:
            estado_salida = "Salió a normal"  # Salió a tiempo

        asistencia["detalles"].append({
            "codigo": codigo,
            "estado_entrada": estado_entrada,
            "hora_entrada": hora_actual,
            "estado_salida": estado_salida,
            "hora_salida": hora_salida_estudiante
        })

    data["asistencia"].append(asistencia)  # Añade la asistencia a la lista de asistencias
    save_data(data)  # Guarda los datos actualizados
    print("Asistencia registrada exitosamente.")  # Mensaje de éxito
    
# Consultas de información
def consultar_informacion(data, entidad):
    return data.get(entidad, [])  # Devuelve la información de la entidad solicitada

def buscar_estudiante_por_codigo(data, codigo):
    estudiantes = consultar_informacion(data, 'estudiantes')  # Obtiene la lista de estudiantes
    for estudiante in estudiantes:
        if estudiante['codigo'] == codigo:
            return estudiante  # Devuelve el estudiante encontrado
    return None  # Retorna None si no se encuentra el estudiante

def buscar_docente_por_cedula(data, cedula):
    docentes = consultar_informacion(data, 'docentes')  # Obtiene la lista de docentes
    for docente in docentes:
        if docente['cedula'] == cedula:
            return docente  # Devuelve el docente encontrado
    return None  # Retorna None si no se encuentra el docente

def buscar_grupo_por_codigo(data, codigo):
    grupos = consultar_informacion(data, 'grupos')  # Obtiene la lista de grupos
    for grupo in grupos:
        if grupo['codigo'] == codigo:
            return grupo  # Devuelve el grupo encontrado
    return None  # Retorna None si no se encuentra el grupo

def buscar_modulo_por_codigo(data, codigo):
    modulos = consultar_informacion(data, 'modulos')  # Obtiene la lista de módulos
    for modulo in modulos:
        if modulo['codigo'] == codigo:
            return modulo  # Devuelve el módulo encontrado
    return None  # Retorna None si no se encuentra el módulo

# Informes de asistencia
def generar_informe_estudiantes_llegaron_tarde(data):
    informe = []  # Inicializa el informe
    mes = input('Ingrese el mes donde quiere revisar la asistencia (2 digitos, ejemplo 01):  ')  # Solicita el mes
    year = input('Ingrese el año donde quiere revisar el mes de la asistencia:  ')  # Solicita el año
    # Filtrar asistencias por el mes y año especificados
    asistencias_mes = [
        a for a in data["asistencia"] 
        if a["fecha"].startswith(f"{year}-{mes}")  # Asegura que el mes tenga dos dígitos
    ]
    for asistencia in asistencias_mes:
        for estudiante in data["estudiantes"]:
            # Buscar si el estudiante está en la asistencia
            estudiante_en_asistencia = next((es for es in asistencia["detalles"] if es["codigo"] == estudiante["codigo"]), None)
            # Verificar si el estudiante llegó tarde
            if estudiante_en_asistencia and estudiante_en_asistencia["estado_salida"] == "Llego tarde":
                informe.append({
                    "nombre": estudiante["nombre"],
                    "codigo": estudiante["codigo"],
                    "fecha": asistencia["fecha"],
                })
    return informe  # Retorna el informe generado
                
def generar_informe_estudiantes_retitaron_finalizacion_sesion(data):
    informe = []  # Inicializa el informe
    asistencias_hoy = [a for a in data["asistencia"] if a["fecha"] == datetime.today().strftime("%Y-%m-%d")]

    for asistencia in asistencias_hoy:
        for estudiante in data["estudiantes"]:
            # Se determina si el estudiante se retiró
            retiro = estudiante["codigo"] not in asistencia["estudiantes"]
            informe.append({
                "nombre": estudiante["nombre"], 
                "codigo": estudiante["codigo"],  
                "retiro": retiro
            })

    return print(retiro)  # Imprime el resultado del retiro

def generar_informe_estudiantes_no_faltaron_sesion(data):
    informe = []  # Inicializa el informe
    asistencias_hoy = [a for a in data["asistencia"] if a["fecha"] == datetime.today().strftime("%Y-%m-%d")]

    for asistencia in asistencias_hoy:
        for estudiante in data["estudiantes"]:
            no_faltaron = estudiante["codigo"] in asistencia["estudiantes"]  # Verifica si el estudiante asistió
            informe.append({
                "nombre": estudiante["nombre"], 
                "codigo": estudiante["codigo"],  
                "no_faltaron": no_faltaron
            })
    return print(no_faltaron)  # Imprime el resultado de asistencia

def generar_porcentaje_asistencia_modulo(data):
    informe = []  # Inicializa el informe

    for grupo in data["grupos"]:
        for modulo in grupo.get("modulos", []):
            estudiantes_grupo = [
                estudiante["codigo"] for estudiante in data["estudiantes"] 
                if estudiante.get("grupo") == grupo["codigo"]
            ]
            total_estudiantes = len(estudiantes_grupo)  # Total de estudiantes en el grupo

            if total_estudiantes == 0:
                continue  # Si no hay estudiantes, saltamos el módulo

            asistencias_modulo = [
                asistencia["estudiantes"] for asistencia in data["asistencia"] 
                if asistencia.get("modulo") == modulo["nombre"]
            ]

            # Aplanamos la lista de listas de asistencias
            asistencias_modulo = [codigo for sublist in asistencias_modulo for codigo in sublist]
            asistencias_totales = len(set(asistencias_modulo))  # Eliminamos duplicados

            porcentaje = (asistencias_totales / total_estudiantes) * 100 if total_estudiantes > 0 else 0
            informe.append({
                "modulo": modulo["nombre"], 
                "porcentaje": porcentaje  # Añade el porcentaje de asistencia al informe
            })

    return porcentaje  # Retorna el porcentaje final
