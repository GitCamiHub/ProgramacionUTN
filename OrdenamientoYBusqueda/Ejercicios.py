import funciones

list_num=funciones.list_assem_num()
list_word=funciones.list_assem_word()

print("Ordenamiento de burbuja")
list_num1=list_num.copy()
print(funciones.ejer1(list_num1))

print("Ordenamiento de selección")
list_word2=list_word.copy()
print("Palabras ordenadas alfabéticamente:", funciones.selection_sort_words(list_word2))

print("Ordenamiento de inserción")
list_word4=list_word.copy()
print("Palabras ordenadas en orden ascendente segun su longitud:",funciones.ejer4(list_word4))

print("Ordenamiento Merge Sort")
list_num8=list_num.copy()
print(funciones.merge_sort(list_num8))

print("Busqueda lineal")
number = int(input("Ingrese el numero a buscar: "))
result = funciones.busqueda_lineal(list_num, number)
if result != -1:
    print(f"El elemento {number} se encuentra en el índice {result}.")
else:
    print(f"El elemento {number} no se encuentra en la lista.")

print("Busqueda binaria")
result2 = funciones.busqueda_binaria(list_num, number)
if result2 != -1:
    print(f"El elemento {number} se encuentra en el índice {result2}.")
else:
    print(f"El elemento {number} no se encuentra en la lista.")