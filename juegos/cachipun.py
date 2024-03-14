def cachipun():
    import random
    # piedra=1;papel=2;tijera=3
    ganador="no"
    while ganador=="no":
        computadora=random.randint(1, 3)
        jugador=str(input("Piedra, papel o Tijera: "))
        if jugador=="Papel" and computadora==1:
            print("GANA JUGADOR")
            ganador="si"
            break
        elif jugador=="Papel" and computadora==3:
            print("GANA COMPUTADORA")
            ganador="si"
            break
        elif jugador=="Piedra" and computadora==2:
            print("GANA COMPUTADORA")
            ganador="si"
            break
        elif jugador=="Piedra" and computadora==3:
            print("GANA JUGADOR")
            ganador="si"
            break
        elif jugador=="Tijera" and computadora==1:
            print("GANA COMPUTADORA")
            ganador="si"
            break
        elif jugador=="Tijera" and computadora==2:
            print("GANA JUGADOR")
            ganador="si"
            break

cachipun()
