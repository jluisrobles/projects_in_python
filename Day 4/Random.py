from random import *
aleatorio = randint(1,20)
print(aleatorio)

#COn decimales, en este caso el numero 1 indica con un decimal
aleatory = round(uniform(10,20), 1)
print(aleatory)

#Usando random, en este caso se movera entre 0 y 1, con muchos decimales
aleato = random()
print(aleato)

#COn string
colores = ["azul", "verde", "negro", "gris", "blanco"]
aleator = choice(colores)
print(aleator)

# Una forma de barajar
numeros = list(range(5,55,5))
shuffle(numeros)
print(numeros)