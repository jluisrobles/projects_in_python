#suma de numeros al cuadrado
def suma_cuadrados(*args):
    suma = 0
    for num in args:
        suma += num ** 2
    return suma
resultado = suma_cuadrados(1, 2, 3)
print(resultado)  # Imprime 14

#Aquí tienes la definición de la función "suma_absolutos" que cumple con los requisitos solicitados:
def suma_absolutos(*args):
    suma = 0
    for num in args:
        suma += abs(num)
    return suma
resultado = suma_absolutos(-1, 2, -3, 4)
print(resultado)  # Imprime 10

#Aquí tienes la definición de la función "numeros_persona" que cumple con los requisitos solicitados:
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje
mensaje = numeros_persona("Juan", 1, 2, 3)
print(mensaje)  # Imprime "Juan, la suma de tus números es 6"