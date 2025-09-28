from datetime import datetime
class Parqueadero:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.parqueos = []
        self.vehiculos = []
        self.propietarios = []
        self.pagos = []
# >>> =================================================== Propietario =====================================================
    # >>> Método Adicionar Propietario =============================== 
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
        try:
            codigo = int(propietario.codigo_propietario)
            if codigo < 0:
                print("Error: El ID del propietario no puede ser negativo.")
                return False
        except ValueError:
            print("Error: El ID del propietario debe ser numérico.")
            return False
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
        if "@" not in propietario.correo_propietario or "." not in propietario.correo_propietario:
            print("Error: El correo electrónico no es válido.")
            return False
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
    # >>> Método Adicionar Vahículo =============================== 
    def adicionar_vehiculo(self, vehiculo):
        if vehiculo.placa == "":
            print("Error: La placa no puede estar vacía.")
            return False
        try:
            modelo = int(vehiculo.modelo)
            if modelo < 1900 or modelo > 2026:
                print("Error: El modelo del vehiculo debe estar entre 1900 y 2026.")
                return False
        except ValueError:
            print("Error: El modelo del vehiculo debe ser numérico.")
            return False
        if self.buscar_vehiculo(vehiculo.placa) != -1:
            print("Error: Ya existe un vehículo con esa placa.")
            return False
        pos = self.buscar_propietario(vehiculo.id_propietario)
        if pos == -1:
            print("Error: No existe un propietario con ese ID.")
            return False
        self.vehiculos.append(vehiculo)
        return True
    # >>> Método Buscar Vehículo =============================== 
    def buscar_vehiculo(self, placa):
        for i, v in enumerate(self.vehiculos):
            if v.placa == placa:
                return i
        return -1
    # >>> Método Listar Vehículo =============================== 
    def listar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
            return
        print("===== LISTA DE VEHÍCULOS =====")
        for v in self.vehiculos:
            print(f"Placa: {v.placa}")
    # >>> Método Listar Vehículo =============================== 
    def visualizar_vehiculo(self, placa):
        pos = self.buscar_vehiculo(placa)
        if pos != -1:
            self.vehiculos[pos].visualizar_vehiculo()
            return True
        print(f"No se encontró un vehículo con placa {placa}.")
        return False
    # >>> Método Modificar Vehículo =============================== 
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
    # >>> Método Eliminar Vehículo =============================== 
    def eliminar_vehiculo(self, placa):
        pos = self.buscar_vehiculo(placa)
        if pos != -1:
            del self.vehiculos[pos]
            return True
        return False
   
# >>> =================================================== Parqueo =====================================================
    # >>> Método Adicionar Parqueo =============================== 
    def adicionar_parqueo(self, parqueo):
        try:
            id_parqueo = int(parqueo.id_parqueo)
            if id_parqueo < 0:
                print("Error: El ID del parqueo no puede ser negativo.")
                return False
        except (ValueError, TypeError):
            print("Error: El ID del parqueo debe ser numérico.")
            return False
        if self.buscar_parqueo(id_parqueo) != -1:
            print("Error: Ya existe un parqueo con ese ID.")
            return False
        parqueo.id_parqueo = id_parqueo
        self.parqueos.append(parqueo)
        print("Parqueo registrado con éxito.")
        return True
    # >>> Método Buscar Parqueo =============================== 
    def buscar_parqueo(self, id_parqueo):
        try:
            target = int(id_parqueo)
        except (ValueError, TypeError):
            return -1

        for i, p in enumerate(self.parqueos):
            try:
                if int(p.id_parqueo) == target:
                    return i
            except (ValueError, TypeError):
                continue
        return -1
    # >>> Método Listar Parqueo =============================== 
    def listar_parqueos(self):
        return [p for p in self.parqueos if p.estado == "Parqueado"]
    def buscar_parqueo_por_placa(self, placa):
        for p in self.parqueos:
            if p.placa == placa and p.estado == "Parqueado":
                return p
        return None
    # >>> Método Modificar Parqueo =============================== 
    def modificar_parqueo(self, id_parqueo, nueva_placa):
        pos = self.buscar_parqueo(id_parqueo)
        if pos != -1:
            veh_pos = self.buscar_vehiculo(nueva_placa)
            if veh_pos == -1:
                print("Error: No existe un vehículo con esa placa.")
                return False
            vehiculo = self.vehiculos[veh_pos]
            p = self.parqueos[pos]
            p.placa = vehiculo.placa
            p.marca = vehiculo.marca
            p.color = vehiculo.color
            return True
        return False
    # >>> Método Eliminar Parqueo =============================== 
    def eliminar_parqueo(self, id_parqueo):
        pos = self.buscar_parqueo(id_parqueo)
        if pos != -1:
            del self.parqueos[pos]
            return True
        return False
# >>> =================================================== Reportes =====================================================
    # >>> Método Reporte De Espacios Ocupados =============================== 
    def reporte_espacios_ocupados(self):
        """
        Devuelve la cantidad de espacios ocupados (parqueos activos).
        """
        return len([p for p in self.parqueos if p.estado == "Parqueado"])
    # >>> Método Reporte De Espacios Disponibles ===============================
    def reporte_espacios_disponibles(self):
        """
        Devuelve la cantidad de espacios disponibles,
        teniendo en cuenta la capacidad total y los ocupados.
        """
        return self.capacidad - self.reporte_espacios_ocupados()
    # >>> Método Reporte Cantidad De Vehiculos Parqueados  ===============================
    def reporte_cantidad_vehiculos_parqueados(self):
        """
        Devuelve la cantidad de vehículos distintos que están parqueados actualmente.
        Usa 'set' para evitar contar placas duplicadas.
        """
        placas = [p.placa for p in self.parqueos if p.estado == "Parqueado"]
        return len(set(placas))
    # >>> Método Reporte De Pagos Recibidos ===============================
    def reporte_pagos_recibidos(self):
        """
        Devuelve el valor total de los pagos recibidos por parqueos finalizados.
        """
        return sum(self.pagos)

