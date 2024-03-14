def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """

    import random
    c=0
    x= random.randint(1,10)
    while c==0:
        y= int(input("Adivina el número: "))
        if y==x:
            c=1
        else:
            print("Intenta de nuevo")
    print("Adivinaste")

    pass

adivinar_numero()
