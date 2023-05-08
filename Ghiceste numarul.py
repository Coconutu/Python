import random
continua="da"
while continua=="da":
    print()
    ghicit=False;
    calc=random.randint(0,100)
    while ghicit==False:
        user=int(input("Ghiceste numarul de la 1 la 100 : "))
        if user==calc:
            print("Felicitari, ai ghicit. Numarul era",calc)
            ghicit=True;
        elif user<calc:
            print("Ma gandeam la un numar mai mare")
        elif user>calc:
            print("Ma gandeam la un numar mai mic")
    continua=input("Doriti sa continuati? (da/nu)")
if continua=="nu":
    input("La revedere!")
    
       
