import pickle

class Persona:
    
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre", self.nombre)

    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas = []

    def __init__(self):

        listaDePersonas = open("30-Ficheroexterno", "ab+")
        # Posicionar el curso en la posicion 0
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersoasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print (p)
    
    def guardarPersoasEnFicheroExterno(self):
        listaDePersonas = open("30-Ficheroexterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es:")
        for p in self.personas:
            print (p)


miLista = ListaPersonas()

p= Persona("Maria", "Femenino", 18)
miLista.agregarPersonas(p)
miLista.mostrarInfoFicheroExterno()
# p= Persona("Ana", "Femenino", 20)
# miLista.agregarPersonas(p)
# p= Persona("Maria", "Femenino", 18)
# miLista.agregarPersonas(p)

# miLista.mostrarPersonas()