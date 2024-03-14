def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    import random 
    enter =input("Debes apretar enter para jugar:")
    if enter == "":
        puntaje_usuario=0
        puntaje_computador=0
        ronda=1
        while puntaje_usuario <30 and puntaje_computador<30:
            
            numero=random.randint(1,6)
            
            puntaje_usuario+=numero

            numero2=random.randint(1,6)
            puntaje_computador+=numero2

            print("Ronda",ronda,"Usuario:", puntaje_usuario)
            print("Ronda", ronda, "Computador:", puntaje_computador)

            ronda+=1
            
        if puntaje_usuario>=30:
            print("El usuario gana el juego")
        else:
            print("Gano el computador")
    else:
        print("No apretaste enter")

juego_del_dado()
