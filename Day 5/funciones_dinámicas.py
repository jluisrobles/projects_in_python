#Verififcar si un nñumero es de tres cifras
def verificar_3_cifras (numero):
    return numero in range (100,1000)
resultado = verificar_3_cifras(1784)
print(resultado)

# Que devuelva una lista de los numeros con tres cifras
def verificar_3_cifras (lista):
    lista_de3_cifras = []
    for n in lista:
        if n in range (100,1000):
            lista_de3_cifras.append(n)
        else:
            pass
    return lista_de3_cifras
resultado = verificar_3_cifras([178,54,122,548])
print(resultado)

#funsiones dinámicas
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero <= 0:
            return False
    return True
lista_numeros = [1, 2, -3, 4, 5]
resultado = todos_positivos(lista_numeros)
print(resultado)  # Imprime False

#Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if 0 < numero < 1000:
            suma += numero
    return suma
lista_numeros = [50, 200, 300, 1001, 150]
resultado = suma_menores(lista_numeros)
print(resultado)  # Imprime 550 (50 + 200 + 300)

#COntador de pares
def cantidad_pares(lista_numeros):
    contador_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador_pares += 1
    return contador_pares
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = cantidad_pares(lista_numeros)
print(resultado)  # Imprime 5 (2, 4, 6, 8, 10 son pares)
