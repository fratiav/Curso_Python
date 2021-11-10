#Paquetes distribuibles
#Este archivo va a crear un instalable de paquete para poder acceder a los modulos sea cual sea la ubicacion

from setuptools import setup

setup(
    name="paqueteCalculos",
    version="1.0",
    description="Paquete con modulos de calculo",
    author="Francisco Jose Ratia Vargas",
    author_email="franratvar7@gmail.com",
    url="",
    packages=["Paquetes","Paquetes.Calculos"] #Se especifican las rutas desde este archivo separado por comas
)

#Ahora desde simbolos del sistema encontramos la ubicacion del setup.py y la sentencia: python setup.py
#Despues instalar el rar creado con la orden: pip install "nombre paquete"
#Ya seria accesible el paquete desde cualquier ubicacion

#Para desinstalar el paquete  la orden: pip uninstall "nombre paquete"