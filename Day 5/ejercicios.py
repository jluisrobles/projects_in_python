#Lanzar dados
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
resultado_dados = lanzar_dados()
dado1, dado2 = resultado_dados
mensaje = evaluar_jugada(dado1, dado2)
print(mensaje)

#Elimina números duplicados
def reducir_lista(lista):
    lista_sin_duplicados = list(set(lista))
    lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return lista_sin_duplicados

def promedio(lista):
    suma = sum(lista)
    cantidad_elementos = len(lista)
    promedio = suma / cantidad_elementos
    return promedio
lista_numeros = [1, 2, 15, 7, 2]

lista_reducida = reducir_lista(lista_numeros)
print(lista_reducida)  # Imprime [1, 2, 7]

promedio_resultado = promedio(lista_reducida)
print(promedio_resultado)  # Imprime el promedio de los valores de lista_reducida

#Aquí tienes la definición de las funciones "lanzar_moneda" y "probar_suerte" que cumplen con los requisitos solicitados:
import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif resultado_moneda == "Cruz":
        print("La lista fue salvada")
        return lista_numeros
lista_numeros = [1, 2, 3, 4, 5]

resultado_moneda = lanzar_moneda()
lista_resultado = probar_suerte(resultado_moneda, lista_numeros)

print(lista_resultado)  # Imprime la lista resultante según el resultado de la moneda