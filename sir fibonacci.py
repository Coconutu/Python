print("Sirul lui Fibonacci")
ls=int(input("Cate numere din sir doriti sa afisez? "))
a=c=0
b=1
print(a)
print(b)
for i in range(ls-2):
    c=a+b
    print(c)
    a=b
    b=c
input("La revedere! :)")  
