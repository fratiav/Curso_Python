numero = int(input("Introduce un numero: ")) #Los datos pedidos desde input son de tipo str --> int() los pasa a entero

def comprobar(numero):
    if numero > 10:
        print("Numero mayor que 10")
    else:
        print("Numero menor que 10")

comprobar(numero)