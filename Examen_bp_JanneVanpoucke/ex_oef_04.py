#examen oefening 4
hoeveelNamen = int(input("Hoeveel namen wil je ingeven: "))
lijstNamen = []
teller = 0

for x in range(0, hoeveelNamen):
	naam = input("Geef een naam in:")
	if len(naam)>5:
		lijstNamen.append(naam)
	else:
		teller += 1
print(lijstNamen)