palabra = "python"
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)
# Otra forma mas sencilla, seria...
palabra = "python"
lista = [letra for letra in palabra]
print(lista)

#lo mismo en una sola linea
lista = [letra for letra in "python"]
print(lista)

#COn numeros
lista = [n for n in range(0,21,2)]
print(lista)

#Por ejemplo si busamos dividir nueros
lista = [n/2 for n in range(0,21,2)]
print(lista)
#SI queremos añadir condiciones
lista = [n if n*2 > 10 else "no" for n in range(0,21,2)]
print(lista)

#Para convertir pies en metros
pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)










