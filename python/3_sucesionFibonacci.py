def fibonnaci(n):
    sucesion = [0, 1]
    for cont in range(2, n):
        sucesion.append(sucesion[cont - 1] + sucesion[cont - 2])

    print(sucesion)

fibonnaci(4)