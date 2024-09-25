import sys  # Importa el módulo sys para manipulación del sistema
import time  # Importa el módulo time para manejar el tiempo

def data_processing_animation(message, duration):
    print(message, end=" ", flush=True)  # Imprime el mensaje de inicio sin nueva línea
    loading_symbols = ["✸", "✹", "✺", "✹"]  # Lista de símbolos para la animación de carga
    start_time = time.time()  # Guarda el tiempo de inicio

    while time.time() - start_time < duration:  # Ciclo hasta que pase la duración especificada
        for symbol in loading_symbols:  # Itera sobre los símbolos de carga
            sys.stdout.write(f"\r{symbol} {message}")  # Imprime el símbolo de carga y el mensaje
            sys.stdout.flush()  # Asegura que se imprima inmediatamente
            time.sleep(0.2)  # Pausa para crear la animación

    sys.stdout.write("\r✸ ¡Proceso finalizado!\n")  # Indica que el proceso ha terminado

massage =  "Procesando datos..."  # Mensaje de procesamiento
duration = 3  # Duración de la animación en segundos
# data_processing_animation(massage, duration)  # Llama a la función (comentada)

# Inicializa
def imprimir_mejor_texto(texto, color='default', negrita=False):
    # Diccionario de colores ANSI
    colores = {
        'default': '\033[39m',
        'rojo': '\033[31m',
        'verde': '\033[32m',
        'amarillo': '\033[33m',
        'azul': '\033[34m',
        'morado': '\033[35m',
        'cyan': '\033[36m',
        'blanco': '\033[37m',
    }

    # Código ANSI para negrita
    negrita_inicio = '\033[1m' if negrita else ''  # Activa negrita si es solicitado
    negrita_fin = '\033[22m' if negrita else ''  # Desactiva negrita

    # Color seleccionado
    color_inicio = colores.get(color, colores['default'])  # Selecciona el color
    color_fin = '\033[39m'  # Reset de color

    # Formatear texto
    texto_formateado = f"{negrita_inicio}{color_inicio}{texto}{negrita_fin}{color_fin}"
    return print(texto_formateado)  # Imprime el texto formateado

def bienvenido():
    # Imprime un mensaje de bienvenida en color verde y en negrita
    imprimir_mejor_texto('                              ██████╗  ██╗ ███████╗ ███╗  ██╗ ██╗   ██╗ ███████╗ ███╗  ██╗ ██╗ ██████╗   █████╗ ', color='verde', negrita=True)
    imprimir_mejor_texto('                              ██╔══██╗ ██║ ██╔════╝ ████╗ ██║ ██║   ██║ ██╔════╝ ████╗ ██║ ██║ ██╔══██╗ ██╔══██╗', color='verde', negrita=True)
    imprimir_mejor_texto('                              ██████╦╝ ██║ █████╗   ██╔██╗██║ ╚██╗ ██╔╝ █████╗   ██╔██╗██║ ██║ ██║  ██║ ██║  ██║', color='verde', negrita=True)
    imprimir_mejor_texto('                              ██╔══██╗ ██║ ██╔══╝   ██║╚████║  ╚████╔╝  ██╔══╝   ██║╚████║ ██║ ██║  ██║ ██║  ██║', color='verde', negrita=True)
    imprimir_mejor_texto('                              ██████╦╝ ██║ ███████╗ ██║ ╚███║   ╚██╔╝   ███████╗ ██║ ╚███║ ██║ ██████╔╝ ╚█████╔╝', color='verde', negrita=True)
    imprimir_mejor_texto('                              ╚═════╝  ╚═╝ ╚══════╝ ╚═╝  ╚══╝    ╚═╝    ╚══════╝ ╚═╝  ╚══╝ ╚═╝ ╚═════╝   ╚════╝ ', color='verde', negrita=True)

    print('\n\n\n\n\n')  # Espacios en blanco

    return bienvenido  

def adios():
    # Imprime un mensaje de despedida en color amarillo y en negrita
    imprimir_mejor_texto('                                                        █████╗  ██████╗  ██╗  █████╗   ██████╗', 'amarillo', True)
    imprimir_mejor_texto('                                                       ██╔══██╗ ██╔══██╗ ██║ ██╔══██╗ ██╔════╝', 'amarillo', True)
    imprimir_mejor_texto('                                                       ███████║ ██║  ██║ ██║ ██║  ██║ ╚█████╗ ', 'amarillo', True)
    imprimir_mejor_texto('                                                       ██╔══██║ ██║  ██║ ██║ ██║  ██║  ╚═══██╗', 'amarillo', True)
    imprimir_mejor_texto('                                                       ██║  ██║ ██████╔╝ ██║ ╚█████╔╝ ██████╔╝', 'amarillo', True)
    imprimir_mejor_texto('                                                       ╚═╝  ╚═╝ ╚═════╝  ╚═╝  ╚════╝  ╚═════╝ ', 'amarillo', True)

    print('\n\n\n\n\n')  # Espacios en blanco

    return adios  

