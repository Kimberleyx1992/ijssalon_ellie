from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs 1 liter in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten deze week is {totaal:.2f} euro, waarover {btw_bedrag} euro btw betaald moet worden"

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    gem = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gem:.2f} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]

print(aanbieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal(week_inkomsten, 0.09))
print(laag_en_hoog(week_inkomsten))
print(gemiddelde(week_inkomsten))
print(meervoudig([10, 5, 3, 2, 1, 2, 9]))
print(combinatie([10, 5, 3, 2, 1, 2, 9]))