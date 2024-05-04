import random
def guessnumber():
    answer = random.randint(1, 100)
    attempts = 0    
    print("Welcome to the Guess the Number game!")
    print("I've picked a number between 1 and 100. Try to guess it.")
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            if guess < answer:
                print("Too low! Try again.")
            elif guess > answer:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number correctly!")
                print(f"It took you {attempts} attempts to win the game.")
                break
        except:
            print("Please enter a valid number.")
guessnumber()