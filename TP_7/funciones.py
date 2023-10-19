# 1 - Burbuja
# Cargar datos a la lista
def list_assembly():
    list_num0=[]
    while True:
        p=int(input("Ingrese un numero (0 para salir): "))
        list_num0.append(p)
        if p==0:
            break
    print (list_num0)
    return list_num0

def ejer1(list_num1):
    n = len(list_num1)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num1[j] > list_num1[j+1]:
                    list_num1[j], list_num1[j+1] = list_num1[j+1], list_num1[j]
    return list_num1

# 4 - Insercion
def insertionSort(li):
    n = len(li)
    if n <= 1:
        return li
    for i in range(1, n):
        key = li[i]
        j = i-1
        while j >= 0 and len(key) < len(li[j]):
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key

# 5 
def ejer5(list_num2):
    n = len(list_num2)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num2[j] < list_num2[j+1]:
                    list_num2[j], list_num2[j+1] = list_num2[j+1], list_num2[j]
    return list_num2

# 6 - Por conteo
def ejer6(list_num6):
    output = [0 for i in range(len(list_num6))]
    count = [0 for i in range(100)]
    for i in list_num6:
        count[i] += 1
    for i in range(1, 100):
        count[i] += count[i-1]
    for i in range(len(list_num6)):
        output[count[list_num6[i]]-1] = list_num6[i]
        count[list_num6[i]] -= 1
    return output

# 7 - Insertion Sort y Bubble Sort
def insertionSort(word_list):
    if len(word_list) <= 1:
        return word_list
    else:    
        for i in range(1, len(word_list)):
            key = word_list[i]
            j = i-1
            while j >= 0 and key < word_list[j]:
                word_list[j+1] =  word_list[j]
                j -= 1
            word_list[j+1] = key
        return word_list

def bubbleSort(number_list):
    n = len(number_list)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if number_list[j] > number_list[j + 1]:
                swapped = True
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
        if not swapped:
            return number_list

# 8 - Merge Sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
 
        mergeSort(sub_array1)
        mergeSort(sub_array2)
           
        i = j = k = 0
 
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
 
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
 
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
 
   
