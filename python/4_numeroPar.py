def numeroPar(n):
    for number in range(0, n +1):
        if number % 2 == 0:
            print(number, "Es par")
        else:
            print(number, "No es par")

numeroPar(100)