import unittest
from working import convert

class TestConvertFunction(unittest.TestCase):
    def test_valid_formats(self):
        # Teste para formatos válidos de entrada
        self.assertEqual(convert("9:00 AM to 5:00 PM"), "09:00 to 17:00")
        self.assertEqual(convert("9 AM to 5 PM"), "09:00 to 17:00")
        # Adicione mais casos de teste para formatos válidos

    def test_invalid_formats(self):
        # Teste para formatos inválidos de entrada
        with self.assertRaises(ValueError):
            convert("12:60 AM")  # Minutos inválidos
        with self.assertRaises(ValueError):
            convert("13:00 PM")  # Hora inválida
        with self.assertRaises(ValueError):
            convert("10AM to 3PM")  # Formato inválido
        # Adicione mais casos de teste para formatos inválidos
        with self.assertRaises(ValueError):
            convert("99:99 AM to 99:99 PM")

if __name__ == '__main__':
    unittest.main()
