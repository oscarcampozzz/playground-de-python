"""14. Juguemos al juego de adivinar el numero, generaremos un numero entre 1 y 100.
Nuestro objetivo es adivinar el numero. 
Si fallamos nos diran si es mayor o menor que el numero buscado.
Tambien poner el numero de intentos requeridos."""

from random import *

def generarNumeroaleatorio(minimo,maximo):
    if minimo>maximo:
        aux=minimo
        minimo=maximo
        maximo=aux
    return randint(minimo,maximo)

i=0
while i<5:
    print(generarNumeroaleatorio(5,10))
    i+=1