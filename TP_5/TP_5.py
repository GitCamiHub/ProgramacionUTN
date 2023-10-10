import funciones
# EJERCICIO 1
import funciones  
document_num = input("Ingrese su numero de documento: ")
if ( funciones.document(document_num)):
    print("la longitud es correcta")
else:
    print("longitud incorrecta")

# EJERCICIO 2
chain = str(input("Ingrse una frase: "))
result = funciones.leng_last_word(chain)
print("Longitud de la última palabra:", result)

# EJERCICIO 3
first_name = input("Ingresar nombre de pila: ")
second_name = input("Ingresar segundo nombre, de no tenerlo ingrese 0: ")
last_name = input("Ingresar apellido: ")
last_name_long = len(last_name)
dni = ""
dni_3_digits = 0
print(funciones.user_name(first_name, second_name, last_name))
dni = input("Ingrese su DNI: ")
while(len(dni) != 7 and len(dni) != 8):
    dni = input("DNI inválido. Ingrese el correcto: ")


dni_3_digits = dni[:3]


final_id = "ID: " + first_name + str(last_name_long) + str(dni_3_digits)
print(final_id)


# EJERCICIO 4
number1 = int(input("Ingrese un numero entero: "))
while funciones.data_validation(number1) == False:
    number1 = int(input("Ingrese un numero entero: "))
number2 = int(input("Ingrese otro numero entero: "))
while funciones.data_validation(number2) == False:
    number2 = int(input("Ingrese otro numero entero: "))

multiple = funciones.is_multiple(number1,number2)
if multiple == number1:
    print(number1,"es multiplo de",number2)
elif multiple == number2:
    print(number2,"es multiplo de",number1)
elif multiple == True:
    print("Son multiplos.")
elif multiple == False:
    print("No son multiplos.")

# EJERCICIO 5
days = int(input("de cuantos dias desea saber la temperatura media"))

for day in range(days):
    min_tem = int(input("Cual es la temperatura minima?: "))
    max_tem = int(input("Cual es la temperatura maxima?: "))
    print("la temperatura media es ",funciones.temperature_middle(min_tem, max_tem),"º")

# EJERCICIO 6
sentence = input("INGRESE FRASE: ")
print("la frase separada es ", funciones.separator(sentence))

# EJERCICIO 7
num=1
numbers_list = []
while num!=0:
    print("Ingrese sucesivamente numeros enteros (0 para terminar).")
    num=int(input("Numero: "))
    numbers_list.append(num)

values = funciones.max_min(numbers_list)
print(f'El mayor número de la lista es {values[0]} y el menor es {values[1]}')

# EJERCICIO 8
radio = float(input("Ingrese el radio del circulo: "))
perimetro = funciones.calculo_perim(radio)
area = funciones.calculo_area(radio)
print("Perimetro:",perimetro)
print("Area:",area)

# EJERCICIO 9
attempts = 0
while attempts <= 3:
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    if funciones.login(username, password, attempts) is True:
        print("Inicio de sesión exitoso!")
        break
    else:
        attempts = funciones.login(username, password, attempts)
        remaining_attempts = 3 - attempts
        if remaining_attempts > 0:
            print("Inicio de sesión fallido. Intentos restantes: ", remaining_attempts)
        else:
            print("Se han agotado los intentos de inicio de sesión.")
            break

# EJERCICIO 10
shopping_cart = {3500: '20%', 14200: '35%', 5700: '10%', 12000: '20%', 7800: '10%'}

print("Su carrito de compras con precio y descuento a aplicar es:")
print(shopping_cart)

while True:
    choise = input("Presione T para ver el total con el descuento aplicado y C para cancelar la compra: ").upper()
    if choise == 'T':
        total_list = funciones.total(shopping_cart)
        print(f'El total de la compra es: ${total_list[0]}. Con el descuento aplicado es ${total_list[1]}')
        break
    elif choise == 'C':
        print("Compra cancelada")
        break
    else:
        print("Ingrese una opcion correcta")

# EJERCICIO 11
numbers = [4,2,8,9,6]
print("-- primer lista --")
for number in numbers:
    print(number)
new_numbers = funciones.apply_function(funciones.product, numbers)
print("-- segunda lista --")
for number in new_numbers:
    print(number)

# EJERCICIO 12
phrase = input("Ingrese una frase: ")
words = phrase.split(" ")
keys = (funciones.define_keys(words))
print(funciones.transform_dict(words))

# EJERCICIO 13
vector = []
prompt = 1
while (prompt >= 1 and prompt <= 3):
    prompt += 1
    digit = input("Ingrese valor del vector")
    vector.append(digit)
print("El módulo del vector es: " , funciones.vector_module(int(vector[0]), int(vector[1]), int(vector[2])))

# EJERCICIO 14
num = int(input("Ingrese un numero: "))
if funciones.es_primo(num) == True:
    print(num,"es un numero primo")
else:
    print(num,"no es un numero primo")

# EJERCICIO 15
cont=0
while True:
    number=int(input("Ingrese un numero (0 para salir): "))
    cont+=1
    if number == 0:
        print("Has ingresado",cont-1,"numeros")
        break
    else:
        fact5  = funciones.factorial(number)
        print("El factorial de",number,"es:",fact5)

# EJERCICIO 16
number = int(input("Ingrese un número entero "))
digit = int(input("Ingrese un digito "))
print("La cantidad de veces que se repite el número ", digit, " es de:", funciones.frecuency(number, digit))

# EJERCICIO 17
while True:
    number = int(input('Ingrese un número primo. Para salir, ingrese un no primo '))
    digit = int(input('Ingrese un dígito '))
    #Seccion para saber si el número primo ingresado es el más grande
    major_number = 0
    if number > major_number:
        major_number = number

    #Sección verificación números primos
    counter = 0
    for i in range(1,number+1):
        if number % i == 0:
            counter += 1
    if counter==2:
      print(number,'es primo')
      print('La suma es: ', funciones.addiging_digits(number))
      print('Las veces que se repite el dígito ', digit, ' son ' , funciones.frecuency(number, digit), ' veces')
    else:
        print("No es un número primo")
    break                

#Sacar el factorial del mayor primo ingresado
factorial = 1
for i in range (1, major_number + 1):
    factorial *= 1
print(f"El factorial de {major_number} es {factorial}")