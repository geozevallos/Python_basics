#Bucle determinado
#Se ejecuta un # determinado de veces

#Indeterminados
#No se sabe cuantas veces

##Declaracion del bucle:
#####Cuerpo del bucle


## ---- FOR

#El bucle determinado en Python puede ser el: for

# for varaible in elementoArecorrer(Esto puede ser una lista, tupla o texto)
#######cuerpo de bucle
#######cuerpo de bucle
#######cuerpo de bucle

'''
for i in [1, 2, 3, 4]:
    print(i)


for dato in ["jorge", "ernesto", "zevallos"]:
    print(dato, end=" ")


#Tambien se puede recorrer un string

for i in "Otorrinolaringologia":
     print(i)

#Validar un correo:
email = False
for letras in "jzevallos@gmail.com":
    if (letras == "@"):
        email = True

if email:
    print("Email correcto")
else: print("NO es correcto :c")


#Otra manera de validad
contador = 0
for letras in "jzevallos@gmail.com":
    if (letras == "@" or letras == "."):
        contador = contador + 1

if contador == 2:
    print("Email correcto")
else: print("NO es correcto :c")
'''


# Range ------------------------------
for i in range(1,10):
    print("GAAAA!")

