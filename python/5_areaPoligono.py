def areaPoligono(figura, altura, base):
    if figura == "c":
        print("esta es el area del cuadrado: ", int(altura) ** 2)
    elif figura == "t":
        print("esta es el area del triangulo:", (int(base) * int(altura)) / 2)
    else:
        print("esta es el area del rectangulo:", int(base) * int(altura))

areaPoligono("c", 4, 0)