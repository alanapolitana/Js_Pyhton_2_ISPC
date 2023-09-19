""" 6.1. Ejercicio práctico de Herencia
Crear la clase Triciclomotor que herede de la clase Motovehículo y le añada el atributo de capacidad de carga y características especiales.

Le dejamos la solución del ejercicio dado, pero se les recomienda intentar varias veces hasta que salga la solución antes de ver la misma
 """

class Construccion:

  def __init__(self, nombre, metros2, pisos, altura):
    self.nombre = nombre
    self.metros2 = metros2
    self.pisos = pisos
    self.altura = altura

  def __str__(self):
    return self.nombre + " posee " + self.metros2 + " metros cuadrados y tiene " + self.pisos + " pisos. Además su altura es de " + self.altura + "m.\n"

  
class Institucion_Educativa(Construccion):

  def __init__(self, nombre, metros2, pisos, altura, alumnos, aulas, cantinas, bibliotecas):
    Construccion.__init__(self, nombre, metros2, pisos, altura)
    self.alumnos = alumnos
    self.aulas = aulas
    self.cantinas = cantinas
    self.bibliotecas = bibliotecas

  def __str__(self):
    return Construccion.__str__(self) + "Esta institución educativa alberga " + self.alumnos + " estudiantes los cuales estan distribuidos en " + self.aulas + " aulas y tienen a su disposición " + self.cantinas + " cantina/s y " + self.bibliotecas + " biblioteca/s.\n"
  

colegio_san_herrera = Institucion_Educativa("San Herrer", "6167", "2", "9", "1120", "20", "2", "1")
empire_state = Construccion("Empire State", "8094", "102", "443,5")

print(colegio_san_herrera)

print(empire_state)