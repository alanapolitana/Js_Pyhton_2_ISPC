from logging import exception
from pedido import * 
from producto import *


#############     AQUÍ CONSTRUYAN UN MENÚ DE OPCIONES     ++++++++++++++++++++++++


p1 = Producto(1, "producto 1", 5)
p2 = Producto(2, "producto 2", 15)
p3 = Producto(3, "producto 3", 25)

pedido = Pedido()

try:
    pedido.añadir_producto(p1,9)
    pedido.añadir_producto(p2,5)
    pedido.añadir_producto(p3,14)

    print ('El total del pedido es: '+str(pedido.total_pedido()))

    pedido.mostrar_producto()

    pedido.eliminar_producto(p2)

    pedido.mostrar_producto()

except Exception as e:
    print(e)



















