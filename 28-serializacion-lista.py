import pickle 


'''
#Creando el archivo binario
lista_frutas = ["manzana", "pera", "mandarina"]

fichero_binario = open("28-serializacion_lista", "wb")

pickle.dump(lista_frutas, fichero_binario)

fichero_binario.close()

del (fichero_binario)
'''

#Accediendo al archivo binarios
fichero = open("28-serializacion_lista", "rb")

lista = pickle.load(fichero)

print(lista)