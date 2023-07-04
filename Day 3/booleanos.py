var1 = True
var2 = False
print(type(var1))
print(var1)

#compración
numero = 5 <= 3+1
print(type(numero))
print(numero)
# Ó tambien de esta forma
numero = bool(5 != 3+1)
print(type(numero))
print(numero)

#para buscar un valor en una lista
lista = [1,2,3,4,5]
control_lista = 9 in lista
print(type(lista))
print(control_lista)
