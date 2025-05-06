import unittest
from matriz import Matriz

class TestSumaMatriz(unittest.TestCase):
    def test_suma_basica(self):
        A = Matriz([[1, 2], [3, 4]])
        B = Matriz([[5, 6], [7, 8]])
        resultado = A + B
        esperado = [[6.0, 8.0], [10.0, 12.0]]
        self.assertEqual(resultado.valores, esperado)

if __name__ == "__main__":
    unittest.main()