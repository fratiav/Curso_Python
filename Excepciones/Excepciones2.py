#Tratamiento de varias excepciones a la vez
#Clausula finally

def division(op1,op2):
    try:
        return op1/op2
    except ZeroDivisionError:
        return ZeroDivisionError

while True:
    try:
        op1 = int(input("Operador 1: "))
        op2 = int(input("Operador 2: "))
        resultado = division(op1,op2)
        if resultado == ZeroDivisionError:
            print("Has dividido entre 0")
        else:
            print("Resultado de la division: ", division(op1, op2))
            break;

    except ValueError:
        print("Introduce valores numericos")
    except BufferError:  #Las excepciones se concatenan añadiendo excepts
        print("Error de buffer")

    finally:
        print("Fin del codigo")
