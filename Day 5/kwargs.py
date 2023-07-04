def suma (**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
suma(x=1, y=6, z=7)

print("*-*-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*")
#Prueba de la mezcla de tipos de argumentos y elementos diferentes
def prueba (num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
prueba(45,74, 254, 4847, 787, 121, x=112, y=126, z=157)

print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
#Cantidad de atributos
def cantidad_atributos(**kwargs):
    return len(kwargs)
print(cantidad_atributos(nombre='Juan', edad=30))  # Imprime: 2
print(cantidad_atributos(color='rojo', precio=10, cantidad=5))  # Imprime: 3
print(cantidad_atributos(usuario='admin', contraseña='secreta', correo='ejemplo@example.com'))  # Imprime: 3

print("*-*-*-*-*-*-*-**-*-****-*-*-*")
#Aquí tienes una función llamada lista_atributos que devuelve en forma de lista los
#valores de los atributos entregados en forma de palabras clave (keywords):
def lista_atributos(**kwargs):
    return list(kwargs.values())
print(lista_atributos(nombre='Juan', edad=30))  # Imprime: ['Juan', 30]
print(lista_atributos(color='rojo', precio=10, cantidad=5))  # Imprime: ['rojo', 10, 5]
print(lista_atributos(usuario='admin', contraseña='secreta', correo='ejemplo@example.com'))  # Imprime: ['admin', 'secreta', 'ejemplo@example.com']

print("-*-**-*-*-*-*-**-*-*-*-*-*-*-*")
# Aquí tienes la función describir_persona que toma como parámetro el nombre de la persona y una cantidad indeterminada de argumentos
#clave-valor para mostrar en pantalla las características de esa persona:
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
describir_persona("María", color_ojos="azules", color_pelo="rubio", edad=25)