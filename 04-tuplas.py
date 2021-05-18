# •	Inmutables, no se puede modificar despues de su creacion
# •	Sí permite extraer porciones, el resultado es una nueva dupla
#Son más rapidas xq tienen menos espacio
# Se puede utilizar como claves en un diccionario

# miTupla = ("Jorge", 1, 4, 5)

#Acceder a un elemento
# print(miTupla[0])

#Una lista en base a la tupla
# milista = list(miTupla)
# print(milista)

#Proceso inverso
listaFruta = ["pera", "melon", "manzana", "pera"]
tuplaFrutas = tuple(listaFruta)
print(tuplaFrutas)

# ¿Está en la tupla?
print("pera" in listaFruta)

#¿Cuantos elementos "x" se encuentran en la tupla?
print(tuplaFrutas.count("pera"))

#¿Cuantos elementos hay en la tupla
print(len(tuplaFrutas))

#Tuplas unitarias
tuplaUnitaria = ("Jorge",)


#Crear una tupla sin parentesis / Conocido como empaquetado
tupla2 = "Jorge", "Yanet"
print(tupla2)

#Dessempaquetado
novio, novia = tupla2
print(novio)