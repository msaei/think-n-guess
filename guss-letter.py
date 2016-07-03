# this is a python program for a gusing game named under curtain.
# there is a combination of four different letters that picked from 6 letters.
# every time player guse the combination will get a score that shows how close was. 
# 10 points for every correct letter in correct position and 1 point for any correct
# letter that is not in correct possition. game continues until player find right 
# combination that means get 40 points.

import random
def get_combination():
	letters="abcdef"
	combination=""
	while len(combination) < 4 :
		random_num = random.randint(0,5)
		random_letter = letters[random_num]
		if combination.find(random_letter) == -1 :
			combination = combination + random_letter
	return combination
	


def get_score(guess, goal):
	score=0
	for i in range(4):

		if goal.find(guess[i])!= -1 :

			if goal[i] == guess[i]:

				score= score + 10
			else: 
				score = score + 1
	return score
	
def main():
	print("game rules ....")
	goal_comb = get_combination()
	print(goal_comb)
	gue_score = 0
	while gue_score != 40:
		player_guess = input("enter your guess:")
		print(player_guess)
		gue_score = get_score(player_guess, goal_comb)
		print('score:',gue_score)
	print('you won, combination was: ', goal_comb)
	
main()