numero1 = int(input("Introduce primer numero: "))
numero2 = int(input("Introduce segundo numero: "))

def mayor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    elif numero2 > numero1:
        return numero2
    else:
        return False

resultado = mayor(numero1,numero2)

if resultado is not False:
    print("Mayor: ",resultado)
else:
    print("Son iguales")