edad = int(input("Edad: "))

if edad < 120 and edad >= 0:
    print("Tu edad es de ", edad, " años")
else:
    print("Tu edad esta fuera de rango")

# - - - - - - - - - - - - - - - - - - - - - - - - -

num1 = 1
num2 = 2
num3 = 3
num4 = 4

if num1 < num2 < num3 < num4:
    print("Escala correcta")
else:
    print("Escala incorrecta")

# - - - - - - - - - - - - - - - - - - - - - - - - -

limiteSalarial = 40000
salario = int(input("Salario: "))
minusvalia = input("Minuvalia? S/N: ")
familiaNumerosa = input("Familia Numerosa? S/N: ")

if salario < limiteSalarial and (minusvalia == "S" or familiaNumerosa == "S"):
    print("Se le aplica la beca del ministerio")
else:
    print("No cumples ninguna de las condiciones para solicitar la beca")


# - - - -  - - - - - - - - - - -

asignatura = input("Introduce asignatura optativa: ")

if asignatura in ("Robotica", "Desarrolo IT", "Big Data"):
    print("Disponemos de esa asignatura")
else:
    print("No disponemos de esa asignatura")


# - - - - - - - - - - - - - - -
    #Se pueden añadir listas y tuplas
tuplaTallas = ("S","M","L")
listaTallas = ["36","38","40"]

talla = input("Talla: ")

if talla in tuplaTallas or talla in listaTallas:
    print("Tu talla está disponible")
else:
    print("No tenemos tu talla")

