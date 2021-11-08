# Una tupla es una lista inmutable (no se puede modificar tras su creación)
# Se pueden utilizar como claves en un diccionario (las listas no)
# Las listas van entre corchetes [ , ], las listas entre parentesis ( , )

tupla = (1, 3, 5, 7, 11)

# Impresion y acceso a valores de una tupla
print("1 - ", tupla)
print("2 - ", tupla[0])

# Hacer una lista de una tupla
listaDeTupla = list(tupla)
print("3 - ", listaDeTupla)  # Se pueden ver los corchetes en la consola de que es una lista

# Se puede hacer tambien desde lista a tupla
listaDeTupla.extend([13, 17, 19])
tuplaDeLista = tuple(listaDeTupla)
print("4 - ", tuplaDeLista)

# Contar cuantos elementos coinciden con la busqueda (count)
print("5 - ", tuplaDeLista.count(13))

# Contar elementos de la tupla (len)
print("6 - ", len(tuplaDeLista))

# Buscar en tupla
tuplaNombres = ("Fran", "Rocio", "Hugo")
if "Rocio" in tuplaNombres:
    print("7 - Hola Rocio")
else:
    print("7 - No esta Rocio")

#Desempaquetado de tuplas en variables simples
tuplaPersona = "Fran",13,"636446253"
nombre, edad, telefono = tuplaPersona #Así se almacenan los valores de la tupla en las variables
print("\nNombre: ",nombre,"\nEdad: ",edad,"\nTelefono: ",telefono)
