texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
caracteres_a_remover = ",:_%#"
resultado = texto.lstrip(caracteres_a_remover)
print(resultado)

# otro ejemplo
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")

print(frutas)

def bienvenida(nombre):
    print("¡Bienvenido", nombre_persona + "!")

nombre_persona = "John"  # Puedes cambiar el nombre aquí

# Potencia de un numero
def potencia(base, exponente):
    resultado = base ** exponente
    return resultado
resultado_potencia = potencia(3, 4)
print(resultado_potencia)  # Imprime 81

#COnversor de divisas
def usd_a_eur(monto_dolares):
    monto_euros = monto_dolares * 0.90
    return monto_euros
dolares = 100  # Monto en dólares a convertir
euros = usd_a_eur(dolares)
print(euros)  # Imprime el monto equivalente en euro

#Invertir palabras
def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1]
    palabra_invertida_mayus = palabra_invertida.upper()
    return palabra_invertida_mayus
palabra = "Python"
palabra_invertida = invertir_palabra(palabra)
print(palabra_invertida)  # Imprime "NOHTYP"
