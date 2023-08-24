# Ejercicio 1

anhos_pc = float(input("Coloque los años de su computadora "))

if (anhos_pc <= 2):
    print("Su computadora es nueva")
else:
    print("Su computadora es vieja")


# Ejercicio 2

anhos_pc = float(input("Coloque los años de su computadora "))
if (anhos_pc < 0):
    print("Error. Número negativo. ")
elif (anhos_pc <= 2):
    print("Su computadora es nueva")
else:
    print("Su computadora es vieja")


# Ejercicio 3

nom1=input("Ingrese un nombre: ")
nom2=input("Ingrese otro nombre: ")
if nom1[0]==nom2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")


# Ejercicio 4

print('Elija una letra para votar por un partido.')
print('A partido Rojo')
print('B partido Verde')
print('C partido Azul')
voto = input('Ingrese su eleccion: ').lower()
if(voto == 'a'):
    print('Usted ha votado por el partido Rojo')
elif(voto == 'b'):
    print('Usted ha votado por el partido Verde')
elif(voto == 'c'):
    print('Usted ha votado por el partido Azul')
else:
    print('Elija una opcion correcta.')


# Ejercicio 5

letra = input("Ingrese una letra")
if (letra == "a" or letra =="e" or letra == "i" or letra == "o" or letra == "u"):
  print("Es vocal")
elif (letra > "1"):
  print("No es posible procesar el dato")


# Ejercicio 6

anho = int(input("Coloque el año "))

if (anho % 4 == 0):
    print("Es un año bisiesto")
else:
    print("No es año bisiesto")


# Ejercicio 7

num1 = float(input('Ingrese un numero: '))
num2 = float(input('Ingrese un numero: '))
num3 = float(input('Ingrese un numero: '))

if(num1>num2 and num3>num2):
    print(num2, 'es el numero menor.')
elif(num2>num1 and num3>num1):
    print(num1, 'es el numero menor.')
else:
    print(num3, 'es el numero menor.')


# Ejercicio 8

usuario = input("Ingrese usuario")
contraseña = input("Ingrese contraseña")

if (usuario == "Gwenevere" and contraseña == "excalibur"):
  print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
  print("Acceso denegado")


# Ejercicio 9

nombre = input("Ingrese nombre").lower()
sexo = input("Ingrese sexo")

grupo_A = []
grupo_B = []

if ((sexo == "mujer" and nombre < "m") or (sexo == "hombre" and nombre > "m")):
  grupo_A.append(nombre)
  print("Correspondes al grupo A")
else:
  grupo_B.append(nombre)
  print("Correspondes al grupo B")


# Ejercicio 10

edad = int(input('Ingrese su edad: '))
if(edad<4):
    print('Entras gratis!')
elif(edad<=18):
    print('El valor de la entrada es $500')
else:
    print('El valor de la entrada es $1000')


#Ejercicio 11

tipo_pizza = input("Pizzería Bella Napoli. Desea una pizza vegetariana o común? ")

if (tipo_pizza == "vegetariana"):
    ingrediente_vege= str(input("Elija un ingrediente especial para la pizza: -Pimiento -Tofu: ").lower())
    if (ingrediente_vege == "pimiento"):
        print("Pizza vegetariana. Ingredientes: Tomate, mozzarella y pimiento")
    elif (ingrediente_vege == "tofu"):
        print("Pizza vegetariana. Ingredientes: Tomate, mozzarella y tofu")
    else:
        print("Ingrediente especial no seleccionado. Pizza común. Ingredientes: tomate, mozzarella")
elif (tipo_pizza == "comun"):
    ingredientes_comun = str(input("Elija un ingrediente especial para la pizza: -Peperoni, Jamon, -Salmon: ").lower())
    if (ingredientes_comun == "peperoni"):
        print("Pizza común. Ingredientes: Tomate, mozzarella y peperoni")
    elif (ingredientes_comun == "jamon"):
        print("Pizza común. Ingredientes: Tomate, mozzarella y jamón")
    elif (ingredientes_comun == "salmon"):
        print("Pizza común. Ingredientes: Tomate, mozzarella y salmón")
    else: 
        print("Ingrediente especial no seleccionado. Pizza común. Ingredientes: Tomate y mozzarella.")
