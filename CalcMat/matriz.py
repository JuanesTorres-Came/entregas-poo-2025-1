"""
Título de práctica: Mascotas 1

Autor: Juan Torres <jetorress@academia.usbbog.edu.co>
Fecha: 04/05/2025
"""
class Matriz:
    def __init__(self, valores):
        if len(valores) != 2 or any(len(fila) != 2 for fila in valores):
            raise ValueError("La matriz debe ser 2x2.")
        self.valores = [[float(c) for c in fila] for fila in valores]

    def __add__(self, otra):
        resultado = [
            [self.valores[i][j] + otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __sub__(self, otra):
        resultado = [
            [self.valores[i][j] - otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __matmul__(self, otra):  #operador para la multiplicación de matrices
        resultado = [
            [
                self.valores[i][0] * otra.valores[0][j] + self.valores[i][1] * otra.valores[1][j]
                for j in range(2)
            ]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __str__(self):
        return '\n'.join(['\t'.join([str(num) for num in fila]) for fila in self.valores])


def pedir_matriz(nombre):
    print(f"\nIntroduce los valores para la matriz {nombre} (solo números reales):")
    valores = []
    for i in range(2):
        fila = []
        for j in range(2):
            entrada = input(f"Elemento [{i+1}][{j+1}]: ")
            fila.append(entrada)
        valores.append(fila)
    return Matriz(valores)


def mostrar_menu():
    print("\nQue operación quieres realizar para estas matrices:")
    print("1. Una Suma")
    print("2. Una Resta")
    print("3. Una Multiplicación")
    return input("Opción: ")


def main():
    A = pedir_matriz("A")
    B = pedir_matriz("B")

    opcion = mostrar_menu()

    print("\nResultado:")
    if opcion == '1':
        print(A + B)
    elif opcion == '2':
        print(A - B)
    elif opcion == '3':
        print(A @ B)
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()