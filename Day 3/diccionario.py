diccionario = {'nombre':"Pedro",'apellido':"Rios", 'peso':98 }
print(type(diccionario))

# Para buscar dentro del diccionario
buscar = diccionario ["peso"]
print(buscar)

#Diccionario dentro de diccionario

dic ={'valo1':2344, 'valo2': "Dias y noches", 'valo3':{'a':1,'b':2, 'c':3}}
print(dic['valo2'])
print(dic["valo3"]['c'])

#Buscar la letra "e" pero que salga en mayúscula
dicci = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dicci["c2"][1].upper())

#Modificar dicionario
dicc = {'a':1, 'b':2, 'c':"tu mismo"}
print(dicc)
dicc ["d"]= "nueva variable"
print(dicc)
#para conocer solo llaves y valosres por separado
print (dicc.keys())
print(dicc.values())
#para conocer todo lo que hay en el diccionario
print(dicc.items())