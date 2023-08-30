#GRUPO: Arnold Ignacio, Ferraro Sofía, Irisarri Camila, Liguori Gianfranco, Viera Gabriela. 

#Ejercicio1
#Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = 10
altura = 5
area = base * altura
print(" 1) Area:", area )

#Ejercicio2
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

a=float(input("Ingrese numero: "))**2
b=float(input("Ingrese numero: "))**2
h=(a+b)**0.5
print(h)

#Ejercicio3
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = 2
num2 = 1
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2
print(" 3) Suma:", suma )
print(" 3) Resta:", resta )
print(" 3) Division:", division )
print(" 3) Multiplicacion:", multiplicacion )

#Ejercicio4
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar
# que la fórmula para la conversión es:
# C = (F-32)*5/9

grados_fahrenheit = 57.9
conversor_temperatura = (grados_fahrenheit - 32) * 5/ 9
print(conversor_temperatura) 

#Ejercicio5
#¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
#a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
#b)	precio = input(“Precio: “)
#total = precio + (precio * 0.1)
#c)	edad = int(input(“Edad: “))
#print(tu edad es, edad)
#d)	edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18)

#a) Para guardar el nombre de la canción en la variable esta no debe estar dentro del input.
nombre = input('¿Cuál es tu canción favorita? ')
print(nombre)
# b) Tenemos que transformar el tipo de la variable precio de string a int o float, ya que input nos
# devuelve una variable de tipo string.
precio = float(input('Precio: '))
total = precio + (precio * 0.1)
print(total)
# c) Cuando queremos imprimir algo que no sea una variable debe ir entre comillas.
edad = int(input('Edad: '))
print('Tu edad es:', edad)
# d) El valor de la variable edad es asignado con el input, y no podemos darle un nuevo valor dentro del
# print.
edad = int(input('Edad: '))
print('Veamos si tu edad es 18…', edad)

#Ejercicio6
#Calcular la media de tres números pedidos por teclado.

num1 = float(input('Ingrese el primer numero: '))
num2 = float(input('Ingrese el segundo numero: '))
num3 = float(input('Ingrese el tercer numero: '))

promedio = (num1 + num2 + num3) / 3
print('El promedio de los numeros ingresados es: ', promedio)

#Ejercicio7
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos
#corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

min = int(input("Ingresar cantidad de minutos"))
cant_h = min/60
cant_min = min % 60
print("Son", int(cant_h), " horas y",cant_min, "minutos" )


#Ejercicio8
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea
#saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el
#total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base= 95000
extra_comision= 15000
total= sueldo_base + (extra_comision * 3)
print(total)

#Ejercicio9
#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto
# deberá pagar finalmente por su compra.

precio_final=float(input("Ingrese el valor total de la compra: "))
print("Precio con descuento: $",precio_final*0.85)

#Ejercicio10
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación
# se compone de los siguientes porcentajes:
#•55% del promedio de sus tres calificaciones parciales.
#•30% de la calificación del examen final.
#•15% de la calificación de un trabajo final.

parcial1= 8.5
parcial2= 4
parcial3= 9
examen_final = 9.25
trabajo_final = 7.5

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
porcentaje_parciales= promedio_parciales * 0.55
porcentaje_examen_final= examen_final * 0.3
porcentaje_trabajo_final = trabajo_final * 0.15
calificacion_final= porcentaje_parciales + porcentaje_examen_final + porcentaje_trabajo_final

print("la calificación final es de: ", calificacion_final)

#Ejercicio11
#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia,
#de modo que el resultado sea siempre positivo).

num_1 = int(input("Ingrese el primer número")) 
num_2 = int(input("Ingrese el segundo número"))
distancia = abs(num_1 -  num_2)
print(distancia)

#Ejercicio12
#Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

numero = float(input('Ingrese un numero: '))
raiz_cuadrada = numero**(1/2)
raiz_cubica = numero**(1/3)

print('La raiz cuadrada es', raiz_cuadrada)
print('La raiz cubica es', raiz_cubica)

#Ejercicio13
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo,
#si se introduce 23 que muestre 32.

numero = (input('Ingrese un numero: '))
numero = int(numero[::-1])
print(numero)

#Ejercicio14
#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo
#que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = input("Coloque un valor para A")
b = input("Coloque un valor para B")
c = a

a = b
b = c
print("Ahora A vale: ", a, "y B vale: ", b )

#Ejercicio15
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta
#llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la
#ciudad B.

hora_partida = int(input("Hora de partida (HH): "))
minuto_partida = int(input("Minuto de partida (MM): "))
segundo_partida = int(input("Segundo de partida (SS): "))
tiempo_viaje = int(input("Tiempo de viaje (T segundos): "))

tiempo_partida_en_segundos = hora_partida * 3600 + minuto_partida * 60 + segundo_partida
tiempo_llegada_en_segundos = tiempo_partida_en_segundos + tiempo_viaje

hh_llegada = tiempo_llegada_en_segundos // 3600
tiempo_llegada_en_segundos %= 3600
mm_llegada = tiempo_llegada_en_segundos // 60
ss_llegada = tiempo_llegada_en_segundos % 60

print("Hora de llegada:", hh_llegada, ":", mm_llegada, ":", ss_llegada)

print("Su horario de llegada fue a las: ")

#Ejercicio16
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Ingresa tu nombre: ")
apellido1 = input("Ingresa tu primer apellido: ")
apellido2 = input("Ingresa tu segundo apellido: ")

print("Iniciales:", nombre[0], apellido1[0], apellido2[0])

#Ejercicio17
#Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario.
#A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.

usuario = input('Ingresa tu nombre: ')
print('Ahora estas en la matrix', usuario)

#Ejercicio18
#Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle
#un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.

cena = float(input("Ingrese el valor de la cena: "))
total = cena + (cena * 0.62) + (cena * .1)
print("El valor total es:",total)

#Ejercicio19
#Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos
# en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato
# dd/mm/aaaa.

fecha = input("Colocar fecha de nacimiento ")
mes = input("Coloque su mes de nacimiento ")
año = input("Coloque su año de nacimiento ")

print(fecha, "/", mes, "/", año)

#Ejercicio20
#Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.

import datetime
fecha_nac = input('Ingrese su fecha de nacimiento en formato dd/mm/yyyy: ')
transformar_fecha = datetime.datetime.strptime(fecha_nac,"%d/%m/%Y" )
print(transformar_fecha.strftime('%d%m%Y'))

#Ejercicio21
#Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para
#saber cuántos tanques de combustible consumirá el viaje entero.
#Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué
#capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
#Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de
#combustible necesarios.

km_por_litro = float(input("Ingresar kilómetros recorridos por litro de combustible"))
capacidad_tanque = float(input("Ingresar cantidad de litros que posee el tanque"))
km_totales = float(input("Ingresar km totales que se van a recorrer"))
tanques_necesarios = km_totales / km_por_litro / capacidad_tanque
print ("son necesarios ",tanques_necesarios, " para realizar el viaje")


