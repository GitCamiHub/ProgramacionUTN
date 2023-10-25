import funciones

# Ejercicio 1
num=int(input("Ingrese un numero: "))
print("Cantidad de digitos:",funciones.dig(num))


# Ejercicio 2
num_b = int(input("Ingrese un número entero: "))
num_n = int(input("Ingrese otro número entero para verificar si es potencia del anterior: "))

result = funciones.num_power(num_b, num_n)
print(result)

# Ejercicio 3
string_a = "Hola que tal como estas"
string_b = "a"
print(funciones.positions_strings(string_a, string_b))

# Ejercicio 4
while True:
    num = int(input("Ingrese un numero natural: "))
    if num<1:
        print("Ingrese un numero natural.")
    else:
        break
if funciones.even(num) == True:
    print ("El numero es par")
else:
    print("El numero es impar")

# Ejercicio 5
numbers_list = []
while True:
    number = int(input('Ingrese numeros enteros a la lista (0 para terminar): '))
    if number == 0:
        break
    else:
        numbers_list.append(number)

print(numbers_list)
position=0
greater_num = 0
print(f'El mayor numero ingresado es {funciones.greater_element(numbers_list,position,greater_num)}')

# Ejercicio 6
numbers_list = [1,2,3,4,5,6,7]
new_list=[]
print(numbers_list)
repeat_n_times = int(input('Cuantas veces quiere replicar los elementos de la lista?: '))
size = len(numbers_list)


funciones.repeat(numbers_list,repeat_n_times,new_list)


print(new_list)

# Ejercicio 7

while True:
    n=int(input("Ingrese un numero n: "))
    p=int(input("Ingrese un numero p: "))
    if n>0 and p>0:
        break
    else:
        print("No puede ingresar 0")
print("Resultado:",funciones.mul(n,p))

# Ejercicio 8

row = int(input("Coloque el valor de la fila: "))
column = int(input("Coloque el valor de la columna: "))
result = funciones.pascal(row, column)
print(f"El valor en la fila {row} y la columna {column} es: {result}")

# Ejercicio 9
char_list= []
while True:
    characters = input('Ingrese distintos caracteres (0 para terminar): ')
    if characters == '0':
        break
    else:
        char_list.append(characters)

len_combination = int(input('Ingrese la longitud de las cadenas a combinar: '))

print(funciones.combinations(char_list, len_combination))

# Ejercicio 10
paper = int(input("Ingrese el numero de la hoja: A"))
print("Las medidas de las hojas A",paper,"son:",funciones.sheet(paper))

