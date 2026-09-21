import random
# Random float between 0 and 1
value = random.random()
# Random integer where 1 <= integer <= 10
value = random.randint(1, 10)
# Random choice between "Left" or "Right"
value = random.choice(["Left", "Right"])

# Another valid syntax for random choice
choices = ["Left", "Right"]
value = random.choice(choices)
guess = input("What is your guess?\n")

guess = guess.lower()
guess = input("What is your guess?\n")

guess = guess.lower()