# Cargar datos lista numeros
def list_assem_num():
    list_num0=[]
    while True:
        p=int(input("Ingrese un numero (0 para salir): "))
        if p==0:
            break
        list_num0.append(p)
    print (list_num0)
    return list_num0


# Cargar datos lista palabras
def list_assem_word():
    list_word0=[]
    while True:
        p=str(input("Ingrese una palabra (vacio para salir): "))
        if p==" ":
            break
        elif p.isalpha():
            list_word0.append(p)
        else:
            print("Ingrese una palabra.")
    print (list_word0)
    return list_word0


# Busqueda lineal
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


# Busqueda binaria
def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def ejer1(list_num1):
    n = len(list_num1)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num1[j] > list_num1[j+1]:
                    list_num1[j], list_num1[j+1] = list_num1[j+1], list_num1[j]
    return list_num1

def selection_sort_words(list_word2):
    len_word = len(list_word2)
    for i in range(len_word - 1):
        min_index = i
        for j in range(i + 1, len_word):
            if list_word2[j] < list_word2[min_index]:
                min_index = j
        list_word2[i], list_word2[min_index] = list_word2[min_index], list_word2[i]
    return list_word2

def ejer4(strings):
    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        while j >= 0 and len(key) < len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
    return strings

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
