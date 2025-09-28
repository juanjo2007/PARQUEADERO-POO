# información y captura de datos.
from os import system
from parqueadero import Parqueadero
from propietario import Propietario
from vehiculo import Vehiculo
from datetime import datetime
from parqueo import Parqueo
# Crear la clase Menu
class Menu:
    def __init__(self):
        self.parqueadero = Parqueadero()
    # >>> Metodo Registrar Propietario ============================================================================
    def registrar_propietario(self):
        system("cls")
        print("*************************************************")
        print("*************** Registrar Propietario ***********")
        print("*************************************************")
        id_propietario = str(input("Ingrese el id del propietario: "))
        nombre_propietario = str(input("Ingrese el nombre del propietario: "))
        telefono_propietario = str(input("Ingrese el teléfono del propietario: "))
        correo_propietario = str(input("Ingrese el correo del propietario: "))
        propietario = Propietario(id_propietario, nombre_propietario, telefono_propietario, correo_propietario)
        if self.parqueadero.adicionar_propietario(propietario):
            print("**********************************************************")
            print("Información - Propietario registrado satisfactoriamente")
            print("**********************************************************")
        else:
            print("**********************************************************")
            print("Error - El propietario no fue adicionado. Verifique los datos.")
            print("**********************************************************")
        input()
    # >>> Metodo Listar Propietarios ==============================================================================  
    def listar_propietario(self):
        system("cls")
        print("*************************************************")
        print("***************** LISTAR propietarios *************")
        print("*************************************************")
        # >>> El ciclo for debe recorrer la lista de aprendices y mostrar sus datos
        for propietario in self.parqueadero.propietarios:
            print("************************************************")
            print("Id_propietario: %s" % (propietario.codigo_propietario))
            print("Nombre_propietario: %s" % (propietario.nombre_propietario))
            print("Telefono_propietario: %s" % (propietario.telefono_propietario))
            print("Correo_propietario: %s" % (propietario.correo_propietario))
            print("************************************************")
        input()
    # >>> Metodo Visualizar Propietario ==============================================================================  
    def visualizar_propietario(self):
        system("cls")
        print("*************************************************")
        print("************* VISUALIZAR PROPIETARIO ************")
        print("*************************************************")
        codigo = input("Ingrese el ID del propietario: ")
        pos = self.parqueadero.buscar_propietario(codigo)
        if pos != -1:
            propietario = self.parqueadero.propietarios[pos]   # <-- ojo, no lista_propietarios
            propietario.visualizar_propietario()               # <-- usa el método de la clase Propietario
        else:
            print("Error - El propietario no existe.")
        input()
    # >>> Metodo Modificar Propietario ==============================================================================
    def modificar_propietario(self):
        system("cls")
        print("*************************************************")
        print("************ MODIFICAR PROPIETARIO **************")
        print("*************************************************")
        codigo = input("Ingrese el ID del propietario a modificar: ")
        pos = self.parqueadero.buscar_propietario(codigo)
        if pos != -1:
            print("Ingrese los nuevos datos del propietario:")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo teléfono (10 dígitos): ")
            nuevo_correo = input("Nuevo correo: ")
            if self.parqueadero.modificar_propietario(codigo, nuevo_nombre, nuevo_telefono, nuevo_correo):
                print("Propietario modificado con éxito.")
            else:
                print("Error - No se pudo modificar el propietario (validación fallida).")
        else:
            print("Error - El propietario no existe.")
        input()
