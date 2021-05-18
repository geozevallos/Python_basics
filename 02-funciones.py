#Funciones predefinidas (Vienen con el lenguaje)
# print("Estamos aprendiendo")
# print("Estamos aprendiendo funciones básicas")
# print("poco a poco avanzaremos")


#Propias: Crear tus propias funciones

#Declaracion de la funcion
# def mensaje():
#     print("Estamos aprendiendo")
#     print("Estamos aprendiendo funciones básicas")
#     print("poco a poco avanzaremos")


#LLamada a la función
# mensaje()

#Funcion con parametros ---------------------
# def suma(num1, num2):
#     print(num1 + num2)

# suma(5, 8)

##Con Return
def suma(num1, num2):
    resultado=num1+num2
    return resultado

print(suma(5,6))

almacenarResultado = suma(5,6)
print(almacenarResultado)