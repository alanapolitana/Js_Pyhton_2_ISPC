from producto import Producto

""" productos y cantidades: Estas son variables de clase que almacenan listas vacías. productos se utilizará para almacenar objetos de la clase Producto, y cantidades se utilizará para almacenar las cantidades correspondientes de esos productos.

El método __init__(self): Este es el constructor de la clase Pedido. Se llama automáticamente cuando se crea una instancia de la clase. En este método, se inicializan las listas self.productos y self.cantidades como listas vacías para cada instancia de pedido. """
class Pedido:

    productos = []
    cantidades = []

    def __init__(self):
        self.productos = []
        self.cantidades = []



    """ El método añadir_producto(self, producto, cantidad): Este método se utiliza para agregar un producto al pedido. Verifica si el objeto producto es una instancia de la clase Producto, si cantidad es un número entero y si es mayor que cero. Luego, comprueba si el producto ya está en la lista de productos (self.productos). Si el producto ya existe, incrementa la cantidad correspondiente en la lista self.cantidades. Si el producto no existe en la lista, agrega el producto y su cantidad a las listas self.productos y self.cantidades. """
    def añadir_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('añadir_producto: producto debe ser de la clase Producto')
        
        if not isinstance(cantidad, int):
            raise Exception('añadir_producto: cantidades debe ser un número')

        if cantidad <=0 :
            raise Exception('añadir_producto: cantidades debe ser número mayor a cero')

        if producto in self.productos : 
            indice = self.productos.index(producto)
            self.cantidades[indice] += cantidad
        else: 
            self.cantidades.append(cantidad)
            self.productos.append(producto)
    
    """ El método eliminar_producto(self, producto): Este método se utiliza para eliminar un producto del pedido. Comprueba si el objeto producto es una instancia de la clase Producto. Luego, verifica si el producto está en la lista de productos (self.productos). Si lo encuentra, elimina el producto y su cantidad correspondiente de las listas self.productos y self.cantidades. Si el producto no existe en la lista, se lanza una excepción indicando que el producto no existe. """
    def eliminar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception('eliminar_producto: producto debe ser de la clase Producto')

        if producto in self.productos:
            indice = self.productos.index(producto)
            del self.productos[indice]
            del self.cantidades[indice] 
        else: 
            raise Exception('eliminar_producto: El producto no existe')
    
    """ El método total_pedido(self): Este método calcula el total del pedido sumando el precio total de cada producto multiplicado por su cantidad correspondiente. Utiliza un bucle for para recorrer las listas self.productos y self.cantidades en paralelo y calcular el total. """
    
    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.productos,self.cantidades):
            total += total + p.calcular_total(c)
        
        return total 
    """ El método mostrar_producto(self): Este método muestra la lista de productos en el pedido junto con sus cantidades. Utiliza un bucle for para recorrer las listas self.productos y self.cantidades en paralelo y muestra la información de cada producto y su cantidad. """
    def mostrar_producto(self): 
        for (p,c) in zip(self.productos,self.cantidades):
            print('Producto:' + p.get_Nombre() + ', Cantidad:' + str(c))