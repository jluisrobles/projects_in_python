texto = "Este es un texto de prueba"
#Mayusculas
resultado = texto.upper()
print (resultado)

# Minúsculas
resultado1 = texto.lower()
print (resultado1)

#Transforma a listas
resultado2 = texto.split()
print (resultado2)

#transforma a listas, tomando en cuenta un elemento que le digamos
resultado3 = texto.split("t")
print (resultado3)

#Separar por espacios
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

# Para buscar una letra o lo que quieras, si no existe lo que qeremos buscar por defecto saldrá -1
texto = "Este es un texto de prueba"
resultado4 = texto.find("o")
print (resultado4)

#Para reemplazar
texto = "Este es un texto de prueba"
resultado5 = texto.replace("texto", "fragmento")
print (resultado5)