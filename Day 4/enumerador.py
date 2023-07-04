lista = ["a", "b", "c"]
indice = 0

for letra in lista:
    print(indice, letra)
    indice+= 1

#Usando enumerate
lista = ["a", "b", "c"]

for letra in enumerate(lista):
    print (letra)

# Si queremos verlo sin paréntesis
list1 = ["a", "b", "c"]

for indice, letra in enumerate(list1):
    print (indice, letra)

# Otro ejemplo sin necesidad de  crear listas

for indice, numero in enumerate(range(22,26)):
    print(indice, numero)
#MAs ejemplos

lis = ["a", "b", "c"]
mis_tuples = list(enumerate(lis))
print(mis_tuples)

#si queremos sacar elelmentos del ptuple
lis2 = ["a", "b", "c"]
mis_tuples = list(enumerate(lis2))
print(mis_tuples[2][1])