def generateJews(jews):
	a_list = []

	for jew in range (jews):
		a_list.append(jew)

	yield from a_list


the_jews = list(generateJews(1000000))
print(generateJews(100000))
print(the_jews[458898])
		
