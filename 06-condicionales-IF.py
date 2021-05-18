print("Evaluación de notas")

nota_alumno = input("Introduce la nota:")

def evaluacion(nota):
    valoracion="aprobado"
    if nota < 11:
        valoracion = "suspenso"
    return valoracion


print(evaluacion(int(nota_alumno)))