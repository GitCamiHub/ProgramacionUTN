def most(a,b):
    if(x>y):
        return a # Cambiamos la variable 'x' por 'a' para que muestre 2, porque 'x' 
                 # es una variable global cuyo valor es 5.
    else:
        return y

def least(a,b):
    if (x<y):
        return x
    else:
        return y
    
x = int(input("Un numero: "))
y = int(input("Otro numero: "))

print(most(x-3,least(x+2,y-5)))