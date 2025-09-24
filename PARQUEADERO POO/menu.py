# información y captura de datos.
from os import system
from parqueadero import Parqueadero
from propietario import Propietario
from vehículo import Vehiculo
from datetime import datetime
from parqueo import Parqueo
# Crear la clase Menu
class Menu: 
    def __init__(self):
        self.parqueadero = Parqueadero()
    # >>> Metodo Registrar Propietario ============================================================================
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
        input("\nPresione ENTER para continuar...")

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
        input("\nPresione ENTER para continuar...")

    # >>> Metodo Visualizar Propietario ==============================================================================  
    def visualizar_propietario(self):
        system("cls")
        print("*************************************************")
        print("************* VISUALIZAR PROPIETARIO ************")
        print("*************************************************")
        codigo = input("Ingrese el ID del propietario: ")
        pos = self.parqueadero.buscar_propietario(codigo)   # buscamos en Parqueadero
        if pos != -1:
            propietario = self.parqueadero.propietarios[pos]   # obtenemos el objeto
            propietario.visualizar_propietario()               # llamamos el método de la clase Propietario
        else:
            print("Error - El propietario no existe.")
        input("\nPresione ENTER para continuar...")

        
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
        input("\nPresione ENTER para continuar...")


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
        input("\nPresione ENTER para continuar...")
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
        codigo_propietario = input("Ingrese el ID del propietario: ")

        pos = self.parqueadero.buscar_propietario(codigo_propietario)
        if pos == -1:
            print("Error: No existe un propietario con ese ID.")
        else:
            nombre_propietario = self.parqueadero.propietarios[pos].nombre_propietario
            vehiculo = Vehiculo(placa, marca, modelo, color, codigo_propietario, nombre_propietario)
            if self.parqueadero.adicionar_vehiculo(vehiculo):
                print("Vehículo registrado con éxito.")
            else:
                print("Error: No se pudo registrar el vehículo.")
        input("\nPresione ENTER para continuar...")


    # >>> Listar Vehículos =====================================================================
    def listar_vehiculos(self):
        system("cls")
        print("*************************************************")
        print("**************** LISTAR VEHÍCULOS ***************")
        print("*************************************************")
        self.parqueadero.listar_vehiculos()
        input("\nPresione ENTER para continuar...")


    # >>> Visualizar Vehículo =====================================================================
    def visualizar_vehiculo(self): 
        system("cls")
        print("*************************************************")
        print("************** VISUALIZAR VEHÍCULO **************")
        print("*************************************************")
        placa = input("Ingrese la placa del vehículo: ")
        pos = self.parqueadero.buscar_vehiculo(placa)   # busca en la lista de vehículos
        if pos != -1:
            vehiculo = self.parqueadero.vehiculos[pos]  # obtiene el objeto vehículo
            vehiculo.visualizar_vehiculo()              # llama el método de la clase Vehiculo
        else:
            print("Error - El vehículo no existe.")
        input("\nPresione ENTER para continuar...")



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
        input("\nPresione ENTER para continuar...")


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
        input("\nPresione ENTER para continuar...")
    # >>> Registrar Parqueo (Ingreso o Salida) =====================================================
    def registrar_parqueo(self): 
        system("cls")
        print("*************************************************")
        print("************** REGISTRAR PARQUEO ****************")
        print("*************************************************")

        codigo_parqueo = input("Ingrese el ID del parqueo: ")
        opcion = input("Digite 1 para ENTRADA o 2 para SALIDA del vehículo: ")

        if opcion == "1":  # ENTRADA
            ahora = datetime.now()
            fecha = ahora.date()        # Guardamos fecha como objeto date
            hora_ingreso = ahora.time() # Guardamos hora como objeto time

            placa = input("Ingrese la placa del vehículo: ")
            pos_vehiculo = self.parqueadero.buscar_vehiculo(placa)

            if pos_vehiculo == -1:
                print("Error - El vehículo no existe. Primero debe registrarlo.")
            else:
                vehiculo = self.parqueadero.vehiculos[pos_vehiculo]
                codigo_propietario = vehiculo.codigo_propietario
                nombre_propietario = vehiculo.nombre_propietario

                # Crear objeto Parqueo
                nuevo_parqueo = Parqueo(
                    codigo_parqueo, fecha, placa, vehiculo.marca,
                    vehiculo.color, codigo_propietario,
                    nombre_propietario, hora_ingreso
                )

                # Pasar el objeto al método
                if self.parqueadero.adicionar_parqueo(nuevo_parqueo):
                    print("\n Parqueo registrado exitosamente.")
                    print("===== DETALLE DEL PARQUEO =====")
                    print(f"ID Parqueo: {codigo_parqueo}")
                    print(f"Fecha: {fecha}")
                    print(f"Placa: {placa}")
                    print(f"Marca: {vehiculo.marca}")
                    print(f"Color: {vehiculo.color}")
                    print(f"ID Propietario: {codigo_propietario}")
                    print(f"Nombre Propietario: {nombre_propietario}")
                    print(f"Hora Ingreso: {hora_ingreso}")  # objeto time
                    print(f"Estado: Activo")
                else:
                    print("Error - No se pudo registrar el parqueo.")
        
        input("\nPresione ENTER para continuar...")




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
                print(f"ID Parqueo: {p.codigo_parqueo}")
                print(f"Fecha: {p.fecha}")
                print(f"Placa: {p.placa}")
                print(f"Marca: {p.marca}")
                print(f"Color: {p.color}")
                print(f"ID Propietario: {p.codigo_propietario}")
                print(f"Nombre Propietario: {p.nombre_propietario}")
                print(f"Hora Ingreso: {p.hora_ingreso}")
                if p.hora_salida:
                    print(f"Hora Salida: {p.hora_salida}")
                    print(f"Valor a Pagar: {p.valor_pagar}")
                print(f"Estado: {p.estado}")

        input("\nPresione ENTER para continuar...")
    # >>> Visualizar Parqueo =====================================================================
    def visualizar_parqueo(self):
        system("cls")
        print("*************************************************")
        print("************* VISUALIZAR PARQUEO ****************")
        print("*************************************************")

        placa = input("Ingrese la placa del vehículo: ")
        parqueo = self.parqueadero.buscar_parqueo_por_placa(placa)

        if parqueo:
            print("===== DETALLE DEL PARQUEO =====")
            print(f"ID Parqueo: {parqueo.codigo_parqueo}")
            print(f"Fecha: {parqueo.fecha}")
            print(f"Placa: {parqueo.placa}")
            print(f"Marca: {parqueo.marca}")
            print(f"Color: {parqueo.color}")
            print(f"ID Propietario: {parqueo.codigo_propietario}")
            print(f"Nombre Propietario: {parqueo.nombre_propietario}")
            print(f"Hora Ingreso: {parqueo.hora_ingreso}")
            if parqueo.hora_salida:  # si ya salió
                print(f"Hora Salida: {parqueo.hora_salida}")
                print(f"Valor a Pagar: {parqueo.valor_pagar}")
            print(f"Estado: {parqueo.estado}")
        else:
            print("Error - No se encontró un parqueo activo para esa placa.")

        input("\nPresione ENTER para continuar...")


    # >>> Modificar Parqueo =====================================================================
    def modificar_parqueo(self):
        system("cls")
        print("*************************************************")
        print("************** MODIFICAR PARQUEO ****************")
        print("*************************************************")
        codigo_parqueo = input("Ingrese el ID del parqueo: ")
        nueva_placa = input("Nueva placa del vehículo: ")
        nuevo_color = input("Nuevo color: ")
        nuevo_codigo_propietario = input("Nuevo ID del propietario: ")

        if self.parqueadero.modificar_parqueo(codigo_parqueo, nueva_placa, nuevo_color, nuevo_codigo_propietario):
            print("Parqueo modificado con éxito.")
        else:
            print("Error: No se pudo modificar el parqueo.")
        input("\nPresione ENTER para continuar...")


    # >>> Eliminar Parqueo =====================================================================
    def eliminar_parqueo(self):
        system("cls")
        print("*************************************************")
        print("************** ELIMINAR PARQUEO *****************")
        print("*************************************************")
        codigo_parqueo = input("Ingrese el ID del parqueo: ")
        if self.parqueadero.eliminar_parqueo(codigo_parqueo):
            print("Parqueo eliminado con éxito.")
        else:
            print("Error: No se encontró un parqueo con ese ID.")
        input("\nPresione ENTER para continuar...")
        
    def visualizar_espacios_ocupados(self):
        system("cls")
        print("*************************************************")
        print("************ ESPACIOS OCUPADOS ******************")
        print("*************************************************")

        ocupados = self.parqueadero.espacios_totales - self.parqueadero.espacios_disponibles
        print(f"Espacios ocupados: {ocupados}")

        input("\nPresione ENTER para continuar...")

    # >>> Reporte de vehículos parqueados
    def generar_reporte_vehiculos_parqueados(self):
        system("cls")
        print("*********************************************")
        print("***** REPORTE DE VEHÍCULOS PARQUEADOS *******")
        print("*********************************************")

        cantidad = self.parqueadero.reporte_vehiculos_parqueados()
        print(f"Cantidad de vehículos parqueados: {cantidad}")

        input("\nPresione ENTER para continuar...")


    # >>> Reporte de espacios disponibles
    def generar_reporte_espacios_disponibles(self):
        system("cls")
        print("*********************************************")
        print("****** REPORTE DE ESPACIOS DISPONIBLES ******")
        print("*********************************************")

        cantidad = self.parqueadero.reporte_espacios_disponibles()
        print(f"Cantidad de espacios disponibles para parqueo: {cantidad}")

        input("\nPresione ENTER para continuar...")

    def visualizar_espacios_disponibles(self):
        system("cls")
        print("*************************************************")
        print("******** ESPACIOS DISPONIBLES *******************")
        print("*************************************************")

        disponibles = self.parqueadero.visualizar_espacios_disponibles()
        print(f"Cantidad de espacios disponibles: {disponibles}")

        input("\nPresione ENTER para continuar...")


    # >>> Reporte de pagos recibidos
    def generar_reporte_pagos_recibidos(self):
        system("cls")
        print("*********************************************")
        print("******* REPORTE DE PAGOS RECIBIDOS **********")
        print("*********************************************")

        total = self.parqueadero.reporte_ingresos()
        print(f"Total de pagos recibidos: ${total}")

        input("\nPresione ENTER para continuar...")

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
            print("******************** p. Visualizar cantidad de espacios ocupados             *******************************")
            print("******************** q. Visualizar cantidad de espacios disponibles          *******************************")
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
                    self.visualizar_espacios_ocupados()
                elif opcion == "q":
                    self.generar_reporte_espacios_disponibles()
                elif opcion == "r":
                    self.generar_reporte_vehiculos_parqueados()
                elif opcion == "s":
                    self.generar_reporte_espacios_disponibles()
                elif opcion == "t":
                    self.generar_reporte_pagos_recibidos()
                elif opcion == "u":
                    break
                else:
                    print("**********************************************")
                    print("Error - Opción no válida")
                    print("**********************************************")
                    input()

            except Exception as e:
                print(f"Error - {e}")
                input()

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()        