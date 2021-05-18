archivo_texto = open("archivo.txt", "r")

#Donde qiero q empiece posiconado el puntero

#archivo_texto.seek(11)
#print(archivo_texto.read())


# ----------
##También puede especificar hasta donde leer
#print(archivo_texto.read(11))


#Este continuaria desde donde dejo el puntero
#print("----")
#print(archivo_texto.read())

#----Poner el puntero en la mitad y leer
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())