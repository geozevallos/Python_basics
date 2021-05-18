#Creación y apertura

archivo_texto = open("archivo.txt", "r")


#Manipulacion 
#contenido = archivo_texto.read()
#print(contenido)

#Crea una lista con las lineas
lineas_texto = archivo_texto.readlines()
#print(lineas_texto)
print(lineas_texto[1])


#Fase de cierre: Es decir cerrarlo en memoria
archivo_texto.close()


