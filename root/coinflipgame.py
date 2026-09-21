import random

incorrect_guesses = 0

while incorrect_guesses < 3:

    coin = random.choice(["heads", "tails"])

    # Input validation
    while True:
        guess = input("Guess heads or tails: ").lower()

        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input. Please enter heads or tails.")

    # Check the guess
    if guess == coin:
        print("Correct!")
        incorrect_guesses = 0
    else:
        incorrect_guesses += 1
        print("Incorrect!")
        print("The coin was", coin)

    # Show strikes
    print("Incorrect guesses in a row:", incorrect_guesses)
    print()

print("Game over! You got 3 incorrect guesses in a row.")