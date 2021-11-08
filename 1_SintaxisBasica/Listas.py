miLista = ["Fran","Rocio","Ruido","Jero","Rosa"]

#Impresion de una lista completa
print(miLista[:])
print(miLista) #Es lo mismo

#Acceso a elementos
print("1 ",miLista[1])
print("2 ",miLista[-3]) #Accede desde el final hacia atras
print("3 ",miLista[0:2]) #Devuelve todos los indices desde el 0 (incluido) hasta el 2 (excluido)
print("4 ",miLista[:2]) #Lo mismo que el anterior
print("5 ",miLista[3:]) #Desde el 3 hasta el final

#Añadir elementos (append,insert,extend)
miLista.append("Luisa") #Añade elemento al final de la lista
print("6 ",miLista)
miLista.insert(3,"Fernando") #Inserta un nuevo elemento en una posicion seleccionada
print("7 ",miLista)
miLista.extend(["Felipe","Marigema","Canuto"]) #Añade mas de un elemento
print("8 ",miLista)

#Devolver el indice de un elemento de la lista
print("9 ",miLista.index("Rocio")) #Si hay repetidos devuelve el primero

#Encontrar un elemento en la lista
if("Fran" in miLista):
    print("10 El elemento Fran se encuentra en la lista")
else:
    print("10 El elemento Fran no se encuentra en la lista")

#Eliminar un elemento
miLista.remove("Canuto")
print("11 ",miLista[:])
miLista.pop(0) #Se le pone el indice para eliminar ese elemento. Si no se pone nada elimina el ultimo
miLista.pop()
print("12 ",miLista[:])

#Las listas pueden contener distintos tipos de datos
nuevaLista = ["Fran",True,5,89.34,"Rocio"]
print("13 ",nuevaLista[:])

#Union de dos listas (+)
listaTotal = miLista + nuevaLista
print("14 ",listaTotal[:])

#Multiplicador de contenido o repetidor (*)
listaMultiplicada = ["5"]*5
print("15 ",listaMultiplicada[:])

#Veces que aparece un elemento (count)
print("16 ",listaMultiplicada.count("5"))

#Ordenacion de listas (No se pueden ordenar listas con diferente tipo de dato)
listaDesordenada = [5,2,7,1,6,4,23,15]
print("17 ",sorted(listaDesordenada,reverse=True)) #Existe un metodo python llamado sorted() que devuelve una lista ordenada
listaDesordenada.sort()
print("18 ",sorted(listaDesordenada)) #El metodo sort() ordena la lista y puede incluirse una clave de ordenacion
textosDesordenados = ["z","Fran","a","BauFest"]
textosDesordenados.sort() #Por defecto, orden alfabetico con distincion de mayusculas y minusculas
print("19 ",textosDesordenados)
textosDesordenados.sort(key=str.lower)  #Orden alfabetico sin distincion de mayusculas y minusculas
print("20 ",textosDesordenados)
textosDesordenados.sort(key=len)  #Por longitud de cadena y orden alfabético
print("21 ",textosDesordenados)

# - - - - - - - - - - - -

