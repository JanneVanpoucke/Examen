# examen oefening 5

from functies import *
controleGetal = int(input("Geef het te controleren getal in: "))
if (echteDelersGroter(controleGetal)==True):
	print("Resultaat: De som van alle delers van ",controleGetal,"is groter")
else:
	print("Resultaat: De som van alle delers van",controleGetal,"is niet groter")

#bewerking
# controleGetal = int(input("Controle van het getal: "))

# echteDelers = []
# teller = 0

# for x in range(1,controleGetal):
# 	if controleGetal%x==0:
# 		echteDelers.append(x)
# 	else:
# 		teller += 1
# # print(echteDelers)
# somVanEchteDelers = sum(echteDelers)

# if somVanEchteDelers > controleGetal:
# 	print("Resultaat: De som van alle delers van ",controleGetal,"is groter")
# else:
# 	print("Resultaat: De som van alle delers van",controleGetal,"is niet groter")


# def echteDelersGroter(controleGetal):
# 	echteDelers = []
# 	teller = 0
# 	for x in range(1,controleGetal):
# 		if controleGetal%x==0:
# 			echteDelers.append(x)
# 		else:
# 			teller += 1
# 	somVanEchteDelers = sum(echteDelers)
# 	if somVanEchteDelers > controleGetal:
# 		return True
# 	else:
# 		return False