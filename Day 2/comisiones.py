nombre = input("Cuál es tu nombre?:")
ventas = int(input("Cuánto es el total de tus ventas?:"))

comision = round(ventas * 13 /100,2)

print(f"Buenos días {nombre} este mes tuviste {ventas} de ganancias en ventas, por lo cual tu comisio será{comision}")