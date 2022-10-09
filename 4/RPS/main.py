import random


def Again():
    tryAgain = input("Try again y/n \nr")
    if tryAgain == "y":
        Play()
    else:
        quit()


def Play():
    move = ['r', 's', 'p']

    print("Welcome to Rock Paper Scissors")

    selection = input("Make your move. r/p/s\n")
    ai = random.choice(move)

    if selection == 'r' and ai == 'r':
        print("Even")
        Again()
    elif selection == 'r' and ai == 's':
        print("Player Won")
        Again()
    elif selection == 'r' and ai == 'p':
        print("CPU Won")
        Again()
    elif selection == 's' and ai == 'r':
        print("CPU Won")
        Again()
    elif selection == 's' and ai == 's':
        print("Even")
        Again()
    elif selection == 's' and ai == 'p':
        print("Player Won")
        Again()
    elif selection == 'p' and ai == 'r':
        print("Player Won")
        Again()
    elif selection == 'p' and ai == 's':
        print("CPU Won")
        Again()
    elif selection == 'p' and ai == 'p':
        print("Even")
        Again()
    else:
        print("I don't know what have you done. I'm ending you!")
        quit()

    Play(selection, ai)


Play()
