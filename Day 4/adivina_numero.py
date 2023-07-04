from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("¿Cuál es tu nombre? ")

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, \ny tienes solo ocho intentos para adivinar cuál crees que es el número")

while intentos < 8:
    estimado = int(input("Dime cual es tu numero: "))
    intentos += 1
    if estimado not in range(1,101):
        print("Tiene que ser un numero del 1 al 100")
    elif estimado < numero_secreto:
        print("Tu numero es mas bajo")
    elif estimado > numero_secreto:
        print("Tu numero es mas alto")
    else :
        print(f"{nombre} ADIVINASTE EL NUMERO!!!!! \nHas adivinado en {intentos} intentos!!!")
        break
if estimado != numero_secreto:
    print(f"Lo siento {nombre}se han terminado los 8 intentos, el número secreto era {numero_secreto}.")




