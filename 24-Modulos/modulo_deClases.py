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
        
        
        
class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"


    def estado(self):
              print(f"La marca es: {self.marca} \n Modelo: {self.modelo} \n En mercha: {self.enmarcha} \n Acelerando: {self.acelera} \n Frenado: {self.frena} \n {self.hcaballito}")
       


#Clase de vehiculos electricos
class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando=True



