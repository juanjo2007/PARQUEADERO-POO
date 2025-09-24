class Parqueo:
    def __init__(self, codigo_parqueo, fecha, placa, marca, color, codigo_propietario, nombre_propietario, hora_ingreso):
        self.codigo_parqueo = codigo_parqueo
        self.fecha = fecha
        self.placa = placa
        self.marca = marca
        self.color = color
        self.codigo_propietario = codigo_propietario
        self.nombre_propietario = nombre_propietario
        self.hora_ingreso = hora_ingreso
        self.estado = "Activo"

        # Inicializamos con valores vacíos
        self.hora_salida = ""      # vacío al inicio
        self.valor_pagar = 0.0     # sin pago al inicio



    def visualizar_parqueo(self):
        print("===== DETALLE DEL PARQUEO =====")
        print(f"ID Parqueo: {self.codigo_parqueo}")
        print(f"Fecha: {self.fecha}")
        print(f"Placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Codigo Propietario: {self.codigo_propietario}")
        print(f"Nombre Propietario: {self.nombre_propietario}")
        print(f"Hora Ingreso: {self.hora_ingreso}")

        # Usar self (no parqueo)
        if self.hora_salida != "":  
            print(f"Hora Salida: {self.hora_salida}")
            print(f"Valor a Pagar: {self.valor_pagar}")

        print(f"Estado: {self.estado}")