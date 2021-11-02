import unittest

from core import cuenta


class TestVerificarIdCuenta(unittest.TestCase):

    # caso exitoso
    # descripcion : el id dado se encuentra registrado para una cuenta de usuario existente
    # resultado esperado : retorna verdadero
    def test_verificar_Id_cuenta_existe(self):
        cuenta_usuario = cuenta.Cuenta("2", "john", "frusciante", "frusciante@outlook.es", "3013062072" , "1992/07/09")
        cuenta.lst_cuentas_usuario.append(cuenta_usuario)
        self.assertEqual(cuenta.Cuenta.verificarIdUsuario("2"),True)
 
    # caso alternativo
    # descripcion : el id no se encuentra registrado para ninguna cuenta de usuario existente
    # resultado esperado : retorna falso
    def test_Verificar_Id_cuenta_no_existe(self):
        self.assertEqual(cuenta.Cuenta.verificarIdUsuario("4"),False)

   

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)