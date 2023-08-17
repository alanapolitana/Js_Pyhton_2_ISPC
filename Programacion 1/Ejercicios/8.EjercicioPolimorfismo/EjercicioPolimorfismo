""" 8.1. Ejercicio práctico de Polimorfismo
En este simple, pero claro ejemplo, veremos como el polimorfismo puede brindarnos la posibilidad de tomar más de una forma una función:

Crear la función "Desplazamiento" y utilizarla para desplazarse en tres tipos de vehículos diferentes.

 """
 
# La técnica de polimorfismo de la POO significa la capacidad de
# tomar más de una forma.
# Una operación puede presentar diferentes comportamientos en
# diferentes instancias.
# El comportamiento depende de los tipos de datos utilizados
# en la operación.
# El polimorfismo es ampliamente utilizado en la aplicación de la herencia.

#se aplica cuando tenemos varias clases con el mismo método
from winsound import MB_ICONQUESTION


class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
        
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")
        
class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
        
#instancio

miVehiculo = Coche()

desplazamientoVehiculo (miVehiculo)