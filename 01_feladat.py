"""2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!"""

def masodik(szam):
    if szam < 0:
        print('A szám negativ.')
    elif szam > 0:
        print('A szám pozitív.')
    else:
        print('A szám nulla.')


"""Addig lehessen számokat megadni, amíg a felhasználó nem ad meg üres sztringet!"""

szam = 0

while szam != '':
    szam = input('Adj meg egy számot: ')
    if szam != '':
        szam = int(szam)
    


masodik(szam)