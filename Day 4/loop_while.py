monedas = 5
while monedas > 0:
    print(f"Tienes {monedas} coins")
    monedas = monedas -1
#una forma mas sencilla seria....:
print("*-*-*-*-*-*-*-*-*-*-*-*")
monedas1 = 4
while monedas1 > 0:
    print(f"Tienes {monedas1} coins")
    monedas1 -= 1
else:
    print("No tienes mas monedas")

# Preguntando al usuario
respuesta = "si"

while respuesta == "si":
    respuesta = input("Te gsuataria continuar? (si/no): ")
else:
    print("Gracias por visitarnos!")

#BREAK para interrumpir
nombre = input("Ingfesa tu nombre: ")
for letra in nombre:
    if letra == "l":
        break
    print (letra)

# CONTINUE para seguir con e mismo programa
nombre = input("Ingfesa tu nombre: ")
for letra in nombre:
    if letra == "e":
        continue
    print (letra)