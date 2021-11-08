#Excepciones a errores inesperados
#Try - Except

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion erronea"

while True:
    try:
        op1 = int(input("Operador 1: "))
        op2 = int(input("Operador 2: "))
        print("Resultado de la division: ", division(op1, op2))
        break;
    except ValueError:
        print("Introduce valores numericos")
