from datetime import datetime


class Parqueo:
    def __init__(self, id_parqueo, fecha, placa, marca, color, id_propietario, nombre_propietario, hora_ingreso, hora_salida=None, valor_pagar=0.0, estado="Parqueado"):
        self.id_parqueo = id_parqueo
        self.fecha = fecha
        self.placa = placa
        self.marca = marca
        self.color = color
        self.id_propietario = id_propietario
        self.nombre_propietario = nombre_propietario
        self.hora_ingreso = hora_ingreso
        self.hora_salida = hora_salida
        self.valor_pagar = valor_pagar
        self.estado = estado  # "Parqueado" o "Finalizado"


    def visualizar_parqueo(self):
        print("===== DETALLE DEL PARQUEO =====")
        print(f"ID Parqueo: {self.id_parqueo}")
        print(f"Fecha: {self.fecha}")
        print(f"Placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"ID Propietario: {self.id_propietario}")
        print(f"Nombre Propietario: {self.nombre_propietario}")
        print(f"Hora Ingreso: {self.hora_ingreso}")
        if self.hora_salida:
            print(f"Hora Salida: {self.hora_salida}")
            print(f"Valor a Pagar: {self.valor_pagar}")
        print(f"Estado: {self.estado}")
