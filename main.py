import random

randNo = random.randint(1,100)
userGuess = None
totalGuesses = 0

# Loop runs until guess matched
while randNo!=userGuess:
    userGuess = int(input("Guess the number between 1 to 100: "))
    if randNo != userGuess:
        if userGuess>randNo:
            print("Your guess is wrong, Select the smaller number")
        else:
            print("Your guess is wrong, Select the Larger number")
    else:
        print("Congratulations!! Your guess is correct")
    totalGuesses += 1

print(f'''you got the correct answer after "{totalGuesses}" Guesses''')