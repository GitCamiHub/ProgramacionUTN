from Person import Person
from Account import Account
from Contact import Contact
from Triangulo import Triangulo

# Ejercicio 1
person = Person()
person.create_person()
print(f'Es mayor de edad? {person.es_mayor()}')
person.mostrar()

# Ejercicio 2
person1 = Person('Carlos',54,24505612)
client1 = Account(person1)
client1.mostrar()
client1.ingresar(500.5)
client1.mostrar()
client1.ingresar(-500)
client1.mostrar()
client1.retirar(100)
client1.mostrar()

# Ejercicio 3
ingreso1 = int(input("Coloque el valor del primer lado: "))
ingreso2 = int(input("Coloque el valor del segundo lado: "))
ingreso3 = int(input("Coloque el valor del tercer lado: "))

triang1 = Triangulo(ingreso1, ingreso2, ingreso3)

#Accedemos a los atributos del objeto
print(f' Valor lado 1: {triang1.lado1}, Valor lado 2: {triang1.lado2}, Valor lado 3: {triang1.lado3}')

triang1.imprimir_lado_mayor()
triang1.determinar_tipo_triangulo()



# Ejercicio 4
user = Contact()
contact_list = []
while True: 
    print('\n1. Añadir contacto\n2. Lista de contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda')
    option = input('Elija una opcion: ')
    if option in ('1','2','3','4','5'):
        if option == '1':
            contact_list = user.add_contact(contact_list)
        elif option == '2':
            user.show_list(contact_list)
        elif option == '3':
            user.contact_search(contact_list)
        elif option == '4':
            user.edit_contact(contact_list)
        else:
            print('Agenda cerrada.')
            break
    else:
        print('Elija una opcion correcta.')








