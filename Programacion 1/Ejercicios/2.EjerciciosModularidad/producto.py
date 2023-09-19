""" class Producto: 
    Codigo = 0
    Nombre = ""
    Precio= 0

    def __init__(self, codigo, nombre, precio):
        self.Codigo = codigo
        self.Nombre= nombre
        self.Precio= precio

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

    def __str__(self):
        return ('El código del producto es:' + str(self.Codigo) + ' su nombre es:' + str(self.Nombre) + 'El precio del producto es: '+ str(self.Precio) )

    def calcular_total(self,unidades):
        return (self.Precio * unidades) """
        
class Producto: 
    Codigo = 0
    Nombre = ""
    Precio = 0

    def __init__(self, codigo, nombre, precio):
        self.Codigo = codigo
        self.Nombre = nombre
        self.Precio = precio
        
        if not isinstance(precio, (int, float)):
            raise Exception('El precio del producto debe ser un número')
        
        if precio <= 0:
            raise Exception('El precio del producto debe ser mayor a cero')

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

    def __str__(self):
        return ('El código del producto es:' + str(self.Codigo) + ' su nombre es:' + str(self.Nombre) + 'El precio del producto es: '+ str(self.Precio) )

    def calcular_total(self, unidades):
        return (self.Precio * unidades)