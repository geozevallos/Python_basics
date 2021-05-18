#### Condiciones para bono ----
#Vivir a 40km de la capita
#tener más de 2 hijos
#Salario menor a 1500 soles

'''
print("Bono covid")
distancia_capital = int(input("Introduce la distancia en km: "))
print(f"La distancia a la capita es: {distancia_capital}")
n_hijos = int(input("Introduce el numero de hijos: "))
print(f"El numero de hijos es: {n_hijos}")
salario = int(input("Introduce el salario: "))
print(f"el salario es: {salario}")

if distancia_capital > 40 and n_hijos > 2 or salario < 1500:
    print("tienes bono covid")
else:
    print("No tienes bono covid :(")
'''

# --- Operador IN
print("Asignaturas optativas Geografía")
print("Asignaturas optativas: Ecoturismo, Geopolítica, Realidad Nacional")

opcion = input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in ("ecoturismo", "geopolitica", "realidad nacional"):
    print("Asignatura elegica " + asignatura)
else:
    print("La asignatura escogida no está disponible")