import requests
oras=''
def afiseaza_vremea(oras):
    url='https://wttr.in/'+oras
    res=requests.get(url)
    print(res.text)

while oras!='EXIT':
    print('Introduceti orasul unde vreti sa aflati vremea. Pentru iesire, introduceti EXIT')
    oras=input('Introduceti orasul :')
    afiseaza_vremea(oras)