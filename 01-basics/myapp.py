
def otazka1(odp):
    vysledek = 7
    bod = 1
    if odp == vysledek:
       print("Spravne!")
       return bod
    elif odp == vysledek + 1 or odp == vysledek - 1:
        print("Skoro...")
        print("Spravna odpoved: ", vysledek)
        return 0
    else:
        print("Spatne")
        print("Spravna odpoved: ", vysledek)
        return 0


def otazka2(odp):
    vysledek = 64
    bod = 1
    if odp == vysledek:
        print("Spravne!")
        return bod
    else:
        print("Mozna priste...")
        print("Spravna odpoved: ", vysledek)
        return 0


def otazka3(odp):
    vysledek = 0
    bod = 3
    if odp == vysledek:
        print("Spravne!!!")
        return bod
    else:
        print("Bouzel spatne :(")
        print("Spravna odpoved: ", vysledek)
        return 0


def pocet_bodu(body):
    if int(body) == 5:
        print("Plny pocet bodu. Musis byt genius!!!")
    elif int(body) < 5 and int(body) > 0:
        print("Plny pocet to neni, ale lepsi nez nic!")
    else:
        print("Zadny bod? Mozna priste...")


body = 0
print("Vitej v matematickem kvizu!")
odpv1 = input("1. Kolik je 2+5? ")
body += otazka1(int(odpv1))
# print (body)
odpv2 = input("2. Kolik je 8 na 2? ")
body += otazka2(int(odpv2))
# print(body)
odpv3 = input("3. Kolik je cosinus 90°?")
body += otazka3(int(odpv3))
print(body)
pocet_bodu(body)
