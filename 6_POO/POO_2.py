#Argumentos en métodos
#Encapsulacion de atributos

class Persona():
    def __init__(self):  #Metodo de iniciación de clase
        self.edad = ""
        self.altura = ""
        self.nombre = ""
        self.__clase = "Humano" #Encapsulacion de atributo. Se le añaden dos guiones bajos al nombre del atributo para encapsularlo

    def definirAtributos(self,edad,altura,nombre): #Le pasamos parametros en los argumentos
        self.edad = edad
        self.altura = altura
        self.nombre = nombre

    def descripcion(self):
        print(self.nombre," tiene ",self.edad, " años y mide ",self.altura," cm. Es ",self.__clase,".")


persona1 = Persona()
persona1.definirAtributos(28,179,"Francisco Jose Ratia Vargas")
persona1.descripcion()