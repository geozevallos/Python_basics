#Creación y apartura

archivo_texto = open("archivo.txt", "w")

frase = "Creando un archivo \n mediante Python"

#Manipulacion y escritura
archivo_texto.write(frase)

#Fase de cierre: Es decir cerrarlo en memoria
archivo_texto.close()