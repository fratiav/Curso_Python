# Modularizacion y reutilizacion de codigo

import Operaciones as op  # Al importar el paquete completo hay que llamar a las funciones con nombre de paquete o alias
from Cadenas import comprobarEmail, concatenar  # Con from podemos importar funciones especificas
from Aleatorios import *  # Esta es la forma mas eficiente de importar todo y no tener que llamar al paquete

suma = op.sumar(2, 4)
print(suma)

nombre = "Francisco Jose"
apellidos = "Ratia Vargas"
print(concatenar(nombre, apellidos))

email = "franratvar7@gmail.com"
print("¿Email correcto? ", comprobarEmail(email))

numeroPositivo = aleatorioPositivo()
numeroNegativo = aleatorioNegativo()
print(numeroPositivo, " y ", numeroNegativo)
