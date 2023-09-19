""" La clase Producto representa un producto con atributos como código, nombre y precio, y también incluye métodos para obtener y establecer estos atributos, además de un método para calcular el precio total de un número determinado de unidades del producto. """
""" Atributos de la clase Producto:

Codigo: Almacena el código del producto. Inicializado a 0 por defecto.
Nombre: Almacena el nombre del producto. Inicializado como una cadena vacía por defecto.
Precio: Almacena el precio del producto. Inicializado a 0 por defecto. """
class Producto: 
    Codigo = 0
    Nombre = ""
    Precio= 0
    """ Método __init__(self, codigo, nombre, precio):
Este es el constructor de la clase Producto. Se llama automáticamente cuando se crea una instancia de la clase Producto. Recibe tres parámetros: codigo, nombre y precio. Estos parámetros se utilizan para inicializar los atributos Codigo, Nombre y Precio del objeto Producto. """
    def __init__(self, codigo, nombre, precio):
        self.Codigo = codigo
        self.Nombre= nombre
        self.Precio= precio


    """ Métodos get y set:
Hay métodos get y set para cada uno de los atributos (Codigo, Nombre, Precio) que te permiten obtener y establecer estos valores. Por ejemplo, get_Codigo devuelve el código del producto, set_Codigo establece el código del producto, y así sucesivamente. Estos métodos son una convención en Python para controlar el acceso a los atributos de la clase y permitir la encapsulación. """
    def get_Codigo(self):
        return self.Codigo

    def set_Codigo(self, codigo):
        self.Codigo = codigo 
    
    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self, nombre):
        self.Nombre = nombre

    def get_Precio(self):
        return self.Precio

    def set_Precio(self, precio):
        self.Precio = precio

    """ Método __str__(self):
Este método proporciona una representación de cadena (string) del objeto Producto. Devuelve una cadena que incluye el código, el nombre y el precio del producto en un formato legible. """
    def __str__(self):
        return ('El código del producto es:' + str(self.Codigo) + ' su nombre es:' + str(self.Nombre) + 'El precio del producto es: '+ str(self.Precio) )
    """ Método calcular_total(self, unidades):
Este método toma la cantidad de unidades del producto como parámetro (unidades) y calcula el precio total multiplicando el precio del producto por la cantidad de unidades. Luego, devuelve el resultado. """
    def calcular_total(self,unidades):
        return (self.Precio * unidades)
    
    """ En resumen, la clase Producto proporciona una estructura para crear objetos que representan productos con información como código, nombre y precio, y ofrece métodos para interactuar con estos atributos. Esta clase es útil cuando necesitas representar productos en un sistema de gestión de pedidos o inventario, por ejemplo. """