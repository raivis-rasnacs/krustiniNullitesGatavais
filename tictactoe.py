"""
Krustiņi un nullītes.
"""

import random  # piesaista random bibliotēku, kas vēlāk būs vajadzīga

laukums = [  # definē sarakstu spēles laukuma reprezentācijai
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


"""
TODO: Drukā grafisku spēles laukumu (kā paraugā) no figūrām, kas glabājas sarakstā.
Ja elements ir skaitlis, tad to izlaiž. Citādi izdrukā X vai 0.
Katru simbolu pozicionē kvadrātiekavās.

Paraugs:
[X][ ][0]
[ ][X][0]
[ ][ ][X]
"""
def ziimeeLaukumu():
    for rinda in laukums:  # caurskata rindas sarakstā (kopā 3)
        for elements in rinda:  # caurskata elementus rindā (katrā pa 3)
            if elements in ["X", "0"]:  # ja attiecīgajā pozīcijā glabājas X vai 0
                print(f"[{elements}]", end="")  # drukā simbolu, NEpārceļot jaunā rindā, jo end=""
            else:
                print(f"[ ]", end="")  # ja nav X vai 0, tad drukā tukšas kvadrātiekavas
        print("")


"""
TODO: Aicina spēlētāju izdarīt gājienu, ievadot skaitli intervālā 1 - 9.
TODO: Atkarībā no ievadītā skaitļa, ieraksta X vai 0 attiecīgajā pozīcijā sarakstā.
Izdrukā pašreizējo spēles laukumu un pārbauda, vai nav fiksēta uzvara/neizšķirts.
Ja spēle nav galā, tā turpinās ar nākamo gājienu.
"""
def gajiens(speletajs):
    global laukums  # pārdefinē globālu mainīgo funkcijā, lai to var pārrakstīt (mainīt)

    mans_gajiens = int(input("Tavs gājiens: "))  # prasa ievadīt skaitli
    for i in range(len(laukums)):  # caurskata saraksta indeksus 0 - 2
        for j in range(len(laukums[i])):  # caurskata attiecīgās rindas indeksus
            if laukums[i][j] == mans_gajiens:  # salīdzina, vai elements ar indeksiem [i][j] ir vienāds ar ievadīto skaitli
                laukums[i][j] = speletajs  # saglabā attiecīgajā pozīcijā X vai 0, atkarībā no gājienu izdarošā spēlētāja

    ziimeeLaukumu()  # izsauc funkciju, kas uzzīmē konsolē spēles laukumu

    iznakums = parbaudaUzvaru()  # izsauc funkciju, kas pārbauda, vai nav fiksēta uzvara
    if iznakums != False:  # ja neatgriež False
        spelesBeigas(iznakums)  # tad izsauc f-ju spelesBeigas, padodot parametru iznakums (True vai False vai "neizšķirts")
    else:
        if speletajs == "X":  # jā gājienu izdarīja X
            gajiens("0")  # pārslēdz uz 0
        else:  # ja gājienu izdarīja O
            gajiens("X")  # pārslēdz uz X


"""
Attīra laukumu no esošajām figūrām, sanumurē laukus.
Spēle turpinās ar pirmo gājienu.
"""
def jaunaSpele(speletajs):
    global laukums  # pārdefinē globālu mainīgo funkcijā, lai to var pārrakstīt (mainīt)
    skaititajs = 1  # skaitītājs lauciņu numurēšanai
    for i in range(len(laukums)):  # caurskata saraksta indeksus
        for j in range(len(laukums[i])):  # caurskata rindas indeksus
            laukums[i][j] = skaititajs  # iestata skaitli attiecīgajā [i][j] pozīcijā
            skaititajs += 1  # palielina skaitītāju

    gajiens(speletajs)  # pāriet uz jaunu gājienu


"""
TODO: Cikliski caurskata sarakstu un pārbauda, vai eksistē uzvaroša kombinācija vai neizšķirts.
TODO: Ja eksistē uzvaroša kombinācija, atgriež uzvarētāja simbolu (X vai 0).
TODO: Ja konstatēts neizšķirts, atgriež "neizšķirts".
TODO: Citādi atgriež False.
"""
def parbaudaUzvaru():
    #horizontāles
    for rinda in laukums:  # caurskata rindas sarakstā
        if rinda[0] == rinda[1] == rinda[2]:  # salīdzina, vai elementi rindā ir vienādi
            return True  # atgriež loģisko vērtību True (f-ja tālāk neizpildās)

    #vertikāles
    for i in range(len(laukums[0])):  # caurskata elementus 1. rindā
        if laukums[0][i] == laukums[1][i] == laukums[2][i]:  # salīdzina elementus katrā kolonnā
            return True  # atgriež loģisko vērtību True (f-ja tālāk neizpildās)

    #diagonāles
    if laukums[0][0] == laukums[1][1] == laukums[2][2]:  # salīdzina elementus pa diagonāli (\)
        return True  # atgriež True (f-ja tālāk neizpildās)
    elif laukums[0][2] == laukums[1][1] == laukums[2][0]:  # salīdzina elementus pa pretējo diagonāli (/)
        return True  # atgriež True (f-ja tālāk neizpildās)
    else:
        for rinda in laukums:  # caurskata rindas sarakstā
            for elements in rinda:  # caurskata elementus rindā
                if elements in range(1, 10):  # ja elements ir skaitlis no 1 līdz 9
                    return False  # atgriež loģisko vērtību False
        else:
            return "neizšķirts"  # atgriež tekstuālu vērtību "neizšķirts"


"""
Izvada jautājumu par jaunas spēles sākumu. 
Ja atbild apstiprinoši, izsauc f-ju jaunaSpele(), padodot kā parametru uzvarētāju, kurš sāks spēli.
"""
def spelesBeigas(uzvaretajs):
    izvele = input("Vai vēlies spēlēt vēlreiz? (y/n")  # prasa ievadīt y vai n
    if izvele == "y":  # ja ievadīts y
        if uzvaretajs == "X":  # ja uzvarējis X
            jaunaSpele("X")  # jaunu spēli sāk X
        elif uzvaretajs == "0":  # ja uzvarējis 0
            jaunaSpele("0")  # jaunu spēli sāk 0
        else:
            jaunaSpele(random.choice(["X", "0"]))  # jaunu spēli sāk nejauši izvēlēts spēlētājs
        # ja neievada y, programmas izpilde neturpinās


# Spēli sāk X
jaunaSpele("X")  # startējot programmu, spēli sāk X
