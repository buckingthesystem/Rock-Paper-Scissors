'''This is a Rock Paper Scissors Game'''

import random 

'''This is the function that houses the variables for use in the Game function'''
def var():
	
	#I made the variables attributes of the var() function to use in the the Game(plays) function
	var.hands = ['R','P','S']
	var.invalid = "Invalid Play. Read the directions below and try again"
	var.lose = "You lose!"
	var.win = "You win!"
	var.tie = "Tie!"
	var.greeting = "\nWelcome to Gary's Rock, Paper, Scissors Game!"
	var.directions = "Type (R) for Rock, (P) for Paper, (S) for Scissors or (Q) to Quit the game and then press Enter\n"
	var.your_result = ''
	var.computer_result = ''
	var.your_score = []
	var.computer_score = []
	var.quit = 'Q'
	var.w = 'win'
	var.goodbye = 'Thanks for playing!'
	var.final_scores = 'Final Scores:'
	
'''This is the main function that houses the logic of the game'''
def game(variables):

	#prints a greeting, game directions, and requests player to type their name
	print(var.greeting)
	print(var.directions)
	players_name = input("Type your name: ")

	#the while loop houses the if/elif/else logic for the game and is nested in an if statement to prevent the while loop from running after quiting the game. 
	#the number of wins are tabulated for the player and computer
	#if the player enters something beyond R, P, S or Q then an invalid entry notice is shown to the player, and they are asked to re-enter their hand
	end = ''
	if end != var.quit:
		while end != var.quit:

			play = input(f"{players_name}'s Hand: ")
				
			if play != var.quit:
				computer = random.choice(var.hands)
				print(f"Computer's Hand: {computer}\n")
			
			if play == var.quit:
				end = var.quit
				print(f"{var.goodbye}\n")
				print(f"{var.final_scores} ")
				print(f"{players_name} - {str(var.your_score.count(var.w))}")
				print(f"Computer:  {str(var.computer_score.count(var.w))}")
				print("\n")

			elif play == var.hands[0] and computer == var.hands[0]:
				print(F"{var.tie}\n")

			elif play == var.hands[0] and computer == var.hands[1]:
				print(f"{players_name} - {var.lose}\n")
				var.computer_result = var.w
				var.computer_score.append(var.computer_result)

			elif play == var.hands[0] and computer == var.hands[2]:
				print(f"{players_name} - {var.win}\n")
				var.your_result = var.w
				var.your_score.append(var.your_result)

			elif play == var.hands[1] and computer == var.hands[0]:
				print(f"{players_name} - {var.win}\n")
				var.your_result = var.w
				var.your_score.append(var.your_result)
				
			elif play == var.hands[1] and computer == var.hands[1] :
				print(f"{var.tie}\n")

			elif play == var.hands[1] and computer == var.hands[2]:
				print(f"{players_name} - {var.lose}\n")
				var.computer_result = var.w
				var.computer_score.append(var.computer_result)

			elif play == var.hands[2] and computer == var.hands [0]:
				print(f"{players_name} - {var.lose}\n")
				var.computer_result = var.w
				var.computer_score.append(var.computer_result)

			elif play == var.hands[2] and computer == var.hands[1]:
				print(f"{players_name} - {var.win}\n")
				var.your_result = var.w
				var.your_score.append(var.your_result)
	
			elif play == var.hands[2] and computer == var.hands[2]:
				print(f"{var.tie}\n")

			else:
				if play != var.hands[0] or var.hands[1] or var.hands[2] or var.quit:
					print(f"{var.invalid}, {players_name}")
					print(var.directions)

game(var())
