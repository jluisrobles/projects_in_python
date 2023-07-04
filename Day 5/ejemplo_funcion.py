precios_cafe = [("cortado",1.50), ("machiato",1.75), ("moka",1.90)]
for elemento in precios_cafe:
    print(elemento)

#El mismo ejemplo, pero solo mirando los tipos de café.
precios_cafe = [("cortado",1.50), ("machiato",1.75), ("moka",1.90)]
for cafe, precio in precios_cafe:
    print(cafe)

#Encontrar el cafe mas caro
precios_cafe = [("cortado",1.50), ("machiato",2.75), ("moka",1.90)]
def cafe_mas_caro (lista_precios):

    precio_mayor = 0
    cafe_mas_caro = " "
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)
cafe, precio = cafe_mas_caro(precios_cafe)

print(f"EL cafe mas caro es {cafe} con un precio de {precio}")
