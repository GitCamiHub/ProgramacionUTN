class Person:

    def __init__(self,name='',age='',dni=''):
        self.__name = name
        self.__age = age
        self.__dni = dni

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name

    # Validar datos
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age = age

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,dni):
        self.__dni = dni

    def create_person(self):
        self.name = input('Ingrese su nombre: ')
        self.age = int(input('Edad: '))
        self.dni = int(input('Dni: '))

    def mostrar(self):
        print(f'Nombre: {self.name}\nEdad: {self.age}\nDni: {self.dni}')

    def es_mayor(self):
        if self.age >= 18:
            return True
        else:
            return False