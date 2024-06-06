def anagrama(string1, string2):
    #OBTENER LISTA DE PALABRAS
    palabraAnagrama1 = []
    palabraAnagrama2= []

    for letra in string1:
        palabraAnagrama1 += [letra]
    
    for letra in string2:
        palabraAnagrama2 += [letra]

    #COMPARAR SI ES UN ANAGRAMA

    if sorted(palabraAnagrama1) == sorted(palabraAnagrama2):
        print("Es un anagrama")
    else:
        print("No es un anagrama")
    print(sorted(palabraAnagrama1))
    print(sorted(palabraAnagrama2))

anagrama("hola", "hoal")
