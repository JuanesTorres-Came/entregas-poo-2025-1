"""
Título de práctica: Mascotas 1

Autor: Juan Torres <jetorress@academia.usbbog.edu.co>
Fecha: 30/03/2025
"""
import datetime
class Mascota:
    def __init__(self, clase, nombre, edad, raza, fecha_ingreso):
        self.clase = clase
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = fecha_ingreso
        
    def obtener_datos (self):
        #organiza los datos de Mascota en forma de lista
        return [
                f"{self.clase}",
                f"{self.nombre}",
                f"{self.edad}",
                f"{self.raza}", 
                f"{self.fecha_ingreso.strftime('%Y-%m-%d')}"]
class Perro(Mascota):
    pass
class Gato(Mascota):
    pass
def ingresar_mascotas():
        #los datos que ingresara el cliente
    while True:
        clase = input ("ingrese la clase de la mascota: ")
        if clase == "perro" or clase == "gato":
            print("es valida esta clase")
            nombre = input("Ingrese el nombre de la mascota: ")
            edad = int(input(f"La edad de {nombre} es: "))
            raza = input(f"la raza de {nombre} es: ")
            fecha_ingreso = datetime.date.today()
            return Mascota(clase, nombre, edad, raza, fecha_ingreso)
        else:
            print("La clase no es valida, intente de nuevo")
    
        
    
def mostrar_mascotas(mascotas):
        #encabezado de la tabla ("titulos")
    encabezado = ["clase","nombre","edad","raza", "fecha_ingreso"]
    print ("Mascotas ingresadas con sus datos:")
    print (
        #se muestran los productos en forma de tabla
        f"{encabezado[0]:<20} {encabezado[1]:<20} {encabezado[2]:15}"
        f"{encabezado[3]:<20} {encabezado[4]:<20}")
            
        
    for mascota in mascotas:
        (
        clase, nombre, edad, raza, fecha_ingreso
        )= mascota.obtener_datos()
        print(
            f"{clase:<20}" f"{nombre:<20}" f"{edad:<15}" 
            f"{raza:<20}"  f"{fecha_ingreso:<20}"
                
            )
def main():
    nmascotas = int(input("cuantas mascotas va a ingresar?: "))
    # Se pide el numero de mascotas que quiera ingresar el usuario
    mascotas = []
    # Se pide los datos para n mascotas
    for i in range(nmascotas):
        print(f"mascota {i+1}:")
        mascota= ingresar_mascotas()
        mascotas.append(mascota)
    # Se muestran los productos que se ingresaron en formato de tabla
    mostrar_mascotas(mascotas)
    
    
                
if __name__ == "__main__":
    main()
        