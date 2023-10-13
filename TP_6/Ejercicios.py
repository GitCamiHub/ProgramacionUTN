import funciones

# EJERCICIO 1
numbers_list_original = list()
entry = 1
while entry != 0:
    numbers = int(input("Ingrese números enteros. Pulse 0 para salir "))
    if numbers == 0:
        break
    else:
        numbers_list_original.append(numbers)
print("Tu lista de números: ", numbers_list_original)

# EJERCICIO 2
# Crearé una copia de la lista original
new_number_list = list(numbers_list_original)
number_in_the_list = int(input("Coloque un número entero distinto de 0. Si el número que colocaste se encuentra en la lista, lo eliminaremos "))
trigger = 0
while trigger == 0:
    for i in new_number_list:
        if i == number_in_the_list:
            del new_number_list[i - 1]
            trigger = 1
        else:
            trigger = 2
    if trigger == 2:
        print("El número no se encuentra en la lista")          
print(new_number_list)

# EJERCICIO 3
numbers_addition = 0
for i in new_number_list:
    numbers_addition = numbers_addition + i
print("la suma de los números de la lista es de: " , numbers_addition)

# EJERCICIO 4
other_number = int(input("Ahora, ingrese otro número "))
new_number_list2 = list()
for i in numbers_list_original:
    if i < other_number:
        new_number_list2.append(i)
print("Números de la lista menores al número que designaste: ", new_number_list2)

# EJERCICIO 5
# Crearé un diccionario para contar la frecuencia de cada número
count_dictionary = {}
for number in numbers_list_original:
    if number in count_dictionary:
        count_dictionary[number] += 1
    else:
        count_dictionary[number] = 1
# Ahora convertimos el diccionario en una lista de tuplas
new_list_with_tuples = [(key, value) for key, value in count_dictionary.items()]
print(new_list_with_tuples)

# EJERCICIO 6
elementary_students_list = []
print("Ingrese solo los nombres de los alumnos de la primaria, para terminar presione 'x'.")
while True:
    e_student = input("Alumno: ")
    if e_student in ('x','X'):
        break
    if e_student.isalpha():
        elementary_students_list.append(e_student)
    else:
        print("Ingrese un nombre válido.")

highschool_students_list = []
print("Ingrese solo los nombres de los alumnos de la secundaria, para terminar presione 'x'.")
while True:
    h_student = input("Alumno: ")
    if h_student in ('x','X'):
        break
    if h_student.isalpha():
        highschool_students_list.append(h_student)
    else:
        print("Ingrese un nombre válido.")

# Punto 1
print("\nLos nombres del nivel primario sin repetir son: ")
e_student_set = set(elementary_students_list)
for student in e_student_set:
    print(student)
print("\nLos nombres del nivel secundario sin repetir son: ")
h_student_set = set(highschool_students_list)
for student in h_student_set:
    print(student)

# Punto 2
repeated_names = funciones.repeated_name(e_student_set,h_student_set)
print("\nLos nombres repetidos entre la primaria y la secundaria son: ")
if repeated_names == set():
    print("No hay nombres repetidos.")
else:
    for i in repeated_names:
        print(i)

# Punto 3
non_repeated_names = set()
print("\nLos nombres de la primaria que no se repiten en la secundaria son: ")
for i in e_student_set:
    if i not in repeated_names:
        non_repeated_names.add(i)
if non_repeated_names == set():
    print("No hay nombres repetidos.")
else:
    for i in non_repeated_names:
        print(i)

# EJERCICIO 7
char_occu = {}
print("Ingrese 50 frases para ver las ocurrencias de cada caracter: ")
for i in range(50):
    text = input("Ingresa una frase: ")
    for character in text:
        if character in char_occu:
            char_occu[character] += 1
        else:
            char_occu[character] = 1
for character, amount in char_occu.items():
    print(f"'{character}': {amount}")

# EJERCICIO 8
goals = [
    ['Goles FC',1,2,3,4,5,6,7,8,9,10],
    [1,0,4,2,1,0,3,1,0,2,0],
    [2,5,0,3,2,1,0,3,1,2,1],
    [3,0,2,0,1,3,0,1,2,0,0],
    [4,1,0,2,0,3,2,1,0,3,3],
    [5,0,1,2,1,0,0,1,0,0,1],
    [6,1,2,2,2,3,0,1,0,1,3],
    [7,2,3,3,2,1,0,0,1,2,0],
    [8,1,0,0,2,1,2,3,0,3,2],
    [9,0,1,4,2,1,1,3,1,0,1],
    [10,3,0,2,2,1,0,3,2,2,0],
]

num_rows = len(goals)
num_cols = len(goals[0])

# Mostrar cuadro de goles
max_cell_width = max(len(str(cell)) for row in goals for cell in row)
print()
for i in range(num_rows):
    for j in range(num_cols):
        cell_value = goals[i][j]
        print(f'{cell_value:>{max_cell_width}}', end=' ')
    print()  
