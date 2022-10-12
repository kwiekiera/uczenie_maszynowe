#1
def powitaj(name: str, surname: str) -> str:
    return ("Cześć " + name + " " + surname + "!")

print(powitaj("Kamila", "Wiekiera"))
    
#2
def pomnoz(mnoznik: int, mnozna: int) -> int:
    return mnoznik*mnozna

print(pomnoz(2, 3))

#3
def sprawdzCzyParzysta(liczba: int) -> bool:
    return(liczba % 2 == 0)

czyParzysta = sprawdzCzyParzysta(3)
if czyParzysta:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
    
#4
def czySuma(l1: int, l2: int, l3: int) -> bool:
    return(l1+l2 >= l3)

print(czySuma(1, 2, 5))

#5
def czyZawiera(lista: list, liczba: int) -> bool:
    return (liczba in lista)

print(czyZawiera([1, 2, 3], 2))

#6
def polaczListy(l1: list, l2: list) -> list:
    l3 = list(set(l1 + l2))
    for i in range(len(l3)):
        l3[i] = l3[i]**3
    return l3

print(polaczListy([1, 2, 3], [3, 4, 5]))


