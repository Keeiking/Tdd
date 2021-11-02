import testVerificarIdcuenta as t
global lst_cuentas_usuario 
lst_cuentas_usuario =[]

class Cuenta():
    # Metodo constructor 
    # Permite crear nuevas instancias de cuentas de usuario
    def __init__(self, id,nombre, apellido, telefono, email ,fechaNacimiento ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.email = email

    # funcionalidad para crear un nuevo usuario
    def registrarCuenta(self, cuenta):
        # si el usuario esta registrado no permite la creacion de un nuevo usuario con el mismo id 
        if self.verificarIdUsuario(cuenta.id) == True:
            return ("el id ya fue registrado para otra cuenta")

        # se crea el usuario y se agrega a la lista
        #cuenta_usuario = Cuenta(id,nombre,apellido,edad,email,contrasena) 
        lst_cuentas_usuario.append(cuenta) 
        return ("registro exitoso")

    # Metodo para la Funcionalidad de verificar si un usuario con un id dado existe
    # si existe algún usuario registrado con el id dado retorna verdadero
    # de lo contrario retorna falso
    def verificarIdUsuario(id):    
        for usuario in lst_cuentas_usuario:
            if (usuario.id == id):  
                return True
        return False
