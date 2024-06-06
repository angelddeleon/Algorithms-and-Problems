
def fizzbuz(n):
    for x in range(1, n+1):
        if x % 5 == 0 and x % 3 == 0:
            print(x, "fizzbuzz")
        elif x % 3 == 0:
            print(x, "fizz")
        elif x % 5 == 0:
            print(x, "buzz")
        else:
            print(x)


fizzbuz(40)