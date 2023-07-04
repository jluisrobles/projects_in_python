# En este caso las dos operaciones tienen que sor o falsas o verdades
mi_bool = 55 == 55 and ("perro" == "PeRRo".lower())
print(mi_bool)

# Cuando usamos "or" si una es fasa, sale como resultado False
mi_bool2 = 55 == 55 and ("perro" == "gato")
print(mi_bool2)

#buscar palabra (si una no es verdadera, sale False)
frase = "Mi mensaje es este y es corto"
mi_bool = "Pedro" in frase and "este" in frase
print(mi_bool)

# En el caso de "or", basta que una sea verdadera para ser TRue
frase = "Mi mensaje es este y es corto"
mi_bool3 = "Pedro" in frase or "este" in frase
print(mi_bool3)

#Comparacion con negación "NOT"

booleano = not 5 == 5
print(booleano)