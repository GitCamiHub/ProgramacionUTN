print('\nBienvenido a la libreria. Estos son nuestros productos:\n')
# Creo un diccionario -> diccionario = {clave:valor, clave:valor, ...}
product_dic={'Block de hojas': 1500, 'Pote de acrilico': 3000, 'Caja de colores':2600, 'Lapiz':700, 'Goma de borrar':450}
# Lo muestro para que se vean los productos con sus precios
print(product_dic,'\n')

print('Elija el numero correspondiente para elegir un producto, presione 0 para salir.\n')
# Inicializo variables que voy a necesitar mas abajo
num = 0
total = 0
# nombre_del_diccionario.keys() trae todas las claves que tenga el diccionario en forma de CONJUNTO, 
# como quiero una lista le pongo list() adelante y guardo esa lista en una variable
product_list = list(product_dic.keys())

# Todo lo anterior fue solo para poder mostrar los productos en un menu y para usar el for que era obligatorio
for i in product_list:
     # Al num de la linea 9 le sumo 1 en cada vuelta para que muestre el numero de producto desde el 1
     num += 1
     # Esto va a mostrar en la primera vuelta ->  1. Block de hojas
     print(num,'.', i)

while True:
    # Acá la persona elije el producto por el numero que entra como string
    option = input('\nProducto (0 para salir): ' )
    # El error que no encontrabamos era que en vez de poner and poniamos or
    # Van con comillas porque son string
    if option!='1' and option!='2' and option!='3' and option!='4' and option!='5' and option!='0':
        print('Elija una opcion correcta.')
    elif option == '0':
        break
    else:
        # Transformo el numero ingresado a int porque mas abajo necesito hacer una cuenta
        number = int(option)
        # Le pregunto que cantidad del producto que eligio va a querer
        amount = int(input('Cantidad?: '))
        if amount>0:
            # Para poder buscar ese producto en la lista uso lista[posicion del elemento que quiero buscar]
            # Como la primer posicion es 0 si pone 1 va a traer 'Pote de acrilico' en vez de 'Block de hojas'
            # entonces pongo entre los corchetes el numero que eligió menos 1
            actual_product = product_list[number-1]
            # Para buscar el valor de ese producto en el diccionario uso diccionario[clave],
            # si yo tenia diccionario{'Nombre': 'Maria'} y pongo diccionario['Nombre'] me devuelve el valor: Maria.
            # Entonces busco en el diccionario la clave (que la guardé en actual_product), me devuelve el precio 
            # y lo multiplico por la cantidad que quiere la persona
            price = product_dic[actual_product] * amount
            # total lo inicialicé en 0 en la linea 10 y ahi voy sumando en cada vuelta los valores
            total += price
            # Muestro en pantalla cantidad y producto que seleccionó
            print(amount,actual_product)
        else:
            print('La cantidad debe ser mayor a 0, o 0 para salir.')
 
# Una vez que tocó 0 y salió evaluo si el total va a tener envio gratis o no.
if total>6000:
    print('\nTenes envio gratis!!!')
    print('El total es:',total)
else:
    print('\nEl costo de envio es del 10 % de la compra:')
    shipping_cost = total*0.10
    print('El total es:', total + shipping_cost)
    

    
    


