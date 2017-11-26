while True:
	print("Wanna play Rock/Paper/Scissors?")
	print("Press y for Yes and n for no.")
	response = input()

	if (response == 'y'):

		print("Let's start.")
		print("Player1: Rock/Paper/Scissors?")
		movelist = []
		movelist.append(input())
		print("Player2: Rock/Paper/Scissors?")
		movelist.append(input())

		for i in range(len(movelist)):
			move = movelist[i]
			if (move == "Rock" or move == "rock" or move == "r"):
				movelist[i] = int(1)
			elif (move == "Paper" or move == "paper" or move == "p"):
				movelist[i] = int(2)
			elif (move == "Scissors" or move == "scissors" or move == "s"):
				movelist[i] = int(3)
			else:
				movelist[i] = int(0)

		if (not (movelist[0] or movelist[1])):
			print("Haha! Wrong input.")	
		elif (movelist[0] == movelist[1]):
			print("Haha! Cheating is not allowed.")
		elif ( ( movelist[0] == 2 and movelist[1] == 1) or (movelist[0] == 3 and movelist[1] == 2) or (movelist[0] == 1 and movelist[1] == 3)):
			print("Player1 wins!")
		else:
			print("Player2 wins!")

	else:
		if (response == "n"):
			print("Sorry to see you go!")
			break
		else:
			print("I don't understand you! Retry.")