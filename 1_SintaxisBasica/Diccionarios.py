# Permite almacenar datos de cualquier tipo, incluso listas o tuplas u otros diccionarios
# Se almacenan los datos con clave:valor
# Los datos almacenados no están ordenados
# Van entre llaves {}

diccionario = {"ESP": "Madrid", "FR": "Paris", "EEUU": "Washington D.C."}

# Impresion del diccionario
print("1 - ", diccionario)

# Acceso por clave al valor
print("2 - ", diccionario["ESP"])

# Acceso a claves
print("3 - ", diccionario.keys())

# Acceso a valores
print("4 - ", diccionario.values())

# Asignacion de un nuevo valor a una clave
diccionario["ESP"] = "CIUDAD DE MADRID"
print("5 - ", diccionario["ESP"])

# Eliminar un elemento del diccionario (del)
del diccionario["FR"]
print("6 - ", diccionario)

# Almacenamiento de tuplas, listas y diccionarios en diccionarios
diccionarioComplejo = {"lista": [1, 3, 5, 7], "tupla": (2, 4, 6, 8), "diccionario": diccionario}
print("7 - ", diccionarioComplejo)
print("8 - ", diccionarioComplejo["lista"])
print("9 - ", diccionarioComplejo)
print("10 - ", diccionarioComplejo)
