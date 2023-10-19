import funciones
import random

# Ejercicio 1
list_num=funciones.list_assembly()
list_num1=list_num.copy()
print(funciones.ejer1(list_num1))

# Ejercicio 2
def selection_sort_words(word):
    len_word = len(word)
   
    for i in range(len_word - 1):
        # Suponemos que el elemento actual es el mínimo
        min_index = i
       
        # Comparamos con el resto de elementos para encontrar el mínimo alfabéticamente
        for j in range(i + 1, len_word):
            if word[j] < word[min_index]:  # Comparamos las cadenas
                min_index = j
       
        # Intercambiamos el mínimo encontrado con el elemento en la posición i
        word[i], word[min_index] = word[min_index], word[i]

# Ejemplo de uso
list_ordered = ["Sofi", "Arnold", "Camila", "Gian", "Gaby"]
selection_sort_words(list_ordered)
print("Palabras ordenadas alfabéticamente:", list_ordered)


# Ejercicio 3
library = [{'titulo': 'Harry Potter y la Piedra Filosofal', 'autora': 'JK Rowling', 'año de publicacion': '1997'},
        {'titulo': 'Harry Potter y la Camara secreta', 'autora': 'JK Rowling', 'año de publicacion': '1998'},
        {'titulo': 'Harry Potter y el prisionero de Azkaban', 'autora': 'JK Rowling', 'año de publicacion': '1999'},
        {'titulo': 'Harry Potter y el Caliz de fuego', 'autora': 'JK Rowling', 'año de publicacion': '2000'},
        {'titulo': 'Harry Potter y la Orden del Fenix','autora': 'JK Rowling', 'año de publicacion': '2003'}
        ]
year_of_publication = []
for book in library:
        year_of_publication.append(book['año de publicacion'])

print(year_of_publication)

# Ejercicio 4
words = []
while True:
    words_input = input("Ingrese palabras (0 para salir): ")
    if words_input == '0':
        break
    elif words_input.isalpha():
        words.append(words_input)
    else:
        print("Ingrese una palabra.")

funciones.insertionSort(words)
print("Palabras ordenadas en orden ascendente segun su longitud: ", words)

# Ejercicio 5
list_num5=list_num.copy()
print(funciones.ejer5(list_num5))

# Ejercicio 6
list_num6=list_num.copy()
print(funciones.ejer6(list_num6))

# Ejercicio 7
words_and_numbers = []
words =[]
numbers = []
   
while True:
    list_input = input("Ingrese numeros y palabras (0 para salir): ").lower()
    if list_input == '0':
        break
    else:
        words_and_numbers.append(list_input)
   
for element in words_and_numbers:
    if element.isalpha():
        words.append(element)
    else:
        numbers.append(int(element))

words_and_numbers = funciones.bubbleSort(numbers) + funciones.insertionSort(words)
print("Números ordenados de menor a mayor y cadenas ordenadas alfabéticamente: ", words_and_numbers)

# Ejercicio 8
while True:
    num = int(input("Ingrese cuantos numeros tendrá la lista (Entre 1 y 20): "))
    if num<1 or num>20:
        print("Ingrese numeros entre 1 y 20.")
    else:
        break

numbers_list = [0]*num

for i in range(num):
    numbers_list[i] = random.randint(1,200)

print("Lista desordenada: ")
for i in numbers_list:
    print(i,end=" ")

print("\nLista ordenada con Merge Sort: ")
funciones.mergeSort(numbers_list)
for i in numbers_list:
    print(i,end=" ")