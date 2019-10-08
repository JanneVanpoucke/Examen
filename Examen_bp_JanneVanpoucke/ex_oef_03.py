#examen oefening 3
waarde = int(input("Geef een getal in: "))
afdrukOpScherm = ""
som = 0
teller = 1
eindGetal = "="

for x in range(0,4):
	teller = waarde
	som = som + int(str(teller) + str(teller)*x)
	afdrukOpScherm += str(teller) + str(teller)*x + "+"

eindGetal = eindGetal + str(som)
afdrukOpScherm = afdrukOpScherm[:-1]

print(afdrukOpScherm,eindGetal)