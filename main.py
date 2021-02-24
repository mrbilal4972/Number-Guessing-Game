import random

randNo = random.randint(1,100)
userGuess = None
totalGuesses = 0

# Loop runs until guess matched
while randNo!=userGuess:
    try: # Try box handle the invalid input from user, like: alphbet or special character
        userGuess = int(input("Guess the number between 1 to 100: "))
        if randNo != userGuess:
            if userGuess>randNo:
                print("Your guess is wrong, Select the smaller number")
            else:
                print("Your guess is wrong, Select the Larger number")
        else:
            print("Congratulations!! Your guess is correct")
        totalGuesses += 1
    except Exception as e:
        print("Invalid Input!! Please Enter Valid Number")

print(f'''you got the correct answer after "{totalGuesses}" Guesses''')

# If Highest score was made it will stored in file hiScore.txt
with open("hiScore.txt") as f:
    prevScore = int(f.read())

if totalGuesses<prevScore:
    print("you Broke the Highest Score")
    newScore = str(totalGuesses)
    with open("hiScore.txt", 'w') as f:
        f.write(newScore)