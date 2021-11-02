import unittest

from core.cuenta import Cuenta


class TestNuevaCuenta(unittest.TestCase):
  # caso exitoso
  # descripcion : el id dado no se encuentra registrado para un usuario existente por lo tanto permite e registro de la nueva cuenta
  # resultado esperado : notifica(registro exitoso)
  def test_registrar_nueva_cuenta_id_no_registrado(self):
    cuenta_usuario = Cuenta("1017252721", "juan", "morales", "jr_m@outlook.es", "3013062071" , "1997/09/05")
    self.assertEqual(Cuenta.registrarCuenta(Cuenta, cuenta_usuario), "registro exitoso")

  # caso exitoso
  # descripcion : el id dado se encuentra registrado para un usuario existente
  # resultado esperado : notifica(el id ya fue registrado para otra cuenta)
  def test_registrar_nueva_cuenta_id_registrado(self):
    cuenta_usuario = Cuenta("1017252721", "juan", "morales", "jr_m@outlook.es", "3013062071" , "1997/09/05")
    self.assertEqual(Cuenta.registrarCuenta(Cuenta, cuenta_usuario), "el id ya fue registrado para otra cuenta")

  

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)