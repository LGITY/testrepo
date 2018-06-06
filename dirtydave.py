def generateJews(jews):
	a_list = []

	for jew in range (jews):
		a_list.append(jew)

	yield from a_list


print(generateJews(100000))
		
