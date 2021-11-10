# Polimorfismo

class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


moto = Moto()
moto.desplazamiento()
coche = Coche()
coche.desplazamiento()
camion = Camion()
camion.desplazamiento()

# No obstante se puede utilizar el polimorfismo para, con un metodo generico, actuar sobre el desplazamiento indicado
# Al ser un lenguaje no tipado no hay que especificar el tipo de objeto que se pasa por el argumento. Esto facilita las cosas

print("- - - - - - - - - - - - - - - - -")

def desplazamientoPolimorfismo(vehiculo):
    vehiculo.desplazamiento()


desplazamientoPolimorfismo(moto)
desplazamientoPolimorfismo(coche)
desplazamientoPolimorfismo(camion)
