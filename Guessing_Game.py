import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(users_guess, correct_number, turns):
    if users_guess > correct_number:
        print("Too High")
        return turns - 1
    elif users_guess < correct_number:
        print("Too Low")
        return turns - 1
    else:
        print(f"You're correct, the answer is {correct_number}!")

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 10!")

def game():
    number = random.randint(1,100)

    def set_difficulty():
        difficulty = (input("Choose a difficulty level. 'easy' or 'hard': "))
        if difficulty == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS

    turns = set_difficulty()


    guess = 0
    while guess != number:
        print(f"You have {turns} attempts to make a guess")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You lose!")
            return
        elif guess != number:
            print("Guess again!")

game()


