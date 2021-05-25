################
# Florencia Edith Jerez - @floedi
# Ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Funcion que solicite el ingreso de un número entero
def ingreso_entero(entero):
    """
    Función que muestra un mensaje y agrega un # para
    indicar el ingreso de un número entero.
    """
try:
    entero = int(input("Poné un número porfas" + " #"))
except ValueError as err:
    print(f"Opa, eso no es un número... Intentá de nuevo")
