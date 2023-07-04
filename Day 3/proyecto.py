#ANALIZADOR DE TEXTO
texto = input("Ingresa un poema corto: ")
letras = []
texto = texto.lower()
letras.append(input("Ahora, ingresa una letra a tu elección: "))
letras.append(input("Ahora, ingresa otra letra a tu elección: "))
letras.append(input("Ahora, ingresa una última letra a tu elección: "))

print("-------------------------------")
print("CATIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Hemos encontrado la letra'{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra'{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra'{letras[2]}' repetida {cantidad_letras3} veces")

print("-------------------------------")
print("CATIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos enconyrado {len(palabras)} palabras en el texto")

print("-------------------------------")
print("LETRA INICIO Y LETRA FINAL")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial del texto es'{letra_inicio}' y la letra final es '{letra_final}'")

print("-------------------------------")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"Tu texto al revés se leerá así: '{texto_invertido}'")

print("-------------------------------")
print("LA PALABRA PYTHON")
buscar_python = "python" in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto que nos diste")