#Bucle For
    #Sintaxis  ---    for (variable) in (elemento a recorrer):
    #Elemento a recorrer: lista, cadena de texto, rango, tupla...

tupla = (3,4,5,6,7)
lista = ["a","e","i","o","u"]
rango = range(0,10)  #En los rango no se incluye el ultimo digito (excluido el 10)
cadenas = ["Fran","Ratia"]

for i in tupla:
    print("Numero: ",i)

for j in lista:
    print("Vocal: ",j)

for z in rango:
    if(z%2 != 0):
        print(z)

for k in cadenas:
    for l in k:
        print(l, end="")