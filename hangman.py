def print_hang(guesses):
	if guesses == 0:
		print ("________      ")
		print ("|      |      ")
		print ("|             ")
		print ("|             ")
		print ("|             ")
		print ("|             ")
	elif guesses == 1:
		print ("________      ")
		print ("|      |      ")
		print ("|      0      ")
		print ("|             ")
		print ("|             ")
		print ("|             ")
	elif guesses == 2:
		print ("________      ")
		print ("|      |      ")
		print ("|      0      ")
		print ("|     /       ")
		print ("|             ")
		print ("|             ")
	elif guesses == 3:
		print ("________      ")
		print ("|      |      ")
		print ("|      0      ")
		print ("|     /|      ")
		print ("|             ")
		print ("|             ")
	elif guesses == 4:
		print ("________      ")
		print ("|      |      ")
		print ("|      0      ")
		print ("|     /|\     ")
		print ("|             ")
		print ("|             ")
	elif guesses == 5:
		print ("________      ")
		print ("|      |      ")
		print ("|      0      ")
		print ("|     /|\     ")
		print ("|     /       ")
		print ("|             ")
	else:
		print ("________      ")
		print ("|      |      ")
		print ("|      0      ")
		print ("|     /|\     ")
		print ("|     / \     ")
		print ("|             ")
		print ("The noose tightens around your neck, and you feel the")
		print ("sudden urge to urinate.")
		print ("GAME OVER!\n")

#print_hang(3)
#text = open("words.txt", "r")
#dictionary = text.read().split('\n')
#for x in range(len(dictionary)):
#	print(dictionary[x])

#test
