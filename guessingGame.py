import random
number = random.randint(1, 9)

chances = 5

print('Guess a number (between 1 and 9): ')

while chances < 5:

     print()
     guess = int(input("Enter your guess:- "))

     if guess == number:
          print("Congratulations!! YOU WIN ")
          print()
          print('Thank you for playing "Number Guessing Game".')
          print('Run the terminal again to play the game.')
          break

     elif guess < number:
          print("Your guess was too low: Guess a number higher than ", guess)

     else:
         print("Your guess was too high: Guess a number lower than", guess)

     chances = chances + 1

if not chances < 5:
     print()
     print("YOU LOSE !!! The number is ", number)      
     print()
     print('Thank you for playing "Number Guessing Game".')
     print('Run the terminal again to play the game.')
