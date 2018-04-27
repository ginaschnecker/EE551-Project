parseData = open("user_input.txt","r")


for line in parseData:

	if "Science" in line:	
		column=line.split(":")
		if len(column[0])<8:
			scienceelective=column[1]
		else:
			sciencelab=column[1]

parseData.close()
