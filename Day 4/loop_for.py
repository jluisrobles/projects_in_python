lista = ["a", "b", "c"]
for letra in lista:
    print("Es la letra: " + letra)

#Para saber la psosición de la letra
lista = ["a", "b", "c"]
for letra in lista:
    posicion = lista.index(letra)
    print(f"La letra {posicion} es: {letra}")

# Para saber si un nombre empieza con una letra determinada
lista2 = ["luis", "pedr", "juan", "maria", "julia"]
for nombre in lista2:
    if nombre.startswith("j"):
        print(nombre)
# Suma de numros con for
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

#Mostarr letras
palabra = "Python"
for letra in palabra:
    print (letra)

# Con varias listas
grupos = [[1,2],[3,4],[5,6]]
for numeros in grupos:
    print(numeros)
#Usando a,b, donde a por defecto son inpares y "b" sierían pares
grupos = [[1,2],[3,4],[5,6]]
for a,b in grupos:
    print(a)

