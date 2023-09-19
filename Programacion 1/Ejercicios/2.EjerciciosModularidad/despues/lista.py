from producto import Producto
from pedido import Pedido
""" permite al usuario elegir productos de una lista de productos disponibles y crea un pedido en base a esas selecciones
 """
"""  En este paso, estamos creando una lista llamada productos_disponibles que contiene objetos de la clase Producto. Cada objeto representa un producto con un código, un nombre y un precio. Puedes agregar más productos a esta lista si lo deseas. """
 # Crear una lista de productos disponibles
productos_disponibles = [
    Producto(1, "Batman", 5),
    Producto(2, "Avengers", 15),
    Producto(3, "Joker", 25),
    # Agregar más productos aquí si es necesario
]
""" En este paso, estamos mostrando al usuario la lista de productos disponibles. Iteramos a través de la lista productos_disponibles y utilizamos el método get_Codigo(), get_Nombre(), y get_Precio() de cada objeto Producto para mostrar el código, nombre y precio de cada producto en un formato legible. """
# Mostrar los productos disponibles al usuario
print("Productos disponibles:")
for producto in productos_disponibles:
    print(f"{producto.get_Codigo()}. {producto.get_Nombre()} - ${producto.get_Precio()}")

""" Aquí, creamos un objeto de la clase Pedido llamado pedido. Este objeto representará el pedido del usuario. """
# Crear un pedido vacío
pedido = Pedido()


""" En este paso, comenzamos un bucle while que permite al usuario seleccionar productos para comprar. Usamos input para obtener el código del producto y la cantidad que el usuario desea comprar. Si el usuario ingresa 0 como código de producto, salimos del bucle, lo que indica que el usuario ha terminado de seleccionar productos. """
# Permitir al usuario elegir productos
while True:
    try:
        codigo_producto = int(input("Ingrese el código del producto que desea comprar (0 para finalizar): "))
        if codigo_producto == 0:
            break  # Finalizar la selección de productos
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))

        """ Aquí buscamos el producto seleccionado por el código ingresado por el usuario en la lista de productos_disponibles. Si encontramos el producto, lo asignamos a producto_seleccionado y luego lo agregamos al pedido utilizando el método añadir_producto() del objeto pedido. Si el producto no se encuentra, mostramos un mensaje de error. """
        # Buscar el producto por código
        producto_seleccionado = None
        for producto in productos_disponibles:
            if producto.get_Codigo() == codigo_producto:
                producto_seleccionado = producto
                break

        if producto_seleccionado is not None:
            pedido.añadir_producto(producto_seleccionado, cantidad)
        else:
            print("Producto no encontrado. Intente nuevamente.")

    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")

# Una vez que el usuario ha terminado de seleccionar productos, mostrar el resumen del pedido y calcular el total.
pedido.mostrar_producto()
print('El total del pedido es: ' + str(pedido.total_pedido()))
""" Finalmente, después de que el usuario haya terminado de seleccionar productos, mostramos el resumen del pedido utilizando el método mostrar_producto() del objeto pedido. Luego, calculamos y mostramos el total del pedido utilizando el método total_pedido() del objeto pedido. """