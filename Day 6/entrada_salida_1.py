#Siempre se tiene que cerrar el archivo al final (mi_archivo.close()).
mi_archivo = open("prueba.txt")
print(mi_archivo.read())

mi_archivo.close()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#Para leer por lineas, se puede repetir el comando (readline) varias veces y lee las siguientes líneas
mi_archivo = open("prueba.txt")

una_linea = mi_archivo.readline()
print(una_linea.upper())           #mayusculas!!!!
una_linea = mi_archivo.readline()
print(una_linea.rstrip())          #quitar salto de linea!!!
una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#Por cada linea poner un mensaje
mi_archivo = open("prueba.txt")
for l in mi_archivo:
    print("Aquí dice: " + l.rstrip())     #Quitando saltos de linea!!!!!

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
#Para escribir dentro del archivo o crea un nuevo archivo, las triple comillas es para escribir varias líneas.
archivo = open("prueba1.txt", "w")
archivo.write('''Hola
                mundo
                como 
                estan?''')
archivo.close()

print("*-*-*-**-**-**-*-*-*-*-**-")
#Para añadir texto al archivo SIN BORRAR LO QUE YA TENEMOS!!! Usar la "a" y no la "w"
archivo = open("prueba1.txt", "a")
archivo.write("ESTAREMOS POR SIEMPRE!!!")
archivo.close()
