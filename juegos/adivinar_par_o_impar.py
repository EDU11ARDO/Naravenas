def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    respuesta_usuario = input("Par o impar: ")
    n = random.randint(1,2)
    if n%2==0:
        print("Salió un par")
        if respuesta_usuario=="Par":
            return "Adivinaste"
        else:
            return "No adivinaste"
    else:
        print("Salió un impar")
        if respuesta_usuario=="Impar":
            return "Adivinaste"
        else:
            return "No adivinaste"

print(adivinar_par_o_impar())
