import unittest

from core import pelicula as p


class TestNuevaPelicula(unittest.TestCase):

    def test_nueva_Pelicula(self): 
        pelicula = p.Pelicula("1", "Bojack", "trata de esto" , "2 horas")
        self.assertIsInstance(pelicula, p.Pelicula)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
