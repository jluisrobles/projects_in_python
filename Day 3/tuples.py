my_tuple = (1,2 ,"hola", 220.2)
print(type(my_tuple))
#Para saber la posicion de los elementos de tuple
print(my_tuple[1])

#Se pueden tener tuples dentro de los mismos tuples
tup = (45,78,(78,"dia"),8)
print(tup[2][1])

#asignar variables a valores
t=(1,2,3)
x,y,z=t
print(x,y,z)

#contar numero de veces que aparece un elemento
tap=(1,2,3,1,1,3)
print(tap.count(1))

#para saber la posicion
tap=(1,2,3,1,1,3)
print(tap.index(3))