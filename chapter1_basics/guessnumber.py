"""
Author: Heriberto Prieto
Plays a game of guess the number with the user.
"""

#import libraries
import random

#initialize main
def main():
	"""
		Inputs the bounds of the range
		of numbers and lets the user guess the
		computer's number until the guess is correct
	"""
	smaller  = int(input("Enter the smaller number: "))
	larger   = int(input("Enter the larger number:  "))
	myNumber = random.randint(smaller,larger)
	count    = 0
	while True:
		cout+=1
		userNumber = int(input("Enter your guess:"))
		if userNumber < myNumber:
			print("Too Small")
		elif userNumber > myNumber:
			print("Too Large")
		else:
			print("You've got it in",count,"tries!")
			break
	if __name__ == "__main__":
		main()



