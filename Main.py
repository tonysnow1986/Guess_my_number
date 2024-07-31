# Choosing a number from 1 to 100
from random import randint
from Art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """checks answer vs guess. Returns the amount of turns remaining"""
    if guess > answer:
        print("Too high!!")
        return turns - 1
    elif guess < answer:
        print("Too Low!!!")
        return turns - 1
    else:
        print(f"Nice job you nailed it! My number was {answer}!!!")


def set_difficulty():
    level = input("Choose your level of difficulty. easy or hard choose one: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to What's the Number!!!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Out of guesses!! You lose!!!")
            print(f"My number was {answer}!!")
            return
        elif guess != answer:
            print("Take another guess!!")
        # Let the user guess a number.


game()
