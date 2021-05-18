#Permite almacenar valores de diferentes tipos (incluye listas y diccionarios)
#Se almacenan en forma CLAVE:VALOR
#Los elementos no están ordenados, es indiferente

# miDiccionarios = {"Peru": "Lima", "Chile": "Santiago", "Ecuador": "Quito"}
# print(miDiccionarios["Peru"])

# #Agregar más elementos
# miDiccionarios["Argentina"]="Cordoba"
# print(miDiccionarios)

# #Modificar/Reasignar
# miDiccionarios["Argentina"] = "Buenos Aires"
# print(miDiccionarios)

#Eliminar un elemento
# del miDiccionarios["Chile"]
# print(miDiccionarios)

tupla1 = ("Jorge", "Pedro", "Luis")
diccionarioNotas = {tupla1[0]:19, tupla1[1]:20, tupla1[2]:10}
print(diccionarioNotas) 

diccionarioAL = {"nombre": "Alianza Lima", "Fundacion": 1991, "Campeonatos":(2003, 2004, 2006)}
print(diccionarioAL["Campeonatos"])

#Metodos de un diccionarios
print(diccionarioAL.keys())
print(diccionarioAL.values())
print(len(diccionarioAL))