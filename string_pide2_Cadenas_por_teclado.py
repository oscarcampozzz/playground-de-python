#16. Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y con los 2 primeros caracteres intercambiados. Por ejemplo, hola mundo pasaria a mula hondo

cadena1=input("Dame la primera cadena: ")
cadena2=input("Dame la segunda cadena: ")

print(cadena2[:2]+cadena1[2:]+" "+cadena1[:2]+cadena2[2:])



