""" El código que proporcionaste parece estar bien estructurado y funciona para crear objetos de la clase Producto y Pedido, agregar productos al pedido, realizar una validación para asegurarse de que haya al menos dos productos en el pedido antes de mostrarlos y calcular el total del pedido """

from producto import Producto
from pedido import Pedido
""" Se crean tres objetos de la clase Producto (p1, p2 y p3) que representan tres productos diferentes con sus códigos, nombres y precios. """

p1 = Producto(1, "Batman", 5)
p2 = Producto(2, "Avengers", 15)
p3 = Producto(3, "Jocker", 25)

""" Se crea un objeto de la clase Pedido llamado pedido. """
pedido = Pedido()
""" Se añaden productos al pedido (p1, p2 y p3) junto con sus respectivas cantidades. """
try:
    pedido.añadir_producto(p1, 9)
    pedido.añadir_producto(p2, 5)
    pedido.añadir_producto(p3, 14)

    """   Se realiza una validación para verificar que haya al menos dos productos en el pedido antes de mostrarlos. """
    # Validación: Corroborar que al menos dos productos se agreguen al pedido
    if len(pedido.productos) < 2:
        raise Exception('Debe agregar al menos dos productos al pedido')
 
    """ Se muestra la lista de productos en el pedido junto con sus cantidades utilizando el método mostrar_producto(). """
    pedido.mostrar_producto()
    
    """ Se elimina un producto del pedido (en este caso, p2). """
    pedido.eliminar_producto(p2)

    """ Se elimina un producto del pedido (en este caso, p2). """
    #pedido.mostrar_producto()
    print('El total del pedido es: ' + str(pedido.total_pedido()))
except Exception as e:
    print(e)
    """ Si en algún momento se lanza una excepción, se captura y se imprime un mensaje de error. """
    


""" Este código parece estar funcionando correctamente para gestionar un pedido de productos. Si ejecutas este código y no se lanzan excepciones, deberías ver la lista de productos en el pedido junto con sus cantidades y el total del pedido al final. """



















