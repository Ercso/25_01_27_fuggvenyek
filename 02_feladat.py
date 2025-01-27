"""4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!"""

szavak = []

hanyszor = 4

for i in range(hanyszor):
    szavak.append(input('Adjon meg egy szót: '))

def leg(szavak):
    legrov = szavak[0]
    for szo in szavak:
        if len(szo) < len(legrov):
            legrov = szo
    return legrov

print('A legrövidebb szó: ', leg(szavak))