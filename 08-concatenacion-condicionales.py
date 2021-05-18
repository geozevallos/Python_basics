#Evaluando una edad

'''
edad = -1

if 0 < edad < 100:
    print("edad es correcta")
else:
    print("edad incorrecta")
'''

salario_presidente = int(input("Introduce salario presidente: "))
print("salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario director: "))
print("salario director: " + str(salario_director))

salario_jefe = int(input("Introduce salario jefe: "))
print("salario jefe: " + str(salario_jefe))

salario_administrador = int(input("Introduce salario administrador: "))
print("salario administrador: " + str(salario_administrador))

if salario_administrador < salario_jefe < salario_director < salario_presidente:
    print("Es lo normal")
else:
    print("Esto no es normal")