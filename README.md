La presente actividad tiene como objetivo continuar con la apropiación de la temática de
POO con el ejercicio Parqueadero. A continuación, se listan los puntos que se deben realizar
y que deben ser entregados totalmente funcional en una carpeta llamada Parqueadero con
los archivos menu.py, propietario.py, vehiculo.py, paqueadero.py (como mínimo), los
cuales deben ser montados en la plataforma classroom (previa verificación y sustentación).
1. Crear un archivo que se llame menu.py
2. En el archivo creado en el punto anterior, se debe incluir los mensajes de
información y captura de datos. No se debe incluir ningún procedimiento.
3. En el archivo menu.py se debe tener un menú con las siguientes opciones:
a. Registrar propietario.
b. Listar propietarios.
c. Visualizar propietario.
d. Modificar propietario.
e. Eliminar propietario.
f. Registrar vehículo.
g. Listar vehículos.
h. Visualizar vehículo.
i. Modificar vehículo.
j. Eliminar vehículo.
k. Registrar parqueo.
l. Listar parqueos.
m. Visualizar parqueo.
n. Modificar parqueo.
o. Eliminar parqueo.
p. Visualizar cantidad de espacios * ocupados.
q. Visualizar cantidad de espacios * disponibles.
r. Generar reporte de cantidad de vehículos parqueados.

2

DO-F-012 V06

s. Generar reporte de cantidad de espacios disponibles para parqueo.
t. Generar reporte de los pagos recibidos por parqueo.
u. Salir.

4. Para el método de registrar propietario, como mínimo se debe realizar la captura de
los siguientes elementos:
a. Id del propietario.
b. Nombre del propietario.
c. Teléfono del propietario.
d. Correo electrónico del propietario.
5. Para el método de listar propietarios se deben listar todos los propietarios que se
encuentren almacenados, el listar debe mostrar los Id de los propietarios y los
Nombres de los propietarios.
6. Para el método de visualizar propietario se deben visualizar todos los atributos del
propietario. Se deben cargar a partir de la solicitud del id del propietario que se
desea visualizar.
7. Para el método de modificar propietario se pueden modificar todos los atributos del
propietario a excepción del id del propietario.
8. Para el método de eliminar propietario, se debe eliminar a través del id del
propietario.
9. Para el método de registrar vehículo, como mínimo se debe realizar la captura de
los siguientes elementos:
a. Placa del vehículo.
b. Marca del vehículo.
c. Modelo del vehículo.
d. Color del vehículo.
e. Id del propietario.

3

DO-F-012 V06

f. Nombre del propietario. (Debe ser cargado por defecto al ingresar el id del
propietario).
10. Para el método de listar vehículos se deben listar todos los vehículos que se
encuentren almacenados, el listar debe mostrar las Placas de los vehículos.
11. Para el método de visualizar vehículo se deben visualizar todos los atributos del
vehículo. Se deben cargar a partir de la solicitud de la placa del vehículo que se desea
visualizar.
12. Para el método de modificar vehículo se pueden modificar todos los atributos del
vehículo a excepción de la placa del vehículo.
13. Para el método de eliminar vehículo, se debe eliminar el vehículo a través de la placa
del vehículo.
12. Para el método de registrar parqueo, como mínimo se debe realizar la captura de
los siguientes elementos:
a. Id del parqueo.
b. Se debe indicar si se desea realizar el registro del parqueo o de salida del
vehículo. Si la opción elegida es parqueo de vehículo, se deben solicitar los
siguientes datos:
 Fecha. (Se debe tomar solo la fecha del sistema).
 Placa del vehículo.
 Marca del vehículo. (Debe ser cargada por defecto al ingresar la placa del
vehículo).
 Color del vehículo. (Debe ser cargado por defecto al ingresar la placa del
vehículo).
 Id del propietario.
 Nombre del propietario. (Debe ser cargado por defecto al ingresar el id
del propietario).
 Hora de ingreso. (Se debe tomar la hora del sistema).

4

DO-F-012 V06

c. Si la opción elegida es salida del vehículo, se debe solicitar la placa del vehículo
y registrar los siguientes datos:
a. Hora de salida**. (Se debe ingresar de forma manual). Manual o del
sistema
b. Valor a pagar***. (Debe cargar de forma automática de acuerdo con el
valor de parqueo)

13. Para el método de listar parqueos se deben listar todos los vehículos que se
encuentren con estado parqueado con los atributos de Placa del vehículo y Marca
del vehículo.
14. Para el método de visualizar el parqueo de un vehículo se deben visualizar los
atributos del parqueo de fecha, placa del vehículo y hora de ingreso. Se deben cargar
a partir de la solicitud de la placa del vehículo que se desea visualizar.
15. Para el método de modificar parqueo se pueden modificar todos los atributos del
vehículo a excepción de id del parqueo. Tenga en cuenta que a partir de los id del
propietario y del vehículo se cargan atributos por defecto.
16. Para el método de eliminar parqueo, se debe eliminar a través del id del parqueo.
17. Para el método de Generar reporte de vehículos parqueados, se debe visualizar la
cantidad de vehículos que se encuentran parqueados.
18. Para el método de Generar reporte de espacios disponibles, se debe visualizar la
cantidad de espacios que se encuentran disponibles para parqueo.
19. Para el método de Generar reporte de los pagos recibidos por parqueo, se debe
cargar el valor total de los ingresos recibidos por los parqueos de los vehículos.
20. Al momento de registrar un parqueo debe tener en cuenta que:
a. No se puede crear el parqueo si no existe el vehículo.
b. No se puede crear el parqueo si no existe el propietario.

5

DO-F-012 V06

c. No se puede crear un parqueo si no hay disponibilidad de espacios.
21. A medida que se registre un parqueo se debe ir descontando la cantidad de espacios
disponibles.
22. A medida que se registre una salida se debe ir aumentado la cantidad de espacios
disponibles.
23. Los id del propietario, la placa del vehículo y el id del parqueo, deben estar validados,
es decir, no se puede crear un id del propietario, la placa del vehículo o el id del parqueo
que ya se encuentren almacenados.
24. (*) El parqueadero cuenta con disponibilidad de parqueo para 10 vehículos.
25. (**) La hora de salida del vehículo debe ser valida, es decir, debe ser una hora real y
no debe ser inferior a la hora de ingreso del vehículo.
26. (***) Para realizar el cálculo del valor a pagar por el parqueadero, se debe tener en
cuenta que el valor de la hora o fracción es de $2.800.
27. Todos los atributos que requiera para realizar el código deben ser atributos públicos.
28. Para el desarrollo del ejercicio se deben crear como mínimo la clase menú, la clase
propietario, la clase vehículo y la clase parqueo.
29. Se deben generar los mensajes correspondientes a la ejecución de los métodos, es
decir, por ejemplo, si se crea el propietario, se debe mostrar por consola el mensaje
que indique que el propietario fue creado de forma satisfactoria.
30. El código debe estar documentado.
