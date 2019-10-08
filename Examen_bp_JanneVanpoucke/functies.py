#####FUNCTIES
#formule om van Celsius naar Farenheit te gaan =  C × 1.8 + 32
#Celsius naar Fahrenheit
def celNaarFar(graden):
    far = graden * 1.8 + 32
    return far

#Som van de echte delers groter of niet
def echteDelersGroter(controleGetal):
	echteDelers = []
	teller = 0
	for x in range(1,controleGetal):
		if controleGetal%x==0:
			echteDelers.append(x)
		else:
			teller += 1
	somVanEchteDelers = sum(echteDelers)
	if somVanEchteDelers > controleGetal:
		return True
	else:
		return False