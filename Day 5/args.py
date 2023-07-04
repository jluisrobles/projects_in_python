#suma con args (solo admite 2 valores)
def suma(a,b):
    return a+b
print(suma(8,6))


print("*-*-*-*-*-*-*-*-*-*-*-*-")
#Numero indefinido de parámetros
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma(8,6,8,5,89,14,0.2,58.32,0.3))
               #El mismo ejemplo de manera mas facil
def suma(*args):
    return sum(args)
print(suma(8,6,8,5,89,14,0.2,58.32,0.3))
