class Tienda:
    
    def __init__(self, producto, nombre, preciounitario= "2000", cantidad= 10):
        """Constructor de la clase tienda"""
        self.producto = producto 
        self.nombre = nombre
        self.preciounitario = preciounitario
        self.cantidad = cantidad
        
        
    def habla(self):
        """Muestra el mensaje de Tienda"""
        print(f"{self.producto}, cual es el nombre?")
        print(f"{self.nombre}")
        
        if self.nombre == "pan":
            print (f"cual es el precio de {self.nombre}?")
            print (f"{self.preciounitario}COP")
            print (f"que cantidad hay de {self.nombre}?")
            print (f"{self.cantidad} unidades")
        elif self.nombre == "leche":
            print (f"cual es el precio de {self.nombre}?")
            print (f"{self.preciounitario}COP")
            print (f"que cantidad hay de {self.nombre}?")
            print (f"{self.cantidad} unidades")
        elif self.nombre == "huevos":
            print (f"cual es el precio de {self.nombre}?")
            print (f"{self.preciounitario}COP")
            print (f"que cantidad hay de {self.nombre}?")
            print(f"{self.cantidad} unidades")
        else: 
            print ("no se encuetra el producto en la tienda")
def run():
    """solicitar al usuario que ingrese el nombre del producto"""
    nombre_producto = input("escriba el nombre del producto: ")
    
    
    if nombre_producto in ["pan","leche", "huevos"]:
    
        m1 = Tienda("producto", nombre=nombre_producto, preciounitario=2000, cantidad=10)
        m1.habla()
    else:
        print("El producto ingresado no esta disponible en la tienda")

if __name__ == "__main__":
    run()
        
    
        
    