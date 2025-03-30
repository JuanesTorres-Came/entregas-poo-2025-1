import Mascotas1
import datetime

class Mascota:
    def __init__(self, clase, nombre, edad, raza, fecha_ingreso):
        self.clase = clase
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = fecha_ingreso
        
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
def main ():
    nmascotas = int(input("cuantas mascotas va a ingresar?: "))
    # Se pide el numero de mascotas que quiera ingresar el usuario
    mascotas = []
    # Se pide los datos para n mascotas
    for i in range(nmascotas):
        print(f"mascota {i+1}:")
                       
if __name__ == "__main__":
    main()
                

    