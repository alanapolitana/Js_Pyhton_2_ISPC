""" 3.1. Ejercicio práctico de clases
Crear un programa que permita crear la clase Motovechiculo, capaz de procesar la información básica de las motos en un concesionario llamado "Córdoba Motos", para ello vamos a suponer que los atributos de una moto son:

•Marca

•Modelo

•Patente

•kilometraje

Se deberá poder ingresar dichos datos y ser mostrados por consola.



Le dejamos la solución del ejercicio dado, pero se les recomienda intentar varias veces hasta que salga la solución antes de ver la misma. """


class Moto: 
    Marca = ""
    Modelo = ""
    Patente= ""
    Kilometraje= 0

    def __init__(self, marca, modelo, patente, kilometraje ):
        self.Marca = marca
        self.Modelo= modelo
        self.Patente= patente
        self.Kilometraje= kilometraje

    def get_Marca(self):
        return self.Marca

    def set_Marca(self, marca):
        self.Marca = marca 
    
    def get_Modelo(self):
        return self.Modelo

    def set_Modelo(self, modelo):
        self.Modelo = modelo

    def get_Patente(self):
        return self.Patente

    def set_Patente(self, patente):
        self.Patente = patente

    def get_Kilometraje(self):
        return self.Kilometraje

    def set_Kilometraje(self, kilometraje):
        self.Kilometraje = kilometraje

    def __str__(self):
        return ('La marca de la moto es: ' + self.Marca + ' modelo: ' + self.Modelo + ' su patente es: ' + self.Patente + ' y el kilometraje es: ' + str(self.Kilometraje))

      

marca= input('Ingrese la marca de la moto.')
modelo= input('Ingrese el modelo de la moto.')
patente= input('Ingrese la patente de la moto.')
kilometraje= input('Ingrese el kilometraje de la moto.')

miMoto= Moto(marca,modelo,patente,kilometraje)

print(str(miMoto))
