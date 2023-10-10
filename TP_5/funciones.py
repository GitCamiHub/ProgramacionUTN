import math

#1
def document(dni) :
    if (len(dni)>=7 and len(dni)<=8):
        dni_correct = True
    else:
        dni_correct = False
    return dni_correct

#2
def leng_last_word(chain):
    chain = chain.strip()
    word = chain.split()
    if word:
        last_word = word[-1]
        return len(last_word)
    else:
        return 0

#3
def user_name (name1, name2, lastname):
    fullname = ""
    if (name2 == "0"):
        fullname = name1 + " " + lastname
    else:
        fullname = name1 + ", " + name2 + ", " + lastname
    return ("Nombre del usuario: " + fullname)

# 4
def is_multiple(num1,num2):
    if num1 % num2 == 0 and num2 % num1 != 0:
        return num1
    elif num2 % num1 == 0 and num1 % num2 != 0:
        return num2
    elif num2 % num1 == 0 and num1 % num2 == 0:
        return True
    else:
        return False

def data_validation(num):
    if num<=0:
        print("Ingrese un numero entero mayor a 0.")
        return False
    else:
        return True

#5
def temperature_middle(min_temperature, max_temperature):
    med_temperature = (min_temperature + max_temperature)/2
    return med_temperature


#6
def separator(sentence):
    item=" "
    sentence_separate = item.join(sentence)
    return sentence_separate


# 7 
def max_min(number_list):
    min_number = number_list[0]
    max_number = number_list[0]
    for i in number_list:
        if i>max_number:
            max_number = i
        elif i<min_number and i!=0:
            min_number = i
    return [max_number,min_number]

#8
def calculo_perim(n):
    perimetro=2*n*math.pi
    return perimetro
def calculo_area(n):
    area=(math.pi*n)**2
    return area
# 9
def login(username, password, attempts):
    if username == "usuario1" and password == "asdasd":
        return True
    else:
        attempts += 1
        return attempts   

# 10 
def total(shopping_dic):
    prices_list=[]
    discount_list=[]
    values_list=[]  

    for i in shopping_dic.keys():
        prices_list.append(i)
   
    for i in shopping_dic.values():
        values_list+=i.split('%')
        discount_list.append(i)

    for i in values_list:
        if i =="":
            values_list.remove(i)
     
    num = [int(i) for i in values_list]

    total_with_discount = 0
    total = 0
    number = len(prices_list)
   
    for i in range(number):
        total_with_discount += prices_list[i] - prices_list[i]*(num[i]/100)
        total += prices_list[i]

    return [total, total_with_discount]

#11
def apply_function(product, numbers):
    result = []
    for number in numbers:
        result.append(product(number))
    return result


def product(element):
    return element * 2

#12
def define_keys(all_keys):
    for sing_key in all_keys:
        list_keys = [sing_key]
    return(all_keys)

def transform_dict(all_words):
    dict_text = {}
    for word in all_words:
        dict_text [word] = len(word)
    return(dict_text)

#13
def vector_module (a,b,c):
    module = math.sqrt(a**2 + b**2 + c**2)
    return module

#14
def es_primo(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
        else:
            return True

#15
def factorial(n):
    if n==0 or n==1:
            result=1
    elif n>1:
            result=n*factorial(n-1)
    return result

#16
def frecuency(number, digit):
    counter = 0
    while number > 0:
        aux_number = number % 10
        if digit == aux_number:
            counter = counter + 1
            number = number // 10
        return counter

#17
def addiging_digits(number):
    add_numbers = 0
    while number > 0:
        aux_number = number % 10
        add_numbers = add_numbers + aux_number
        number = number // 10
    return add_numbers

def frecuency(number, digit):
    counter = 0
    while number > 0:
        aux_number = number % 10
        if digit == aux_number:
            counter = counter + 1
            number = number // 10
    return counter

  