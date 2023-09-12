print('\nBienvenido a la libreria. Estos son nuestros productos:\n')

product_dic={'Block de hojas': 1500, 'Pote de acrilico': 3000, 'Caja de colores':2600, 'Lapiz':700, 'Goma de borrar':450}

print(product_dic,'\n')

print('Elija el numero correspondiente para elegir un producto, presione 0 para salir.\n')

num = 0
total = 0

product_list = list(product_dic.keys())

for i in product_list:
     num += 1
     print(num,'.', i)

while True:
    option = input('\nProducto (0 para salir): ' )
    if option!='1' and option!='2' and option!='3' and option!='4' and option!='5' and option!='0':
        print('Elija una opcion correcta.')
    elif option == '0':
        break
    else:
        number = int(option)
        amount = int(input('Cantidad?: '))
        if amount>0:
            actual_product = product_list[number-1]
            price = product_dic[actual_product] * amount
            total += price
            print(amount,actual_product)
        else:
            print('La cantidad debe ser mayor a 0, o 0 para salir.')
 
if total>6000:
    print('\nTenes envio gratis!!!')
    print('El total es:',total)
else:
    print('\nEl costo de envio es del 10 % de la compra:')
    shipping_cost = total*0.10
    print('El total es:', total + shipping_cost)
    

    
    


