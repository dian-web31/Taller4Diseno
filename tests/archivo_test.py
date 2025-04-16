"""
Archivo de prueba para la clase Archivo.
"""
import unittest
import os
from src.services.archivo import Archivo

class TestArchivo(unittest.TestCase):
    """
    Clase de prueba para la clase Archivo.
    """

    def setUp(self):
        # Crear archivo CSV de prueba
        self.test_file = 'test_data.csv'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("1234567,Lulú López,1040,Cálculo\n")
            f.write("9876534,Pepito Pérez,1040,Cálculo\n")
            f.write("4567766,Calvin Clein,1050,Física I\n")
            f.write("1234567,Lulú López,1060,Administración\n")
            f.write("4567766,Calvin Clein,1070,Espíritu Empresarial\n")

        self.archivo = Archivo(self.test_file)

    def tearDown(self):
        # Eliminar el archivo después de la prueba
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_leer_csv(self):
        """
        Pruebas para el metodo leer_csv()
        """
        resultado = self.archivo.leer_csv()
        self.assertEqual(len(resultado), 5)
        self.assertEqual(resultado[0]['nombre'], 'Lulú López')
        self.assertEqual(resultado[0]['codigo_materia'], '1040')
        self.assertEqual(resultado[1]['nombre'], 'Pepito Pérez')
        self.assertEqual(resultado[1]['codigo_materia'], '1040')
        self.assertEqual(resultado[2]['nombre'], 'Calvin Clein')
        self.assertEqual(resultado[2]['codigo_materia'], '1050')

    def test_cuenta_materias(self):
        """"
        Pruebas para el metodo cuenta_materias()
        """
        resultado = self.archivo.cuenta_materias()
        esperado = {'Lulú López': 2, 'Pepito Pérez': 1, 'Calvin Clein': 2}
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
