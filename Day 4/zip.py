nombre = ["Maria", "Pedrita", "Palmira"]
edades = [25, 35, 45]
ciudades = ["La Paz", "Lima", "london"]

combinados = list (zip(nombre, edades, ciudades))
print(combinados)

print("-*-*-*-*-*-*-*-*-*-*-")
# SI queremos explcar cada dato
for nombre, edades, ciudades in combinados:
    print(f"La persona {nombre}, tiene {edades} y es de la ciudad de {ciudades}")