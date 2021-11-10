# Herencia multiple
import random


class Ordenador:

    def __init__(self, so):
        self.__claveMAC = random.randint(0, 1000)
        self.__so = so
        self.__encendido = False
        self.__chequeo()

    def definirSO(self, sistema):
        self.__so = sistema
        print("Se ha instalado un nuevo sistema operativo: ", self.__so)

    def verClaveMAC(self):
        return self.__claveMAC

    def sistemaOperativo(self):
        return self.__so

    def encenderPC(self):
        self.__encendido = True
        print("Ordenador encendido")

    def apagarPC(self):
        self.__encendido = False
        print("Ordenador apagado")

    def estado(self):
        return self.__encendido

    def __chequeo(self):
        if self.__so != "":
            print("Ordenador preparado")
        else:
            print("Ordenador sin sistema operativo")


class Teclado:

    def __init__(self):
        self.tipo = "QWERTY"
        self.__tactil = True

    def pulsarTecla(self, tecla):
        print("Has pulsado la tecla: ", tecla)


class Movil(Ordenador, Teclado):  # Herencia multiple. El constructor es el de la primera clase indicada

    def __init__(self, so, marca, modelo, pantalla, pulgadas):
        super().__init__(
            so)  # Debemos inicializar la clase padre para que no de error con los atributos de su instanciacion
        self.__pantalla = pantalla
        self.__pulgadas = pulgadas
        self.__marca = marca
        self.__modelo = modelo

    def descripcion(self):
        print("Telefono: ", self.__marca, self.__modelo, "\nPantalla: ", self.__pantalla, self.__pulgadas, "pulgadas",
              "\nS.O: ", self.sistemaOperativo(),
              "\nTipo de teclado: ", "\nEstado: ", self.estado())

    def jugar(self, juego):
        print("Se ha iniciado el juego: ", juego)


miMovil = Movil("MAC", "iPhone", "7S", "OLED", 11)
miMovil.descripcion()
miMovil.pulsarTecla("z")
miMovil.encenderPC()
print(isinstance(miMovil,Ordenador)) #Este metodo indica si una clase hereda de otra