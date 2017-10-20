import os
def pigify(rawInString):
	#needs a little bit of formatting to get the ball rolling
	inString = ''
	inString = str.lower(rawInString)
	outString = ''
	if (len(inString) < 3):
		inString = inString + 'e'
	#this initializes the two strings that we'll be manipulating today
	#it also ensures that the input and outputs will be considered as lower case

	#get ready for the mother of all 'if' statements
	if ((inString[0] == 'a') or (inString[0] == 'e') or (inString[0] == 'i') or (inString[0] == 'o') or (inString[0] == 'u')):
		outString = inString + 'way'
	elif (((inString[0] != 'a') or (inString[0] != 'e') or (inString[0] != 'i') or (inString[0] != 'o') or (inString[0] != 'u')) and ((inString[1] == 'a') or (inString[1] == 'e') or (inString[1] == 'i') or (inString[1] == 'o') or (inString[1] == 'u') or (inString[1] == 'y'))):
		outString = inString[1:] + inString[0] + 'ay'
	elif (((inString[0] != 'a') or (inString[0] != 'e') or (inString[0] != 'i') or (inString[0] != 'o') or (inString[0] != 'u')) and ((inString[1] != 'a') or (inString[1] != 'e') or (inString[1] != 'i') or (inString[1] != 'o') or (inString[1] != 'u')) and ((inString[2] == 'a') or (inString[2] == 'e') or (inString[2] == 'i') or (inString[2] == 'o') or (inString[2] == 'u'))):
		outString = inString[2:] + inString[:2] + 'ay'
	elif (((inString[0] != 'a') or (inString[0] != 'e') or (inString[0] != 'i') or (inString[0] != 'o') or (inString[0] != 'u')) and ((inString[1] != 'a') or (inString[1] != 'e') or (inString[1] != 'i') or (inString[1] != 'o') or (inString[1] != 'u')) and ((inString[2] != 'a') or (inString[2] != 'e') or (inString[2] != 'i') or (inString[2] != 'o') or (inString[2] != 'u'))):
		outString = inString[3:] + inString[:3] + 'ay'

	#now that i've committed programming sacrilige, let's send back our pig latin word!
	return outString
def writer(inBook, outBook):
	bookString = ''
	fooforopeningtheoutput = open(outBook, 'w')
	fooforopeningtheoutput.write('')
	fooforopeningtheoutput.close()

	with open(inBook,'r') as f:
		for line in f:
			for word in line.split():
				bookString = filter(str.isalnum, word)
				with open(outBook, 'a') as g:
					bookString = pigify(bookString)
					g.write(bookString + ' ')

for i in os.listdir('inBook'):
	writer('inBook/'+i,'outBook/'+i)
	print('inBook/'+i+'written into outBook/'+i)
