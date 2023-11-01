class Contact:

    def __init__ (self,name='',tel=0,email=''):
        self.__name = name
        self.__tel = tel
        self.__email = email

    # Getter
    @property
    def name(self):
        return self.__name
    # Setter
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def tel(self):
        return self.__tel
    
    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email


    def add_contact(self, contact_list):
        name = input('Nombre: ').lower()
        tel = int(input('Telefono: '))
        email = input('Mail: ')
        new_contact = Contact(name, tel, email)
        contact_list.append(new_contact)
        return contact_list


    def show_list(self,contact_list):
        for i in contact_list:
            print(f'\n{i.name}\n{i.tel}\n{i.email}')

    def contact_search(self,contact_list):
        person = input('Ingrese el nombre del contacto que quiere buscar: ').lower()
        counter = 0
        for i in contact_list:
            if i.name == person:
                print(f'Nombre: {i.name}\nTelefono: {i.tel}\nMail: {i.email}')
                counter +=1
        if counter == 0:
            print('\nEl nombre ingresado no se encuentra en la lista de contactos.')
            
    def edit_contact(self,contact_list):
        contact_name = input('Ingrese el nombre del contacto para editarlo: ').lower()
        counter = 0
        for i in contact_list:
            if i.name == contact_name:
                print(f'Nombre: {i.name}\nTelefono: {i.tel}\nMail: {i.email}')
                while True:
                    print('\n1. Editar nombre\n2. Editar teléfono\n3. Editar mail\n4. Salir')
                    option = input('Opcion: ')
                    if option in ('1','2','3','4'):
                        if option == '1':
                            new_name = input('Nombre: ')
                            i.name = new_name
                            print('\nContacto editado!')
                            print(f'Nombre: {i.name}\nTelefono: {i.tel}\nMail: {i.email}')
                        elif option == '2':
                            new_tel = int(input('Telefono: '))
                            i.tel = new_tel
                            print('\nContacto editado!')
                            print(f'Nombre: {i.name}\nTelefono: {i.tel}\nMail: {i.email}')
                        elif option == '3':
                            new_email = input('Mail: ')
                            i.email = new_email
                            print('\nContacto editado!')
                            print(f'Nombre: {i.name}\nTelefono: {i.tel}\nMail: {i.email}')
                        elif option == '4':
                            print('Saliendo.')
                            break
                    else:
                        print('Elija una opcion correcta.')
                    counter +=1
        if counter == 0:
            print('\nEl nombre ingresado no se encuentra en la lista de contactos.')


