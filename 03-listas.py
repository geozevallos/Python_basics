#Es similar a los arrays por ejm de JS.
miLista = ["manzana", "pera", "fresa", "sandia"]

# Mostrar toda la lista
print(miLista[:])

print(miLista[3])

print(miLista[-2])

#Quiero los 2 primeros 
print(miLista[:2])


print(miLista[1:2])


print(miLista[1:])

#Agregar elemento al final
miLista.append("granadilla")

print(miLista[:])

##Agregar a uno en especifico
miLista.insert(2, "mandarina")
print(miLista[:])

#Agregar varios elementos
miLista.extend(["platano", "mango", "melon"])
print(miLista[:])

#El indice, si hubieran 2 fresas, impriima el 1er indice
print(miLista.index("fresa"))

#Si está o no
print("mango" in miLista)

#eliminar un elemento
miLista.remove("sandia")
print(miLista[:])

#elimiar el ultimmo elemento
miLista.pop()
print(miLista[:])


#Suma de lista
lista1 = [1, 2, 3, 4]
lista2 = [5,6]
lista3 = lista1 + lista2

print(lista3[:])

#Repetir 3 veces la lista
print(miLista * 3)