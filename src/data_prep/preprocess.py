
with open("../../data/Cuentos/La_marea.txt") as f:

	for x in f:
		if x=='\n':
			pass
		else:
			print(x)