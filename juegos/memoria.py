def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    print("Te voy a mostrar una secuencia de 5 números, tienes que repetirla")
    n1 = random.randint(0,10)
    n2 = random.randint(0,10)
    n3 = random.randint(0,10)
    n4 = random.randint(0,10)
    n5 = random.randint(0,10)
    secuencia= [n1, n2, n3, n4, n5]
    print(n1, "-", n2,"-", n3, "-", n4, "-", n5)

    print("Ahora repitelo")
    u1 = int(input("N1: "))
    u2 = int(input("N2: "))
    u3 = int(input("N3: "))
    u4 = int(input("N4: "))
    u5 = int(input("N5: "))
    respuesta = [u1, u2, u3, u4, u5]

    print("La secuencia es:", secuencia)
    print("Tu dijiste:", respuesta)

    if secuencia == respuesta:
        return "Acertaste"
    else:
        return "No acertaste"

print(memoria())
