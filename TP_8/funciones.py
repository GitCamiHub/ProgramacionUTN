#1 fun
def dig(num,coun=0):
    while True:
        if num<1:
            if coun==0:
                coun= coun+1
                return coun
            return coun
        else:
            num=num//10
            coun= coun+1
            return dig(num,coun)

#2 fun
def num_power(num_b, num_n):

    if num_n < num_b:
        return False
    if num_n == num_b:
        return True
    if num_n % num_b == 0:
        return num_power(num_b,(num_n//num_b))
    return False
   
#3 fun
def positions_strings(a, b, start=0, result=None):
    if result is None:
        result = []

    index = a.find(b, start)
    if index != -1:
        result.append(index)
        positions_strings(a, b, index + 1, result)
    return result


# 4 fun
def even(num):
    if num == 0:
        return True
    else:
        return odd(num-1)


def odd(num):
    if num == 0:
        return False
    else:
        return even(num-1)


# 5 fun
def greater_element(numbers_list, position,greater_number):
    if position==len(numbers_list):
        return greater_number
    else:
        if position == 0:
            greater_number = numbers_list[0]
            return greater_element(numbers_list,position+1,greater_number)
        else:
            if greater_number<numbers_list[position]:
                greater_number = numbers_list[position]
                return greater_element(numbers_list,position+1,greater_number)
            else:
                return greater_element(numbers_list,position+1,greater_number)
            

# 6 fun
def repeat(li,times,new_li):
    counter=len(li)
    if times==0:
        return new_li.sort()
    else:
        add_elements(li,counter,times,new_li)
 
def add_elements(li,counter,times,new_li):
    if counter == 0:
        repeat(li,times-1,new_li)
    else:
        element = li[len(li)-counter]
        new_li.append(element)
       
        add_elements(li,counter-1,times,new_li)

# 7 fun
def mul(n,p,res=0):
    while True:
        if n==0:
            return res
        else:
            res=res+(p*n)
            n=n-1
            return mul(n,p,res)

# 8 fun
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

# 9 fun
def combinations(lista, k, prefix=""):
    if k == 0:
        print(prefix)
        return 
    for char in lista:
        combinations(lista, k - 1, prefix + char)

# 10 fun
def sheet(paper,a=0,long=841,broad=1189):
    while True:
        if a==paper:
            return long,broad
        else:
            a=a+1
            if a%2==0:
                long=long//2
            else:
                broad=broad//2
            return sheet(paper,a,long,broad)



