class Coche():  #Clase coche
    largoChasis = 250  #Atributos
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self): #Metodos
        self.enMarcha = True

    def estado(self):  #Self es como This en otros lenguajes
        if self.enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche está parado"


miCoche = Coche()
print("Coche 1: ",miCoche.enMarcha, ", ", miCoche.estado())

# - - - - - - - - - - SEGUNDO OBJETO - - - - - - - - - #

miCoche2 = Coche()
miCoche2.arrancar()
print("Coche 2: ",miCoche2.enMarcha, ", ", miCoche2.estado())