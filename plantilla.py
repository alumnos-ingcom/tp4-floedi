################
# Florencia Edith Jerez - @floedi
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
# 
# 1. Ingreso de números enteros
# Limitar el ingreso de valores y gestionar los errores que dicha actividad
# puedan producir es una actividad cotidiana en los primeros programas a desarrollar.
# Por lo que es un excelente primer ejercicio.
# 
# Escribir una funcion que solicite el ingreso de un número entero y vuelva a
# solicitarlo en caso de ingresar un valor incorrecto.
# 
# Escribir una funcion que solicite el ingreso de un número entero entre dos valores.
# 
# Las tres funciones al rechazar el ingreso de valores incorrectos, deben levantar
# la excepción Ingreso Incorrecto con un mensaje que indique lo sucedido.



import tp4ej1 as soporte
#esto importa un archivo, pero como es el primero no se si sirve

soporte.ingreso_entero("Hola Mundo")
#que es esto?


def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass
#que es pass?


#Ejemplo de implementación

def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    #que eran las 3 comillas'
    
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero


