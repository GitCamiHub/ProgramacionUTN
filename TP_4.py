# Ejercicio 1 Ingles

x = 0

while x<=30:
    x+=1
    if x==4 or x==6 or x==10:
        print('The value',x,'of x was skipped')
        continue
    print('The value of the loop is', x)
    if x==15:
        break
print('The execution of the loop was broken when x was',x)

# Ejercicio 1

line = ""

while line != " ":
    line = input('Ingrese una palabra o frase (Vacio para salir): ').upper()
    if line == "":
        break
    print(line)


# Ejercicio 2

option = 'D'
account = 0

while option!='D' or option!='R':
    option = input('Presione D+(espacio)+monto para ingresar dinero o R+(espacio)+monto para retirar: ').upper()
    if option=="":
        break
    elif option[0]=='D':
        split_string = option.split()
        amount = int(split_string[1])
        account += amount
    elif option[0]=='R':
        split_string = option.split()
        amount = int(split_string[1])
        account -= amount
    else:
        print('No existe esa opcion')
   
print('Saldo:', account)


# Ejercicio 3

num = 2
prime_numbers = 0
while num>1:
    counter = 0
    num = int(input('Ingrese un numero entero positivo mayor a 1 (0 para salir): '))
    if num == 0:
        break
    for i in range(1,num+1):
        if num % i == 0:
            counter += 1
    if counter==2:
      print(num,'es primo')
      prime_numbers+=1

print('Se ingresaron',prime_numbers,'numeros primos')


# Ejercicio 4

year1 = int(input('Ingrese un año: '))
year2 = int(input('Ingrese otro año: '))

if year1<year2:
    print('Año bisiesto y multiplo de 10 entre', year1, 'y', year2, ':')
    for i in range(year1, year2+1):
        if i % 10 != 0:
            continue
        elif i % 4 == 0 and (i % 100 != 0 or i%400==0):
            print(i)
     
else:
    print('Año bisiesto y multiplo de 10 entre', year2, 'y', year1, ':')
    for i in range(year2, year1+1):
        if i % 10 != 0:
            continue
        elif i % 4 == 0 and (i % 100 != 0 or i%400==0):
            print(i)


# Ejercicio 5

for i in range(1, 20+1):
    if i % 2 != 0:
        continue
    print(i)

# Ejercicio 6

number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num = int(input("Que numero quiere buscar en la lista? (Del 1 al 20): "))
for i in number_list:
    print(i)
    if  i == num:
        print("Bucle terminado")
        break

# Ejercicio 7

print("Elija una opcion:\n 1. Opcion 1 \n 2. Opcion 2 \n 3. Opcion 3 \n 0. Salir")
yes_no = ''
while True:
    option = int(input("Opcion: "))
    if option == 1 or option == 2 or option == 3:
        print("Estas en la opcion", option)
    elif option == 0:
        print("Saliendo...")
        break
    else:
        print("Elija una opcion correcta.")