inf=int(input("Afisare numere prime intre :"))
sup=int(input("Pana la :"))
for numar in range(inf+1,sup+1):
    if numar>1:
        for i in range(2,numar):
            if (numar%i)==0:
                break
        else:
            print(numar)
