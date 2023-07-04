#Mostrar resultadode buscqueda con parámetro
lista = ['a', 'b', 'c']
resultado = lista [:2]
print (resultado)

#Concatenación de listas
lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
print (lista+lista2)

#Cambiar datos dentro de la lista
lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
lista3= lista + lista2

lista3 [0] = "Pedro"
print(lista3)

#agregar a lista
lista3 = ['a', 'b', 'c']
lista4 = ['d', 'e', 'f']
todo = lista3 + lista4
todo.append("g")

print(todo)

# Metodo para eliminar elementos
todo.pop(1)
print(todo)

# Metodo para eliminar elementos y guardado en una variable
eliminado = todo.pop(1)
print(eliminado)
#Ordena listas
lista_desordenada  = ['a', 'd', 'b', 'e', 'c']
lista_desordenada.sort()
print(lista_desordenada)

#Ordena listas al revés
lista_o = ['a', 'd', 'b', 'e', 'c']
lista_o.reverse()
print(lista_o)