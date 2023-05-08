from Calculator import rezolva_ec2
calculeaza=True
while calculeaza==True:
    print("Rezolvarea ecuatiei de gradul al doilea de forma ax+b=c ")
    tasta=input('Pentru rezolvare apasa D, pentru iesire apara X ')
    if tasta=='D':
        a = int(input('Introduceti a : '))
        b = int(input('Introduceti b : '))
        c = int(input('Introduceti c : '))
        rezolva_ec2(a,b,c)
    elif tasta=='X':
        print('Va multumim !')
        calculeaza=False
    else:
        print('Selectati o optiune valida.')
