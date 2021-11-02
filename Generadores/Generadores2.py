#Yield from (Para bucles anidados)
    #Es como un array de dos dimensiones

def miGenerador(*ciudades): #Asterisco: Va a recibir un numero indeterminado de elementos y en forma de tupla
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento  #Acceso a las letras de las ciudades

def miGeneradorIgual(*ciudades):
    for elemento in ciudades:
        yield from elemento  #Acceso a las letras de las ciudades


ciudades_devueltas = miGenerador("Madrid","Barcelona","Jaen","Linares","Rus")
ciudades_devueltas2 = miGeneradorIgual("Madrid","Barcelona","Jaen","Linares","Rus")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas2))
print(next(ciudades_devueltas2))



