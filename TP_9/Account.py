
class Account:
    
    def __init__ (self,titular,cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print(f'Titular: {self.titular.name}\nCantidad: ${self.cantidad}')

    def ingresar(self,cantidad):
        if cantidad>0:
            self.__cantidad += cantidad
    
    def retirar(self,cantidad):
        self.__cantidad -= cantidad