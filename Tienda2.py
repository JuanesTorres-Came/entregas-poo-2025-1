"""
Título de práctica: Tienda 2

Autor: Juan Torres <jetorress@academia.usbbog.edu.co>
Fecha: 07/03/2025
"""

class Producto:
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion
    
    
    def obtener_datos (self):
         # Organiza o pone los datos del producto en forma de lista
        return [
                f"{self.nombre}",
                f"{self.precio} pesos",
                f"{self.cantidad} unidades",
                f"{self.descripcion}",
                f"{self.clasificacion}"]
            

def ingresar_producto():
    #los datos que ingresara el cliente
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input(f"El precio de {nombre} es: "))
    cantidad = int(input(f"la cantidad de {nombre} es: "))
    descripcion = input(f"La descripcion de {nombre} es: ")
    clasificacion = input(f"La clasificacion de {nombre} es: ")
    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def mostrar_productos(productos):
    #encabezado de la tabla ("titulos")
    encabezado = ["nombre","precio","cantidad","descripcion","clasificacion"]
    print ("Productos ingresados con sus datos:")
    print (
        f"{encabezado[0]:<15} {encabezado[1]:<20} {encabezado[2]:<15}"
        f"{encabezado[3]:<20} {encabezado[4]:<30}")
    #se muestran los productos en forma de tabla
        
        
    for producto in productos:
        (
            nombre, precio, cantidad,
            descripcion, clasificacion
        )= producto.obtener_datos()
        print(
            f"{nombre:<15}" f"{precio:<20}" f"{cantidad:<15}"
            f"{descripcion:<20}" f"{clasificacion:<30}"
        )


def mostrar_productos_juntos(productos):
    #suma de productos por clasificacion
    clasificaciones= {}
    for producto in productos:
        if producto.clasificacion in clasificaciones:
                clasificaciones[producto.clasificacion] += producto.precio
        else:
                clasificaciones[producto.clasificacion] = producto.precio
    print("\nsuma de precios clasificacion:")
    print(f"{'Clasificación':<20} {'Precio Total':<15}")
    for clasificacion, precio_total in clasificaciones.items():
        print(f"{clasificacion:<20} {precio_total:<5}pesos")
        
        
def main():
    nproductos = int(input("cuantos productos va a ingresar?: "))
    # Se pide el numero de productos que quiera ingresar el usuario
    productos = []
    # Se pide los datos para n productos
    for i in range(nproductos):
        print(f"Producto {i+1}:")
        producto = ingresar_producto()
        productos.append(producto)
    # Se muestran los productos que se ingresaron en formato de tabla
    mostrar_productos(productos)
    mostrar_productos_juntos(productos)

            
if __name__ == "__main__":
    main()
