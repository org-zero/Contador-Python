# Pedir al usuario que introduzca el número inicial y final
inicio = int(input("Introduce el número inicial: "))
fin = int(input("Introduce el número final: "))

# Bucle for para contar desde el número inicial hasta el número final
for i in range(inicio, fin+1):
    print(i)

# Imprimir un mensaje al final del contador
print("Conteo finalizado.")
