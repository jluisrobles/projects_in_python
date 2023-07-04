serie = "N-02"

if serie == "N-01 ":
    print("Samnsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

print("*-*-*-*-*-*-*-*-*-*-*-*-*-**-*")
serie = "N-01"
match serie:

    case "N-01":
        print("Samnsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

# Un caso algo mas complejo

cliente = {"nombre": "Jose", "edad":41, "ocupacion": "profesor"}
pelicula = {"titulo": "matrix",
            "ficha_tecnica":{"protagonista": "Keanu Reeves", "director": "lana y lilly Wachowski"}}
elemento = [ cliente, pelicula, "libro"]
for e in elemento:
    match e:
        case {"nombre": nombre, "edad": edad, "ocupacion": ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo, "ficha_tecnica": {"protagonista": protagonista, "director": director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No sabemos que es esto!!")