print("-------------------------------------------------------------------------------------------------------------")
while True:
    team = int(input("\nIngrese el numero del equipo (del 1 al 10) para ver:\n1.Resultados\n2.Diferencia de goles\n3.Puntos obtenidos\nPresione 0 para salir.\nEquipo: "))
    if team in (1,2,3,4,5,6,7,8,9,10):
        # Mostrar partidos ganados, empatados y perdidos
        results = funciones.games_results(goals,num_cols,team)
        print(f"\n{results[0]} partidos ganados, {results[1]} empatados y {results[2]} perdidos.")
        print("-------------------------------------------------------------------------------------------------------------")
        # Diferencia entre el total de goles marcados y el total de goles recibidos
        goal_count = funciones.goals_dif(goals,num_cols,num_rows,team)
        print(f"Goles marcados: {goal_count[0]}\nGoles recibidos: {goal_count[1]}\nDiferencia: {goal_count[0]-goal_count[1]}")
        print("-------------------------------------------------------------------------------------------------------------")
        # Puntos obtenidos por cada equipo
        points_count = funciones.points(results)
        print(f"El total de puntos obtenidos es {points_count}")
        print("-------------------------------------------------------------------------------------------------------------")
    elif team == 0:
        break 
    else:
        print("Ingrese un equipo correcto. ")


# EJERCICIO 9
import random
def create_board(rows, columns):
    numbers = list(range(1, rows * columns // 2 + 1))
    cards = numbers + numbers
    random.shuffle(cards)
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            card = cards.pop()
            row.append(card)
        board.append(row)
    return board

def print_board(board, rows, columns, pairs_found):
    for i in range(rows):
        for j in range(columns):
            if (i, j) in pairs_found:
                print(f'{board[i][j]:2}', end=' ')
            else:
                print('X', end=' ')
        print()

def memory_game(rows, columns):
    board = create_board(rows, columns)
    pairs_found = set()
    attempts = 0

    while len(pairs_found) < rows * columns // 2:
        print_board(board, rows, columns, pairs_found)
        print("\nIngresa las coordenadas de dos cartas (ejemplo: '0 1 1 2'): ")
        input_str = input().split()

        if len(input_str) != 4:
            print("Debes ingresar dos pares de coordenadas.")
            continue

        try:
            row1, col1, row2, col2 = map(int, input_str)
            if (
                0 <= row1 < rows
                and 0 <= col1 < columns
                and (row1, col1) not in pairs_found
            ):
                card1 = board[row1][col1]
            else:
                print("Coordenadas inválidas o carta ya emparejada.")
                continue
        except ValueError:
            print("Coordenadas inválidas.")
            continue

        if (
            0 <= row2 < rows
            and 0 <= col2 < columns
            and (row2, col2) not in pairs_found
        ):
            card2 = board[row2][col2]
        else:
            print("Coordenadas inválidas o carta ya emparejada.")
            continue

        if card1 == card2:
            print("¡Encontraste un par!")
            pairs_found.add((row1, col1))
            pairs_found.add((row2, col2))
        else:
            print("Las cartas no son iguales. Inténtalo de nuevo.")

        attempts += 1

    print_board(board, rows, columns, pairs_found)
    print(" Felicidades! Has encontrado todas las parejas en {attempts} intentos.")

if __name__ == "__main__":
    rows = 4
    columns = 4
    memory_game(rows, columns)

# EJERCICIO 10
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for row in range(len(matrix)):
    print(matrix[row])
# a
print("\nDiagonal principal: ")
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if row == column:
            print(matrix[row][column], end=" ")
# b
print("\nDiagonal inversa: ")
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if row + column == len(matrix)-1:
            print(matrix[row][column], end=" ")
            
# EJERCICIO 11
currency = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
badge = input("Ingrese una divisa: ").lower().title()
if badge in currency:
    if badge == 'Euro':
        print(currency['Euro'])
    elif badge == 'Dollar':
        print(currency['Dollar'])
    elif badge == 'Yen':
        print(currency['Yen'])
else:
    print("La divisa no se encuentra en el diccionario")

# EJERCICIO 12
user_data = {'name':'', 'age':'', 'address':'', 'phone_number':''}
user_data['name'] = input('Ingrese su nombre: ')
user_data['age'] = int(input('Ingrese su edad: '))
user_data['address'] = input('Ingrese su dirección: ')
user_data['phone_number'] = input('Ingrese número de teléfono: ')
print(f"{user_data.get('name')} tiene {user_data.get('age')} años, vive en {user_data.get('address')} y su número de teléfono es {user_data.get('phone_number')}.")

# EJERCICIO 13
fruit_prices = {
    "manzana": 500,
    "banana": 800,
    "naranja": 400,
    "pera": 450,
    "uva": 550,
}
fruit = input("Ingresa el nombre de la fruta: ").lower()
kg = float(input("Ingresa la cantidad de kilos: "))


if fruit in fruit_prices:
    total_price = fruit_prices[fruit] * kg
    print(f"El precio de {kg} kilos de {fruit} es: ${total_price:}")

