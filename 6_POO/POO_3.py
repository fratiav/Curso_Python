# Metodos encapsulados
# Atributos encapsulados

class Coche():

    def __init__(self):
        self.__gasolina = 0.0
        self.__puertas = 5
        self.__estadoArranque = False
        self.color = "Rojo"
        self.__chequeoInicial()

    def __chequeoInicial(self):  # Al igual que con los atributos, oble guion bajo para encapsular
        if self.__gasolina > 0 and self.__estadoArranque == False:
            print("El vehículo ha pasado el chequeo inicial y puede arrancarse!")
        else:
            print("El vehículo no tiene gasolina o ya esta arrancado")

    def arrancar(self):
        if self.__gasolina == 0:
            print("El vehículo no tiene gasolina")
        else:
            self.__estadoArranque = True
            print("Vehiculo arrancado")

    def apagar(self):
        if self.__estadoArranque:
            self.__estadoArranque = False
            print("Vehículo apagado")
        else:
            print("El vehículo ya está apagado")

    def rellenarGasolina(self, cantidad):
        if cantidad > 0:
            self.__gasolina += cantidad
        else:
            print("Cantidad no permitida")

    def estadoVehiculo(self):
        print("Estado: ",self.__estadoArranque," - Gasolina: ",self.__gasolina, " - Color: ",self.color, " - Puertas: ",self.__puertas)

hiunday = Coche()
hiunday.arrancar()
hiunday.estadoVehiculo()
hiunday.color = "Blanco"  # Acceso a variable publica
hiunday.rellenarGasolina(100)
hiunday.arrancar()
hiunday.estadoVehiculo()
hiunday.apagar()
hiunday.estadoVehiculo()


