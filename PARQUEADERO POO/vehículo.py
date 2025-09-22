class Vehiculo:
    def __init__(self, placa, marca, modelo, color, id_propietario, nombre_propietario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.id_propietario = id_propietario
        self.nombre_propietario = nombre_propietario

    def visualizar_vehiculo(self):
        print("===== DETALLE DEL VEHÍCULO =====")
        print(f"Placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"ID Propietario: {self.id_propietario}")
        print(f"Nombre Propietario: {self.nombre_propietario}")
