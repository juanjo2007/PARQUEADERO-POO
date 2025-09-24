class Propietario: 
    def __init__(self, codigo_propietario, nombre_propietario, telefono_propietario, correo_propietario):
        self.codigo_propietario = codigo_propietario
        self.nombre_propietario = nombre_propietario
        self.telefono_propietario = telefono_propietario
        self.correo_propietario = correo_propietario
        
    def visualizar_propietario(self):  # >>> Visualiza los datos del propietario
        print("Id_propietario: %s" % (self.codigo_propietario)) 
        print("Nombre_propietario: %s" % (self.nombre_propietario))
        print("Telefono_propietario: %s" % (self.telefono_propietario))
        print("Correo_propietario: %s" % (self.correo_propietario))