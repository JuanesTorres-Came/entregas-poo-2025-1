class Mascota:
    def __init__(self, nombre, raza, edad, tamaño, color):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.color = color


    def comer (self):
        print(f"{self.nombre} de raza {self.raza} come 10k de purina")
        
    def caminar (self):
        print(f"{self.nombre} camino 10 kilometros por la granja")


class Perro (Mascota):
    def __init__(self, nombre, raza, genero):
        super().__init__(nombre, raza)
        self.genero = genero
    def Genero(self):
        print(f"el genero del perro es:{self.genero}")
    
    
    
    
    
nombre = input("ingrese el nombre de la mascota: ")
raza = input("ingrese la raza de la mascota: ")
edad = input("ingrese la edad de la mascota: ")
tamaño = input("ingrese el tamaño de la mascota: ")
color = input("ingrese el color de la mascota: ")
genero = input("Ingrese el genero del perro")


mi_mascota = Mascota(nombre, raza, edad, tamaño, color)
mi_perro = Perro(nombre, raza, genero)

mi_mascota.comer()
mi_mascota.caminar()
mi_perro.Genero()
        