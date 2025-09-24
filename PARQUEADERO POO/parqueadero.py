from datetime import datetime

class Parqueadero:
    def __init__(self):
        self.propietarios = []
        self.vehiculos = []
        self.parqueos = []
        self.espacios_totales = 10     # Según enunciado
        self.espacios_disponibles = 10
        self.total_ingresos = 0.0

    # =================================================== PROPIETARIOS ===================================================
    def adicionar_propietario(self, propietario):
        if propietario.codigo_propietario == "":
            print("Error: El ID del propietario no puede estar vacío.")
            return False
        if self.buscar_propietario(propietario.codigo_propietario) != -1:
            print("Error: Ya existe un propietario con ese ID.")
            return False
        self.propietarios.append(propietario)
        print("Propietario registrado satisfactoriamente.")
        return True

    def buscar_propietario(self, codigo_propietario):
        for i, p in enumerate(self.propietarios):
            if p.codigo_propietario == codigo_propietario:
                return i
        return -1

    def listar_propietarios(self):
        if not self.propietarios:
            print("No hay propietarios registrados.")
        else:
            for p in self.propietarios:
                print(f"ID: {p.codigo_propietario} | Nombre: {p.nombre_propietario}")

    # =================================================== VEHÍCULOS =====================================================
    def adicionar_vehiculo(self, vehiculo):
        if vehiculo.placa == "":
            print("Error: La placa no puede estar vacía.")
            return False
        if self.buscar_vehiculo(vehiculo.placa) != -1:
            print("Error: Ya existe un vehículo con esa placa.")
            return False
        if self.buscar_propietario(vehiculo.codigo_propietario) == -1:
            print("Error: No existe un propietario con ese ID.")
            return False
        self.vehiculos.append(vehiculo)
        print("Vehículo registrado satisfactoriamente.")
        return True

    def buscar_vehiculo(self, placa):
        for i, v in enumerate(self.vehiculos):
            if v.placa == placa:
                return i
        return -1

    def listar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        else:
            for v in self.vehiculos:
                print(f"Placa: {v.placa} | Propietario: {v.codigo_propietario}")

    # =================================================== PARQUEOS ======================================================
    def adicionar_parqueo(self, parqueo):
        if self.buscar_parqueo(parqueo.codigo_parqueo) != -1:
            print("Error: Ya existe un parqueo con ese ID.")
            return False
        if self.buscar_vehiculo(parqueo.placa) == -1:
            print("Error: No existe un vehículo con esa placa.")
            return False
        if self.buscar_propietario(parqueo.codigo_propietario) == -1:
            print("Error: No existe un propietario con ese ID.")
            return False
        if self.espacios_disponibles <= 0:
            print("Error: No hay espacios disponibles.")
            return False

        self.parqueos.append(parqueo)
        self.espacios_disponibles -= 1
        print("Parqueo registrado satisfactoriamente.")
        return True

    def buscar_parqueo(self, codigo_parqueo):
        for i, p in enumerate(self.parqueos):
            if p.codigo_parqueo == codigo_parqueo:
                return i
        return -1
    
    def buscar_parqueo_por_placa(self, placa):
        for parqueo in self.parqueos:
            if parqueo.placa == placa and parqueo.estado == "Activo":
                return parqueo
        return None



    def buscar_parqueo_activo_por_placa(self, placa):
        # Busca solamente parqueos activos
        for i, p in enumerate(self.parqueos):
            if p.placa == placa and p.estado == "Activo":
                return i
        return -1



    def listar_parqueos(self):
        activos = [p for p in self.parqueos if p.estado == "Activo"]
        if not activos:
            print("No hay vehículos parqueados.")
        else:
            for p in activos:
                print(f"ID: {p.id_parqueo} | Placa: {p.placa} | Ingreso: {p.hora_ingreso}")

    def registrar_salida(self, placa, hora_salida):
        for p in self.parqueos:
            if p.placa == placa and p.estado == "Activo":
                try:
                    hora_s = datetime.strptime(hora_salida, "%H:%M:%S")
                    hora_i = datetime.strptime(p.hora_ingreso, "%H:%M:%S")
                    if hora_s <= hora_i:
                        print("Error - La hora de salida no es válida.")
                        return False
                except ValueError:
                    print("Error - Formato de hora incorrecto (HH:MM:SS).")
                    return False

                # Calcular valor a pagar ($2800 la hora o fracción)
                delta = hora_s - hora_i
                horas = delta.total_seconds() / 3600
                valor = int((horas if horas.is_integer() else int(horas) + 1) * 2800)

                p.hora_salida = hora_salida
                p.valor_pagar = valor
                p.estado = "Finalizado"

                self.espacios_disponibles += 1
                self.total_ingresos += valor

                print(f"Salida registrada. Valor a pagar: ${valor}")
                return True
        print("Error - No se encontró un parqueo activo con esa placa.")
        return False
    
    def modificar_parqueo(self, id_parqueo, nueva_placa, nuevo_color, nuevo_id_propietario):
        # Buscar parqueo por ID
        pos_parqueo = self.buscar_parqueo(id_parqueo)
        if pos_parqueo == -1:
            print("Error - No existe un parqueo con ese ID.")
            return False

        parqueo = self.parqueos[pos_parqueo]

        # Verificar que el vehículo exista
        pos_vehiculo = self.buscar_vehiculo(nueva_placa)
        if pos_vehiculo == -1:
            print("Error - No existe un vehículo con esa placa.")
            return False
        vehiculo = self.vehiculos[pos_vehiculo]

        # Verificar que el propietario exista
        pos_propietario = self.buscar_propietario(nuevo_id_propietario)
        if pos_propietario == -1:
            print("Error - No existe un propietario con ese ID.")
            return False
        propietario = self.propietarios[pos_propietario]

        # Modificar atributos del parqueo (excepto el ID)
        parqueo.placa = vehiculo.placa
        parqueo.marca = vehiculo.marca
        parqueo.color = nuevo_color   # color lo das tú manualmente
        parqueo.id_propietario = propietario.codigo_propietario
        parqueo.nombre_propietario = propietario.nombre_propietario

        print("Parqueo actualizado correctamente.")
        return True
    
    def eliminar_parqueo(self, codigo_parqueo):
        pos = self.buscar_parqueo(codigo_parqueo)
        if pos == -1:
            return False

        parqueo = self.parqueos[pos]

        # Si el parqueo está activo, liberar espacio
        if parqueo.estado == "Activo":
            self.espacios_disponibles += 1

        # Eliminar de la lista
        del self.parqueos[pos]

        return True
    # =================================================== REPORTES============================================
    def visualizar_espacios_ocupados(self):
        """
        Retorna la cantidad de espacios ocupados en el parqueadero.
        """
        ocupados = self.espacios_totales - self.espacios_disponibles
        return ocupados
    
    def visualizar_espacios_disponibles(self):
        """
        Retorna la cantidad de espacios disponibles en el parqueadero.
        """
        return self.espacios_disponibles


    def reporte_espacios_disponibles(self):
        """
        Retorna la cantidad de espacios disponibles para parqueo.
        """
        return self.espacios_disponibles

    def reporte_vehiculos_parqueados(self):
        """
        Retorna la cantidad de vehículos que actualmente están parqueados (estado activo).
        """
        cantidad = len([p for p in self.parqueos if p.estado == "Activo"])
        return cantidad

    def reporte_ingresos(self):
        """
        Retorna el total de ingresos generados por el parqueadero.
        """
        return self.total_ingresos
