#examen oefening 1
eindGetal = int(input("Hoeveel getallen wil je ingeven?:"))
reeksEen = []
reeksTwee = []
teller = 0

for x in range(0,eindGetal):
	willekeurigGetalGebruiker = int(input("Voer getal in:"))
	if willekeurigGetalGebruiker%2==0:
		reeksEen.append(willekeurigGetalGebruiker)
	else:
		reeksTwee.append(willekeurigGetalGebruiker)
		teller = teller +1

samenvoegen = reeksTwee + reeksEen
print(samenvoegen)