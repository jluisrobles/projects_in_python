my_set = set([1,2,3,4,5])
print(type(my_set))
print(my_set)

#otra forma de escribir set´s
otro_set = {1,2,3,3,4,5}
print(type(otro_set))
print(otro_set)

#Se puede tuples ya que son inmutables como los sets
set = {1,2,(3,3),4,5}
print(set)

#Se pueden contar los elelmentos
set1 = {1,2,3,4,5}
print(len(set1))

#Para saber si esta un elemento dentro del set
set2 = {1,2,8,3,4,5}
print(8 in set2)

#Unir sets
s1 = {1,2,8,3,4,5}
s2 = {5,2,12,3}
s3 = s1.union(s2)
print(s3)

#agregar elemntos
ss = {1,2,8}
ss.add(9)
print(ss)

#Para quitar
ss = {1,2,8}
ss.remove(2)
print(ss)

#POR EJEMPLO PARA HACER UN SORTEO (el metodo POP elimina de forma aleatoria)
s3 = {3,2,8,3,4,5}
sorteo = s3.pop()
print(sorteo)

#Limpiat el st

s4 = {1,2,8,3,4,5}
s4.clear()
print(s4)