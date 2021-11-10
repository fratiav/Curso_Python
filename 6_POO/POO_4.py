# Herencia simple
# Sobreescritura de metodo

class Vehiculos():  # Clase padre o superclase

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelerando = False
        self.frenando = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelerando = True

    def frenar(self):
        self.frenando = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelerando, "\nFrenando: ", self.frenando)


class Moto(Vehiculos):  # Se pone en los parentesis la clase de la que se hereda

    caballito = "No estoy haciendo caballito"

    def hacerCaballito(self):
        self.caballito = "Voy haciendo el caballito"

    def estado(self):   #Sobreescritura del metodo estado de la superclase añadiendo caballito (Debe tener el mismo nombre y los mismos argumentos)
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelerando, "\nFrenando: ", self.frenando, "\nCaballito: ", self.caballito)


miMoto = Moto("BMW", "C")
miMoto.estado()
miMoto.acelerar()
miMoto.hacerCaballito()
miMoto.estado()
