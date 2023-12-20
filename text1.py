diviseur = 2 
premier = True

val= int(input("entrez un nr entier > 1 :  "))

while premier and diviseur*diviseur <= val :
    if val % diviseur == 0 :
        premier = False
    diviseur+= 1

if premier :
 print(val, "est premier")
else :
 print(val, "n'est pas premier")