def grupos():
    # Imprime un mensaje relacionado a grupos en color cyan y en negrita
    imprimir_mejor_texto(" ██████╗  ██████╗  ██╗   ██╗ ██████╗   █████╗   ██████╗", "cyan", True)
    imprimir_mejor_texto("██╔════╝  ██╔══██╗ ██║   ██║ ██╔══██╗ ██╔══██╗ ██╔════╝", "cyan", True)
    imprimir_mejor_texto("██║  ██╗  ██████╔╝ ██║   ██║ ██████╔╝ ██║  ██║ ╚█████╗ ", "cyan", True)
    imprimir_mejor_texto("██║  ╚██╗ ██╔══██╗ ██║   ██║ ██╔═══   ██║  ██║  ╚═══██╗", "cyan", True)
    imprimir_mejor_texto("╚██████╔╝ ██║  ██║ ╚██████╔╝ ██║      ╚█████╔╝ ██████╔╝", "cyan", True)
    imprimir_mejor_texto(" ╚═════╝  ╚═╝  ╚═╝  ╚═════╝  ╚═╝       ╚════╝  ╚═════╝ ", "cyan", True)
    
    print('')  # Espacio en blanco
    
    return grupos  

def modulos():
    # Imprime un mensaje relacionado a módulos en color cyan y en negrita
    imprimir_mejor_texto("███╗   ███╗  █████╗  ██████╗  ██╗   ██╗ ██╗       █████╗   ██████╗", "cyan", True)
    imprimir_mejor_texto("████╗ ████║ ██╔══██╗ ██╔══██╗ ██║   ██║ ██║      ██╔══██╗ ██╔════╝", "cyan", True)
    imprimir_mejor_texto("██╔████╔██║ ██║  ██║ ██║  ██║ ██║   ██║ ██║      ██║  ██║ ╚█████╗ ", "cyan", True)
    imprimir_mejor_texto("██║╚██╔╝██║ ██║  ██║ ██║  ██║ ██║   ██║ ██║      ██║  ██║  ╚═══██╗", "cyan", True)
    imprimir_mejor_texto("██║ ╚═╝ ██║ ╚█████╔╝ ██████╔╝ ╚██████╔╝ ███████╗ ╚█████╔╝ ██████╔╝", "cyan", True)
    imprimir_mejor_texto("╚═╝     ╚═╝  ╚════╝  ╚═════╝   ╚═════╝  ╚══════╝  ╚════╝  ╚═════╝ ", "cyan", True)
    
    print('')  # Espacio en blanco
    
    return modulos  

def estudiantes():
    # Imprime un mensaje relacionado a estudiantes en color cyan y en negrita
    imprimir_mejor_texto("███████╗  ██████╗ ████████╗ ██╗   ██╗ ██████╗  ██╗  █████╗  ███╗  ██╗ ████████╗ ███████╗  ██████╗", "cyan", True)
    imprimir_mejor_texto("██╔════╝ ██╔════╝ ╚══██╔══╝ ██║   ██║ ██╔══██╗ ██║ ██╔══██╗ ████╗ ██║ ╚══██╔══╝ ██╔════╝ ██╔════╝", "cyan", True)
    imprimir_mejor_texto("█████╗   ╚█████╗     ██║    ██║   ██║ ██║  ██║ ██║ ███████║ ██╔██╗██║    ██║    █████╗   ╚█████╗ ", "cyan", True)
    imprimir_mejor_texto("██╔══╝    ╚═══██╗    ██║    ██║   ██║ ██║  ██║ ██║ ██╔══██║ ██║╚████║    ██║    ██╔══╝    ╚═══██╗", "cyan", True)
    imprimir_mejor_texto("███████╗ ██████╔╝    ██║    ╚██████╔╝ ██████╔╝ ██║ ██║  ██║ ██║ ╚███║    ██║    ███████╗ ██████╔╝", "cyan", True)
    imprimir_mejor_texto("╚══════╝ ╚═════╝     ╚═╝     ╚═════╝  ╚═════╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚══╝    ╚═╝    ╚══════╝ ╚═════╝ ", "cyan", True)
    
    print('')  # Espacio en blanco
    
    return estudiantes  

def docentes():
    # Imprime un mensaje relacionado a docentes en color cyan y en negrita
    imprimir_mejor_texto("██████╗   █████╗   █████╗  ███████╗ ███╗  ██╗ ████████╗ ███████╗  ██████╗", "cyan", True)
    imprimir_mejor_texto("██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔════╝ ████╗ ██║ ╚══██╔══╝ ██╔════╝ ██╔════╝", "cyan", True)
    imprimir_mejor_texto("██║  ██║ ██║  ██║ ██║  ╚═╝ █████╗   ██╔██╗██║    ██║    █████╗   ╚█████╗ ", "cyan", True)
    imprimir_mejor_texto("██║  ██║ ██║  ██║ ██║  ██╗ ██╔══╝   ██║╚████║    ██║    ██╔══╝    ╚═══██╗", "cyan", True)
    imprimir_mejor_texto("██████╔╝ ╚█████╔╝ ╚█████╔╝ ███████╗ ██║ ╚███║    ██║    ███████╗ ██████╔╝", "cyan", True)
    imprimir_mejor_texto("╚═════╝   ╚════╝   ╚════╝  ╚══════╝ ╚═╝  ╚══╝    ╚═╝    ╚══════╝ ╚═════╝ ", "cyan", True)
    
    print('')  # Espacio en blanco
    
    return docentes  

