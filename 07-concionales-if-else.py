#Para un else, debe haber un if

print("Vender bebida alcoholica")

edad_cliente = int(input("Introduce tu edad: "))

if edad_cliente<18:
    print("No puedes tomar")
elif edad_cliente > 120:
    print("No es una edad real")
else: print("Puedes tomar")

print("El programa ha finalizado")