else:
    print("Tipo de pizza no seleccionada.")


# Ejercicio 12

anio_actual = int(input('Ingrese el año actual: '))
otro_anio = int(input('Ingrese un año cualquiera: '))

if(anio_actual>otro_anio):
    print('Pasaron', anio_actual-otro_anio, 'años desde el', otro_anio)
else:
    print('Faltan', otro_anio-anio_actual, 'años para el', otro_anio)


# Ejercicio 13

num1 = int(input('Ingrese un numero entero: '))
num2 = int(input('Ingrese otro numero entero: '))

if(num1<1 or num2<1):
    print('Numero invalido')
elif(num1>num2):
    if(num1%num2 == 0):
        print(num1,'es multiplo de', num2)
    else:
        print(num1,'NO es multiplo de', num2)
else:
    if(num2%num1 == 0):
        print(num2,'es multiplo de', num1)
    else:
        print(num2,'NO es multiplo de', num1)


# Ejercicio 14

a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
if a!=0:
    x=-1*b/a
    print("x =",x)
else:
    print("Error matematico")


# Ejercicio 15

import math
forma = input('Escriba T para calcular el area del triangulo o C para calcular la del circulo: ').upper()

if(forma=='T'):
    base = float(input('Ingrese la base: '))
    altura = float(input('Ingrese la altura: '))
    print('El area del triangulo es:', base*altura)
elif(forma=='C'):
    radio = float(input('Ingrese el radio: '))
    print('El area del circulo es: ', math.pi*(radio**2))
else:
    print('Ingrese una letra correcta')



# Ejercicio 16

a = int(input("Coloque el primer número "))
b = int(input("Coloque el segundo número "))

tipo_operacion= input("¿Qué tipo de operación desea realizar? -Suma = 1, Resta = 2, Multiplicacion = 3, Division = 4 ").lower()

if tipo_operacion == "1":
    print(a, "+", b, "=", a+b)
elif tipo_operacion == "2":
    print(a, "-", b, "=", a-b)
elif tipo_operacion == "3":
    print(a, "*", b, "=", a*b)
elif tipo_operacion == "4":
    print(a, "/", b, "=", a/b)


# Ejercicio 17
dia = input("Ingrese día de la semana").lower()

if (dia == "lunes"):
  print("Buen día! Hoy es Lunes")
elif (dia == "viernes"):
  print("Buen día! Hoy es Viernes")
elif (dia == "sábado" or dia == "domingo"):
  print("Buen Fin de semana!")
else:
  print("Buen dia! Hoy se cursa doble turno")


# Ejercicio 18

hs=int(input("Ingrese la cantidad de horas trabajadas: "))
valor=int(input("Ingrese el valor de las horas: "))
if hs>48:
    total=valor*hs+(hs-48)*0.1
    print("Su sueldo es de:",total)
else:
    total=valor*hs
    print("Su sueldo es de:",total)


# Ejercicio 19

cant_lapiz = int(input('Cuantos lapices desea comprar: '))

if(cant_lapiz>=1000):
    print('Tiene descuento del 7 porciento. El importe a pagar es $', cant_lapiz*60 - (cant_lapiz*60*0.07))
else:
    print('No tiene descuento. El importe a pagar es $', cant_lapiz*60)


# Ejercicio 20

nota1= int(input("Coloque la primera nota "))
nota2= int(input("Coloque la segunda nota "))
nota3= int(input("Coloque la tercera nota "))
nota4= int(input("Coloque la cuarta nota "))

promedio= (nota1 + nota2+ nota3 + nota4) / 4

if promedio >= 6:
    print(promedio, "Aprobado")
else:
    print(promedio, "Desaprobado")