def asistencia():
    # Imprime un mensaje relacionado a asistencia en color cyan y en negrita
    imprimir_mejor_texto(" █████╗   ██████╗ ██╗  ██████╗ ████████╗ ███████╗ ███╗  ██╗  █████╗  ██╗  █████╗ ", "cyan", True)
    imprimir_mejor_texto("██╔══██╗ ██╔════╝ ██║ ██╔════╝ ╚══██╔══╝ ██╔════╝ ████╗ ██║ ██╔══██╗ ██║ ██╔══██╗", "cyan", True)
    imprimir_mejor_texto("███████║ ╚█████╗  ██║ ╚█████╗     ██║    █████╗   ██╔██╗██║ ██║  ╚═╝ ██║ ███████║", "cyan", True)
    imprimir_mejor_texto("██╔══██║  ╚═══██╗ ██║  ╚═══██╗    ██║    ██╔══╝   ██║╚████║ ██║  ██╗ ██║ ██╔══██║", "cyan", True)
    imprimir_mejor_texto("██║  ██║ ██████╔╝ ██║ ██████╔╝    ██║    ███████╗ ██║ ╚███║ ╚█████╔╝ ██║ ██║  ██║", "cyan", True)
    imprimir_mejor_texto("╚═╝  ╚═╝ ╚═════╝  ╚═╝ ╚═════╝     ╚═╝    ╚══════╝ ╚═╝  ╚══╝  ╚════╝  ╚═╝ ╚═╝  ╚═╝", "cyan", True)
    
    print('')  # Espacio en blanco
    
    return asistencia  

def consultas():
    # Imprime un mensaje relacionado a consultas en color cyan y en negrita
    imprimir_mejor_texto(" █████╗   █████╗  ███╗  ██╗  ██████╗ ██╗   ██╗ ██╗      ████████╗  █████╗   ██████╗", "cyan", True)
    imprimir_mejor_texto("██╔══██╗ ██╔══██╗ ████╗ ██║ ██╔════╝ ██║   ██║ ██║      ╚══██╔══╝ ██╔══██╗ ██╔════╝", "cyan", True)
    imprimir_mejor_texto("██║  ╚═╝ ██║  ██║ ██╔██╗██║ ╚█████╗  ██║   ██║ ██║         ██║    ███████║ ╚█████╗ ", "cyan", True)
    imprimir_mejor_texto("██║  ██╗ ██║  ██║ ██║╚████║  ╚═══██╗ ██║   ██║ ██║         ██║    ██╔══██║  ╚═══██╗", "cyan", True)
    imprimir_mejor_texto("╚█████╔╝ ╚█████╔╝ ██║ ╚███║ ██████╔╝ ╚██████╔╝ ███████╗    ██║    ██║  ██║ ██████╔╝", "cyan", True)
    imprimir_mejor_texto(" ╚════╝   ╚════╝  ╚═╝  ╚══╝ ╚═════╝   ╚═════╝  ╚══════╝    ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ", "cyan", True)
    
    print('')  # Espacio en blanco
    
    return consultas  
def informes():
    # Imprime un mensaje relacionado a informes en color cyan y en negrita
    imprimir_mejor_texto("██╗ ███╗  ██╗ ███████╗  █████╗  ██████╗  ███╗   ███╗ ███████╗  ██████╗", "cyan", True)
    imprimir_mejor_texto("██║ ████╗ ██║ ██╔════╝ ██╔══██╗ ██╔══██╗ ████╗ ████║ ██╔════╝ ██╔════╝", "cyan", True)
    imprimir_mejor_texto("██║ ██╔██╗██║ █████╗   ██║  ██║ ██████╔╝ ██╔████╔██║ █████╗   ╚█████╗ ", "cyan", True)
    imprimir_mejor_texto("██║ ██║╚████║ ██╔══╝   ██║  ██║ ██╔══██╗ ██║╚██╔╝██║ ██╔══╝    ╚═══██╗", "cyan", True)
    imprimir_mejor_texto("██║ ██║ ╚███║ ██║      ╚█████╔╝ ██║  ██║ ██║ ╚═╝ ██║ ███████╗ ██████╔╝", "cyan", True)
    imprimir_mejor_texto("╚═╝ ╚═╝  ╚══╝ ╚═╝       ╚════╝  ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚══════╝ ╚═════╝ ", "cyan", True)
    
    print('')  # Espacio en blanco
    
    return informes 

# Puedes llamar a la función data_processing_animation para ver la animación
# massage =  "Procesando datos..."
# duration = 3
# data_processing_animation(massage, duration)




