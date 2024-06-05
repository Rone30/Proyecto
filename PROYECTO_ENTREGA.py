print("¡¡¡ADIVINA LA PALABRA!!!!!!!")

palabra_secreta = "automatico"

letras_adivinadas = []

intentos_max = 5
intentos = 0


while intentos < intentos_max:
    letra = input("Ingresa una letra: ").lower()

    if letra in letras_adivinadas:
        print("Ya adivinaste esta letra antes.")
        continue

    letras_adivinadas.append(letra)

    if letra not in palabra_secreta:
        intentos += 1
        print(f"Letra incorrecta. Te quedan {intentos_max - intentos} intentos.")
    else:
        print("¡Adivinaste una letra!")

    palabra_mostrada = ""
    for letra_secreta in palabra_secreta:
        if letra_secreta in letras_adivinadas:
            palabra_mostrada += letra_secreta
        else:
            palabra_mostrada += "_"
    print(palabra_mostrada)

    if palabra_mostrada == palabra_secreta:
        print("¡Ganaste! Has adivinado la palabra.")
        break

if intentos == intentos_max:
    print(f"Perdiste! La palabra secreta era: {palabra_secreta} \n Suerte la próxima!")