# >>> Metodo Eliminar Propietario ==============================================================================
    def eliminar_propietario(self):
        system("cls")
        print("*************************************************")
        print("************* ELIMINAR PROPIETARIO **************")
        print("*************************************************")
        codigo = input("Ingrese el ID del propietario a eliminar: ")
        if self.parqueadero.eliminar_propietario(codigo):
            print("Propietario eliminado con éxito.")
        else:
            print("Error - El propietario no existe.")
        input()
    # >>> Registrar Vehículo =====================================================================
    def registrar_vehiculo(self):
        system("cls")
        print("*************************************************")
        print("************** REGISTRAR VEHÍCULO ***************")
        print("*************************************************")
        placa = input("Ingrese la placa del vehículo: ")
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        color = input("Ingrese el color del vehículo: ")
        id_propietario = input("Ingrese el ID del propietario: ")
        pos = self.parqueadero.buscar_propietario(id_propietario)
        if pos == -1:
            print("Error: No existe un propietario con ese ID.")
        else:
            nombre_propietario = self.parqueadero.propietarios[pos].nombre_propietario
            vehiculo = Vehiculo(placa, marca, modelo, color, id_propietario, nombre_propietario)
            if self.parqueadero.adicionar_vehiculo(vehiculo):
                print("Vehículo registrado con éxito.")
            else:
                print("Error: No se pudo registrar el vehículo.")
            input()
    # >>> Listar Vehículos =====================================================================
    def listar_vehiculos(self):
        system("cls")
        print("*************************************************")
        print("**************** LISTAR VEHÍCULOS ***************")
        print("*************************************************")
        self.parqueadero.listar_vehiculos()
        input()
    # >>> Visualizar Vehículo =====================================================================
    def visualizar_vehiculo(self):
        system("cls")
        print("*************************************************")
        print("************** VISUALIZAR VEHÍCULO **************")
        print("*************************************************")
        placa = input("Ingrese la placa del vehículo: ")
        self.parqueadero.visualizar_vehiculo(placa)
        input()
    # >>> Modificar Vehículo =====================================================================
    def modificar_vehiculo(self):
        system("cls")
        print("*************************************************")
        print("************** MODIFICAR VEHÍCULO ***************")
        print("*************************************************")
        placa = input("Ingrese la placa del vehículo: ")
        nueva_marca = input("Nueva marca: ")
        nuevo_modelo = input("Nuevo modelo: ")
        nuevo_color = input("Nuevo color: ")
        nuevo_id_propietario = input("Nuevo ID del propietario: ")
        if self.parqueadero.modificar_vehiculo(placa, nueva_marca, nuevo_modelo, nuevo_color, nuevo_id_propietario):
            print("Vehículo modificado con éxito.")
        else:
            print("Error: No se pudo modificar el vehículo.")
        input()
    # >>> Eliminar Vehículo =====================================================================
    def eliminar_vehiculo(self):
        system("cls")
        print("*************************************************")
        print("************** ELIMINAR VEHÍCULO ****************")
        print("*************************************************")
        placa = input("Ingrese la placa del vehículo: ")
        if self.parqueadero.eliminar_vehiculo(placa):
            print("Vehículo eliminado con éxito.")
        else:
            print("Error: No se encontró el vehículo.")
        input()
    # >>> Registrar Parqueo (Ingreso o Salida) =====================================================
    def registrar_parqueo(self):
        system("cls")
        print("*************************************************")
        print("************** REGISTRAR PARQUEO ****************")
        print("*************************************************")
        id_parqueo_raw = input("Ingrese el ID del parqueo: ")
        try:
            id_parqueo = int(id_parqueo_raw)
            if id_parqueo < 0:
                print("Error - El ID del parqueo no puede ser negativo.")
                input("\nPresione Enter para continuar...")
                return
        except ValueError:
            print("Error - El ID del parqueo debe ser numérico.")
            input("\nPresione Enter para continuar...")
            return
        opcion = input("Digite 1 para ENTRADA o 2 para SALIDA del vehículo: ")
        if opcion == "1":  # ENTRADA
            ahora = datetime.now()
            fecha = str(ahora.date())
            hora_ingreso = ahora.strftime("%H:%M:%S")

            placa = input("Ingrese la placa del vehículo: ")
            pos_vehiculo = self.parqueadero.buscar_vehiculo(placa)

            if pos_vehiculo == -1:
                print("Error - El vehículo no existe. Primero debe registrarlo.")
                input("\nPresione Enter para continuar...")
            else:
                vehiculo = self.parqueadero.vehiculos[pos_vehiculo]
                id_propietario = vehiculo.id_propietario
                nombre_propietario = vehiculo.nombre_propietario

                # Crear objeto Parqueo
                nuevo_parqueo = Parqueo(
                    id_parqueo, fecha, placa, vehiculo.marca,
                    vehiculo.color, id_propietario,
                    nombre_propietario, hora_ingreso
                )
                if self.parqueadero.adicionar_parqueo(nuevo_parqueo):
                    # Mostrar comprobante de entrada
                    print("\n===== ENTRADA REGISTRADA =====")
                    print(f"Placa: {placa}")
                    print(f"Propietario: {nombre_propietario}")
                    print(f"Marca: {vehiculo.marca}")
                    print(f"Color: {vehiculo.color}")
                    print(f"Hora Ingreso: {hora_ingreso}")
                    print("Estado: Parqueado")
                else:
                    print("Error - No se pudo registrar el parqueo.")
                input("\nPresione Enter para continuar...")
        elif opcion == "2":  # SALIDA
            placa = input("Ingrese la placa del vehículo: ")
            parqueo = self.parqueadero.buscar_parqueo_por_placa(placa)
            if parqueo is None:
                print("Error - No se encontró un parqueo activo con esa placa.")
            else:
                # Hora de salida
                hora_salida = input("Ingrese la hora de salida (HH:MM:SS): ")

                formato = "%H:%M:%S"
                try:
                    h_ingreso = datetime.strptime(parqueo.hora_ingreso, formato)
                    h_salida = datetime.strptime(hora_salida, formato)
                    if h_salida < h_ingreso:
                        h_salida = h_salida.replace(day=h_ingreso.day + 1)
                except ValueError:
                    print("Error - La hora de salida no tiene un formato válido (HH:MM:SS).")
                    input("\nPresione Enter para continuar...")
                    return
                tiempo = h_salida - h_ingreso
                horas = tiempo.total_seconds() / 3600
                horas_cobradas = int(horas) + (1 if horas % 1 > 0 else 0)  
                valor_pagar = horas_cobradas * 2800
                parqueo.hora_salida = hora_salida
                parqueo.valor_pagar = valor_pagar
                parqueo.estado = "Finalizado"
                self.parqueadero.pagos.append(valor_pagar)
                print("\n===== SALIDA REGISTRADA =====")
                print(f"Placa: {parqueo.placa}")
                print(f"Hora Ingreso: {parqueo.hora_ingreso}")
                print(f"Hora Salida: {hora_salida}")
                print(f"Horas cobradas: {horas_cobradas}")
                print(f"Valor a Pagar: ${valor_pagar}")
                print("Estado: Finalizado")
                input("\nPresione Enter para continuar...")
        else:
            print("Error - Opción no válida. Debe ser 1 (Entrada) o 2 (Salida).")
            input("\nPresione Enter para continuar...")
    # >>> Listar Parqueos =====================================================================
    def listar_parqueos(self):
        system("cls")
        print("*************************************************")
        print("**************** LISTAR PARQUEOS ****************")
        print("*************************************************")
        if not self.parqueadero.parqueos:
            print("No hay parqueos registrados.")
        else:
            for p in self.parqueadero.parqueos:
                print("-----------------------------------")
                print(f"ID Parqueo: {p.id_parqueo}")
                print(f"Fecha: {p.fecha}")
                print(f"Placa: {p.placa}")
                print(f"Marca: {p.marca}")
                print(f"Color: {p.color}")
                print(f"ID Propietario: {p.id_propietario}")
                print(f"Nombre Propietario: {p.nombre_propietario}")
                print(f"Hora Ingreso: {p.hora_ingreso}")
                if p.hora_salida:
                    print(f"Hora Salida: {p.hora_salida}")
                    print(f"Valor a Pagar: {p.valor_pagar}")
                print(f"Estado: {p.estado}")
        input()
    # >>> Visualizar Parqueo =====================================================================
    def visualizar_parqueo(self):
        system("cls")
        print("*************************************************")
        print("************ VISUALIZAR PARQUEO *****************")
        print("*************************************************")
        placa = input("Ingrese la placa del vehículo: ")
        parqueo = self.parqueadero.buscar_parqueo_por_placa(placa)
        if parqueo:
            print("===== DETALLE DEL PARQUEO =====")
            print(f"ID Parqueo: {parqueo.id_parqueo}")
            print(f"Fecha: {parqueo.fecha}")
            print(f"Placa: {parqueo.placa}")
            print(f"Marca: {parqueo.marca}")
            print(f"Color: {parqueo.color}")
            print(f"ID Propietario: {parqueo.id_propietario}")
            print(f"Nombre Propietario: {parqueo.nombre_propietario}")
            print(f"Hora Ingreso: {parqueo.hora_ingreso}")
            print(f"Hora Salida: {parqueo.hora_salida if parqueo.hora_salida else '---'}")
            print(f"Valor a Pagar: {parqueo.valor_pagar if parqueo.valor_pagar else '---'}")
            print(f"Estado: {parqueo.estado}")
        else:
            print("Error - No se encontró un parqueo con esa placa.")
        input()
    # >>> Modificar Parqueo =====================================================================
    def modificar_parqueo(self):
        system("cls")
        print("*************************************************")
        print("************** MODIFICAR PARQUEO ****************")
        print("*************************************************")
        id_parqueo = input("Ingrese el ID del parqueo: ")
        nueva_placa = input("Nueva placa del vehículo: ")

        if self.parqueadero.modificar_parqueo(id_parqueo, nueva_placa):
            print("Parqueo modificado con éxito.")
        else:
            print("Error: No se pudo modificar el parqueo.")
        input()

    # >>> Eliminar Parqueo =====================================================================
    def eliminar_parqueo(self):
        system("cls")
        print("*************************************************")
        print("************** ELIMINAR PARQUEO *****************")
        print("*************************************************")
        id_parqueo = input("Ingrese el ID del parqueo: ")
        if self.parqueadero.eliminar_parqueo(id_parqueo):
            print("Parqueo eliminado con éxito.")
        else:
            print("Error: No se encontró un parqueo con ese ID.")
        input()
    # >>> Método Visualizar La Cantidad De Espacios Ocupados ========================================
    def visualizar_cantidad_espacios_ocupados(self):
        system("cls")
        print("*********************************************")
        print("**** VISUALIZAR CANTIDAD DE ESPACIOS OCUPADOS ****")
        print("*********************************************")
        cantidad = self.parqueadero.reporte_espacios_ocupados()
        print(f"Cantidad de espacios ocupados: {cantidad}")
        input("\nPresione Enter para continuar...")
    # >>> Método Visualizar La Cantidad De Espacios Disponibles ========================================
    def visualizar_cantidad_espacios_disponibles(self):
        system("cls")
        print("*********************************************")
        print("**** VISUALIZAR CANTIDAD DE ESPACIOS DISPONIBLES ****")
        print("*********************************************")
        cantidad = self.parqueadero.reporte_espacios_disponibles()
        print(f"Cantidad de espacios disponibles: {cantidad}")
        input("\nPresione Enter para continuar...")
    # >>> Método Reporte De Vehículos Parqueados =====================================================================
    def reporte_vehiculos_parqueados(self):
        system("cls")
        print("*********************************************")
        print("*** REPORTE DE CANTIDAD VEHÍCULOS PARQUEADOS ***")
        print("*********************************************")
        cantidad = self.parqueadero.reporte_cantidad_vehiculos_parqueados()
        print(f"Cantidad de vehículos parqueados: {cantidad}")
        input("\nPresione Enter para continuar...")
    # >>> Método Reporte De Espacios Disponibles =====================================================================
    def reporte_espacios_disponibles(self):
        system("cls")
        print("*********************************************")
        print("*** REPORTE DE ESPACIOS DISPONIBLES ***")
        print("*********************************************")
        disponibles = self.parqueadero.reporte_espacios_disponibles()
        print(f"Espacios disponibles: {disponibles}")
        input("\nPresione Enter para continuar...")
    # >>> Método Reporte De Pagos Recibidos =====================================================================
    def reporte_pagos(self):
        system("cls")
        print("*********************************************")
        print("*** REPORTE DE PAGOS RECIBIDOS POR PARQUEO ***")
        print("*********************************************")
        total = self.parqueadero.reporte_pagos_recibidos()
        print(f"Total de pagos recibidos: ${total}")
        input("\nPresione Enter para continuar...")
   # >>> Crear Metodo mostrar_menu que muestre el menu de la aplicacion y permita seleccionar una opcion
    def mostrar_menu(self):
        while True:
            system("cls")
            print("****************************************** PARQUEADERO CDTI ************************************************")
            print("************************************************************************************************************")
            print("*********************************************** MENÚ *******************************************************")
            print("************************************************************************************************************")
            print("******************** a. Registrar propietario                                *******************************")
            print("******************** b. Listar propietarios                                  *******************************")
            print("******************** c. Visualizar propietario                               *******************************")
            print("******************** d. Modificar propietario                                *******************************")
            print("******************** e. Eliminar propietario                                 *******************************")
            print("******************** f. Registrar vehículo                                   *******************************")
            print("******************** g. Listar vehículos                                     *******************************")
            print("******************** h. Visualizar vehículo                                  *******************************")
            print("******************** i. Modificar vehículo                                   *******************************")
            print("******************** j. Eliminar vehículo                                    *******************************")
            print("******************** k. Registrar parqueo                                    *******************************")
            print("******************** l. Listar parqueos                                      *******************************")
            print("******************** m. Visualizar parqueo                                   *******************************")
            print("******************** n. Modificar parqueo                                    *******************************")
            print("******************** o. Eliminar parqueo                                     *******************************")
            print("******************** p. visualizar_espacios_disponibles                      *******************************")
            print("******************** q. visualizar_vehiculos_parqueados                      *******************************")
            print("******************** r. Generar reporte de cantidad de vehículos parqueados  *******************************")
            print("******************** s. Generar reporte de espacios disponibles              *******************************")
            print("******************** t. Generar reporte de pagos recibidos por parqueo       *******************************")
            print("******************** u. Salir                                                *******************************")
            print("************************************************************************************************************")
            try:
                print("**************************************************")
                opcion = input("Seleccione la opción que desea: ").lower()
                print("**************************************************")
                if opcion == "a":
                    self.registrar_propietario()
                elif opcion == "b":
                    self.listar_propietario()
                elif opcion == "c":
                    self.visualizar_propietario()
                elif opcion == "d":
                    self.modificar_propietario()
                elif opcion == "e":
                    self.eliminar_propietario()
                elif opcion == "f":
                    self.registrar_vehiculo()
                elif opcion == "g":
                    self.listar_vehiculos()
                elif opcion == "h":
                    self.visualizar_vehiculo()
                elif opcion == "i":
                    self.modificar_vehiculo()
                elif opcion == "j":
                    self.eliminar_vehiculo()
                elif opcion == "k":
                    self.registrar_parqueo()
                elif opcion == "l":
                    self.listar_parqueos()
                elif opcion == "m":
                    self.visualizar_parqueo()
                elif opcion == "n":
                    self.modificar_parqueo()
                elif opcion == "o":
                    self.eliminar_parqueo()
                elif opcion == "p":
                    self.visualizar_cantidad_espacios_ocupados()
                elif opcion == "q":
                    self.visualizar_cantidad_espacios_disponibles()
                elif opcion == "r":
                    self.reporte_vehiculos_parqueados()
                elif opcion == "s":
                    self.reporte_espacios_disponibles()
                elif opcion == "t":
                    self.reporte_pagos()
                elif opcion == "u":
                    break
                else:
                    print("**********************************************")
                    print("Error - Opción no válida")
                    print("**********************************************")
                    input()
            except ValueError:
                print(f"Error - Dato no valido")
                input()
if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()        
