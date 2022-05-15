import random

def getComputerOption():
    num = random.randint(1, 3)
    if num == 1:
        return 'r'
    elif num == 2:
        return 'p'
    elif num == 3:
        return 's'

def getUserOption():
    print("Rock, Paper and Scissors Game!")
    print("Choose one of the following options")
    print("-----------------------------------")
    printChoose()
    c = input("Your choose: ")
    while c != 'r' and c != 'p' and c != 's':
        print("Please enter one of the following options only.")
        printChoose()
        c = input("Your choose: ")
    return c

def printChoose():
    print("(r) for rock")
    print("(p) for paper")
    print("(s) for scissors")

def getSelectedOption(option):
    if option == 'r':
        return "ROCK"
    elif option == 'p':
        return "PAPER"
    elif option == 's':
        return "SCISSORS"
    else:
        return "unknown"

def chooseWinner(uChoice, cChoice):
    if uChoice == "ROCK" and cChoice == "PAPER":
        print("Computer Wins! Paper wraps Rock.")
    elif uChoice == "ROCK" and cChoice == "SCISSORS":
        print("You Win! Paper wraps Rock.")
    elif uChoice == "PAPER" and cChoice == "SCISSORS":
        print("Computer Wins! Scissors cut Paper.")
    elif uChoice == "PAPER" and cChoice == "ROCK":
        print("You Win! Paper wraps Rock.")
    elif uChoice == "SCISSORS" and cChoice == "ROCK":
        print("Computer Wins! Rock smashes Scissors.")
    elif uChoice == "SCISSORS" and cChoice == "PAPER":
        print("You Win! Scissors cut Paper.")
    else:
        print("Tie. Play again win the Game.")

def main():
    # User's choice
    uInput = getUserOption()
    uChoice = getSelectedOption(uInput)
    print("Your choice is: " + uChoice)
    # Compter's choice
    cInput = getComputerOption()
    cChoice = getSelectedOption(cInput)
    print("Computer's choice is: " + cChoice)
    # detect winner
    chooseWinner(uChoice, cChoice)

main()