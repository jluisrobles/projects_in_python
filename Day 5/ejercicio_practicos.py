"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3

    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        return sorted([num1, num2, num3])[1]
print(devolver_distintos(5, 7, 3))  # Devuelve: 3 (suma = 15)
print(devolver_distintos(2, 4, 6))  # Devuelve: 6 (suma = 12)
print(devolver_distintos(10, 1, 2))  # Devuelve: 10 (suma = 13)

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-**")
"""Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']"""
def letras_unicas_ordenadas(palabra):
    letras_unicas = sorted(set(palabra))
    return letras_unicas
resultado = letras_unicas_ordenadas("entretenido")
print(resultado)  # Devuelve: ['d', 'e', 'i', 'n', 'o', 'r', 't']

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-**")
"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""
def verificar_cero_repetido(*args):
    previo = None

    for num in args:
        if num == 0 and previo == 0:
            return True
        previo = num

    return False
print(verificar_cero_repetido(5, 6, 1, 0, 0, 9, 3, 5))  # Devuelve: True
print(verificar_cero_repetido(6, 0, 5, 1, 0, 3, 0, 1))  # Devuelve: False
print(verificar_cero_repetido(1, 2, 3, 4, 0, 0, 0, 0))  # Devuelve: True

print("*-*-*-*-***-*-*-*-*-*-*-*-*-")
"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos"""
def contar_primos(numero):
    contador = 0

    for num in range(2, numero + 1):
        if es_primo(num):
            contador += 1
            print(num)

    return contador
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
cantidad = contar_primos(20)
print("Cantidad de números primos:", cantidad)