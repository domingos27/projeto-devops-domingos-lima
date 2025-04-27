import unittest

# Supondo que você tenha uma função para somar dois números
def somar(a, b):
    return a + b

# E uma função para subtrair dois números
def subtrair(a, b):
    return a - b

class TesteFuncoes(unittest.TestCase):

    def test_somar(self):
        # Corrigido: soma de 1 + 4 deve ser 5, e não 7
        self.assertEqual(somar(1, 4), 5)  # Corrigido de 7 para 5
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)
        self.assertEqual(subtrair(-1, -1), 0)

    # Teste com uma operação com números negativos
    def test_somar_negativos(self):
        self.assertEqual(somar(-5, -3), -8)

    # Teste com números flutuantes
    def test_somar_float(self):
        self.assertEqual(somar(2.5, 3.5), 6.0)

    # Teste de subtração com valores negativos
    def test_subtrair_negativos(self):
        self.assertEqual(subtrair(-2, -2), 0)

if __name__ == "__main__":
    unittest.main()
