import random


def print_result():
    print("Computer:", computer)
    print("Human:", human)


def print_you_lose():
    print("You lose!")


def print_you_win():
    print("You win!")


choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
human = None

while True:
    while human not in choices:
        human = input("Rock, Paper, or Scissors?: ").lower()

    print_result()

    if computer == human:
        print("It's a tie!")
    elif computer == "rock":
        if human == "paper":
            print_you_win()
        elif human == "scissors":
            print_you_lose()
    elif computer == "paper":
        if human == "rock":
            print_you_lose()
        elif human == "scissors":
            print_you_win()
    elif computer == "scissors":
        if human == "rock":
            print_you_win()
        elif human == "paper":
            print_you_lose()

    human = None
