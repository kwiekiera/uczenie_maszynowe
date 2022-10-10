#a
def wypisz(imiona): 
    for i in imiona:
            print(i)
            
listaImion = ['Andrzej', 'Maciej', 'Sandra', 'Sebastian', 'Julia']
wypisz(listaImion)
        
#b
    #I
def oblicz1(liczby):
    for i in range(len(liczby)):
        liczby[i] = liczby[i]*2
    return liczby 

listaLiczb = [1, 3, -5, 10, -19]
print(oblicz1(listaLiczb))

    #II
def oblicz2(liczby):
        liczby = [liczba*2 for liczba in liczby]
        return liczby
    
print(oblicz2(listaLiczb))

#c

def zwrocParzyste(liczby):
    for i in range(len(liczby)):
        if liczby[i] % 2 == 0:
            print(liczby[i])

lista10Liczb = [1, -22, 5, -7, 0, 2, -1, 8, -9, 14]
zwrocParzyste(lista10Liczb)

#d
def zwrocCo2(liczby):
    for i in range(0, len(liczby), 2):
            print(liczby[i])

zwrocCo2(lista10Liczb)