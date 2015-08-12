def chop(intNum,intArray):
	try:
		indexNum = intArray.index(intNum)
	except ValueError:
		indexNum = -1

	return indexNum



