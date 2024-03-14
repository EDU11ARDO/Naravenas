def juego_del_dado():
    import random 
    print("debes apretar enter para jugar")
    puntaje_usuario=0
    puntaje_computador=0
    while puntaje_usuario !=30 or puntaje_computador!=30:
        numero=random.randit(1,6)
        puntaje_usuario+=numero
        numero2=random.randit(1,6)
        puntaje_computador+=numero2
    if puntaje_usuario==30:
        print("El usuario gana el juego")
    else:
        print("Gano el computador")