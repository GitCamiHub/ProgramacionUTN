# Ejercicios en clase For - While

# Ejercicio 1

abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
cant_lugares = int(input("Cuantos lugares quiere correr las letras? "))
mensajes = []


for i in range(5):
    mensaje = (input("Ingrese el mensaje: ").upper())
    mensajes.append(mensaje)
    mensaje_encriptado =""
    for j in mensaje:
        for k in j:
            if j != 'Z':
                cambiar_letra = abc[abc.find(j) + cant_lugares]
                mensaje_encriptado += cambiar_letra 
            else:
                cambiar_letra = abc[(abc.find(j)+cant_lugares)%27]
                mensaje_encriptado += cambiar_letra 

    print(mensaje_encriptado)


# Ejercicio 2

digito_par = 0
digito_impar = 0
contador_par = 0
contador_impar = 0

num_ingresado = int(input("Ingresá un numero entero positivo: "))

while num_ingresado != 0:
    num_aux  = num_ingresado
    while num_aux>=1:
        resto = num_aux%10   
        num_aux = int(num_aux/10)

        if resto % 2 == 0:
            digito_par += 1
            contador_par += 1
        else:
            digito_impar += 1
            contador_impar +=1
    print("Este numero tiene", digito_par, "digitos pares y", digito_impar,"digitos impares.")
    digito_par = 0
    digito_impar = 0
    print("=============================================")
    num_ingresado = int(input("Ingresá otro numero entero positivo: "))
   

print("Numeros pares ingresados:", contador_par)
print("Numeros impares ingresados:", contador_impar)






