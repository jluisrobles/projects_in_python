minimo = min(23,56,78,898,6565,11,21,30)
print(minimo)
maximo = max(23,56,78,898,6565,11,21,30)
print(maximo)

# T%ambien se puede trabajar con listas de esta forma
lista = [23,56,78,898,6565,11,21,30]
print(f"El número mayor de etos números es {max(lista)} y el menor es {min(lista)}")

# Tambien con strings/ primero busca las mayusculas por oreden alfa.
nombre = "Carlos"
print(min(nombre))
#por eso mejor usar el ".lower"
nomb = "Carlos"
print(min(nombre.lower()))

#En diccionarios
dic = {"C1":54, "C2":13}
print(min(dic.values()))