#Generador: yield

#Funcion general
def generarPares(limite):
    num = 1
    miLista = []
    while num<limite:
        if num%2 == 0:
            miLista.append(num)
        num = num + 1
    return miLista

print(generarPares(20))

#Funcion generadora
def generadorPares(limite):
    num = 1
    while num<limite:
        if num%2 == 0:
            yield num  #Crea un propio iterable, no necesita crear un objeto lista
        num += 1

pares = generadorPares(20)

print("Primer iterable: ",next(pares)) #Podemos ir recorriendolo con next

for i in pares:
    print(i, end=" ")