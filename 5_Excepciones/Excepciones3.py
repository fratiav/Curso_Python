#Lanzando excepciones manualmente de forma intencionada --> Raise

def evaluaEdad(edad):
    if edad<0:
        raise TypeError("Has introducido una edad no permitida")
    elif edad<18:
        return "Eres menor de edad"
    elif edad>=18 and edad<=67:
        return "Estas en edad de trabajar"
    elif edad>67:
        return "Estas en edad de jubilacion"

edad = int(input("Edad: "))

try:
    print(evaluaEdad(edad))
except TypeError:
    print("Error de edad")

