#17. Pide una cadena e indica si es un palíndromo o no.

cadena=input("Escribe la cadena")

cadena_al_reves = cadena[::-1]

if(cadena==cadena_al_reves):
    print("si es palindromo")
else:
    print("no es palindromo")