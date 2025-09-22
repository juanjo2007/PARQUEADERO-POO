from datetime import datetime
class Parqueadero:
    def __init__(self):
        # Aquí inicializamos las listas principales
        self.propietarios = []
        self.vehiculos = []
        self.parqueos = []
        self.espacios_totales = 50   # ejemplo: el parqueadero tiene 50 espacios
        self.espacios_ocupados = 0
        self.pagos_recibidos = 0.0
# >>> =================================================== Propietario =====================================================
# >>> Método Adicionar (Registrar) Propietario ====================================================================
    def adicionar_propietario(self, propietario):
        # >>> Validación de campos vacíos
        if propietario.codigo_propietario == "":
            print("Error: El ID del propietario no puede estar vacío.")
            return False
        if propietario.nombre_propietario == "":
            print("Error: El nombre del propietario no puede estar vacío.")
            return False
        if propietario.telefono_propietario == "":
            print("Error: El teléfono del propietario no puede estar vacío.")
            return False
        if propietario.correo_propietario == "":
            print("Error: El correo electrónico del propietario no puede estar vacío.")
            return False

        # >>> Validación de código (numérico y no negativo)
        try:
            codigo = int(propietario.codigo_propietario)
            if codigo < 0:
                print("Error: El ID del propietario no puede ser negativo.")
                return False
        except ValueError:
            print("Error: El ID del propietario debe ser numérico.")
            return False

        # >>> Validación de teléfono (numérico, no negativo, exactamente 10 dígitos)
        try:
            telefono = int(propietario.telefono_propietario)
            if telefono < 0:
                print("Error: El teléfono no puede ser negativo.")
                return False
            if len(str(telefono)) != 10:
                print("Error: El teléfono debe tener exactamente 10 dígitos.")
                return False
        except ValueError:
            print("Error: El teléfono debe ser numérico.")
            return False

        # >>> Validar correo básico (contenga @ y .)
        if "@" not in propietario.correo_propietario or "." not in propietario.correo_propietario:
            print("Error: El correo electrónico no es válido.")
            return False

        # >>> Verificar que el ID no esté repetido
        if self.buscar_propietario(propietario.codigo_propietario) == -1:
            self.propietarios.append(propietario)
            return True

        print("Error: Ya existe un propietario con ese ID.")
        return False

    # >>> Método Buscar Propietario ====================================================================
    def buscar_propietario(self, codigo_propietario):
        for i in range(len(self.propietarios)):
            if codigo_propietario == self.propietarios[i].codigo_propietario:
                return i
        return -1
    # >>> Método Modificar Propietario ====================================================================
    def modificar_propietario(self, codigo_propietario, nuevo_nombre, nuevo_telefono, nuevo_correo):
        pos = self.buscar_propietario(codigo_propietario)
        if pos != -1:
            # >>> Validación de teléfono
            try:
                telefono = int(nuevo_telefono)
                if telefono < 0:
                    print("Error: El teléfono no puede ser negativo.")
                    return False
                if len(str(telefono)) != 10:
                    print("Error: El teléfono debe tener exactamente 10 dígitos.")
                    return False
            except ValueError:
                print("Error: El teléfono debe ser numérico.")
                return False

            # >>> Validar correo
            if "@" not in nuevo_correo or "." not in nuevo_correo:
                print("Error: El correo electrónico no es válido.")
                return False

            propietario = self.propietarios[pos]
            propietario.nombre_propietario = nuevo_nombre
            propietario.telefono_propietario = str(nuevo_telefono)
            propietario.correo_propietario = nuevo_correo
            return True
        return False

    # >>> Método Eliminar Propietario ====================================================================
    def eliminar_propietario(self, codigo_propietario):
        pos = self.buscar_propietario(codigo_propietario)
        if pos != -1:
            del self.propietarios[pos]
            return True
        return False

    # >>> =================================================== Vehículo =====================================================
    def adicionar_vehiculo(self, vehiculo):
        # Validar placa obligatoria
        if vehiculo.placa == "":
            print("Error: La placa no puede estar vacía.")
            return False

        # Validar que no exista otro vehículo con la misma placa
        if self.buscar_vehiculo(vehiculo.placa) != -1:
            print("Error: Ya existe un vehículo con esa placa.")
            return False

        # Validar que el propietario exista
        pos = self.buscar_propietario(vehiculo.id_propietario)
        if pos == -1:
            print("Error: No existe un propietario con ese ID.")
            return False

        self.vehiculos.append(vehiculo)
        return True


    def buscar_vehiculo(self, placa):
        for i, v in enumerate(self.vehiculos):
            if v.placa == placa:
                return i
        return -1


    def listar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
            return
        print("===== LISTA DE VEHÍCULOS =====")
        for v in self.vehiculos:
            print(f"Placa: {v.placa}")


    def visualizar_vehiculo(self, placa):
        pos = self.buscar_vehiculo(placa)
        if pos != -1:
            self.vehiculos[pos].visualizar_vehiculo()
            return True
        print(f"No se encontró un vehículo con placa {placa}.")
        return False


    def modificar_vehiculo(self, placa, nueva_marca, nuevo_modelo, nuevo_color, nuevo_id_propietario):
        pos = self.buscar_vehiculo(placa)
        if pos != -1:
            # Validar que el nuevo propietario exista
            prop_pos = self.buscar_propietario(nuevo_id_propietario)
            if prop_pos == -1:
                print("Error: No existe un propietario con ese ID.")
                return False

            propietario = self.propietarios[prop_pos]

            v = self.vehiculos[pos]
            v.marca = nueva_marca
            v.modelo = nuevo_modelo
            v.color = nuevo_color
            v.id_propietario = propietario.codigo_propietario
            v.nombre_propietario = propietario.nombre_propietario
            return True
        return False


    def eliminar_vehiculo(self, placa):
        pos = self.buscar_vehiculo(placa)
        if pos != -1:
            del self.vehiculos[pos]
            return True
        return False
    
    # >>> =================================================== Parqueo =====================================================
    def adicionar_parqueo(self, parqueo):
        # Validar ID único
        for p in self.parqueos:
            if p.id_parqueo == parqueo.id_parqueo:
                print("Error: Ya existe un parqueo con ese ID.")
                return False
        self.parqueos.append(parqueo)
        return True


    def buscar_parqueo(self, id_parqueo):
        for i, p in enumerate(self.parqueos):
            if p.id_parqueo == id_parqueo:
                return i
        return -1


    def listar_parqueos(self):
        # Devuelve solo los parqueos activos
        return [p for p in self.parqueos if p.estado == "Parqueado"]


    def visualizar_parqueo(self, placa):
        # Devuelve el parqueo activo de esa placa o None
        for p in self.parqueos:
            if p.placa == placa and p.estado == "Parqueado":
                return p
        return None
    
    def modificar_parqueo(self, id_parqueo, nueva_placa, nuevo_color, nuevo_id_propietario):
        pos = self.buscar_parqueo(id_parqueo)
        if pos != -1:
            # Validar propietario
            prop_pos = self.buscar_propietario(nuevo_id_propietario)
            if prop_pos == -1:
                print("Error: No existe un propietario con ese ID.")
                return False
            propietario = self.propietarios[prop_pos]

            # Validar vehículo
            veh_pos = self.buscar_vehiculo(nueva_placa)
            if veh_pos == -1:
                print("Error: No existe un vehículo con esa placa.")
                return False
            vehiculo = self.vehiculos[veh_pos]

            p = self.parqueos[pos]
            p.placa = vehiculo.placa
            p.marca = vehiculo.marca
            p.color = nuevo_color
            p.id_propietario = propietario.codigo_propietario
            p.nombre_propietario = propietario.nombre_propietario
            return True
        return False


    def eliminar_parqueo(self, id_parqueo):
        pos = self.buscar_parqueo(id_parqueo)
        if pos != -1:
            del self.parqueos[pos]
            return True
        return False


    def salida_vehiculo(self, placa, hora_salida, tarifa=2000):
        for p in self.parqueos:
            if p.placa == placa and p.estado == "Parqueado":
                p.hora_salida = hora_salida
                # Calcular valor (ejemplo: tarifa fija por hora)
                hora_in = datetime.strptime(p.hora_ingreso, "%H:%M:%S")
                hora_out = datetime.strptime(hora_salida, "%H:%M:%S")
                horas = (hora_out - hora_in).seconds // 3600 + 1  # redondeo mínimo 1h
                p.valor_pagar = horas * tarifa
                p.estado = "Finalizado"
                self.pagos_recibidos += p.valor_pagar
                return True
        return False

