import pickle

class Vehiculos:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True
    
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        print(f"La marca es: {self.marca} \n Modelo: {self.modelo} \n En mercha: {self.enmarcha} \n Acelerando: {self.acelera} \n Frenado: {self.frena}")


coche1=Vehiculos("Mazda", "Mx5")
coche2=Vehiculos("Toyota", "Yatis")
coche3=Vehiculos("Nissan", "GOL")

coches = [coche1, coche2, coche3]
fichero = open("29-serializacion-LosCoches", "wb")

pickle.dump(coches,fichero)

fichero.close()

del (fichero)

# Lectura del fichero

ficheroApertura = open("29-serializacion-LosCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())