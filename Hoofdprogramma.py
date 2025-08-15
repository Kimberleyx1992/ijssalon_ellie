from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aardbeienijs, emmertje van 5 lieter: 5 euro")
uitvoer.append("Slaproom, spuitbus van 1 liter: 2 euro")

print()

for el in uitvoer:
    print(el)