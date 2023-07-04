def jugar_ahorcado():
    palabra_secreta = "python"
    intentos = 6
    letras_adivinadas = []

    while intentos > 0:
        letra = input("Ingresa una letra: ")

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta nuevamente.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Adivinaste una letra!")
        else:
            intentos -= 1
            print("La letra no está en la palabra. Te quedan", intentos, "intentos.")

        palabra_actual = ""
        for letra_secreta in palabra_secreta:
            if letra_secreta in letras_adivinadas:
                palabra_actual += letra_secreta
            else:
                palabra_actual += "_ "

        print("Palabra actual:", palabra_actual)

        if palabra_actual == palabra_secreta:
            print("¡Felicidades! ¡Adivinaste la palabra!")
            break

    if intentos == 0:
        print("¡Oh no! Te quedaste sin intentos. La palabra era", palabra_secreta)


jugar_ahorcado()