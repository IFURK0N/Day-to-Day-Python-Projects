def GameOver():
    input("You did some thing that I can't understand so I kicked you out!")
    quit()


def Again():
    again = input("Would you like to try again? y/n\n")
    if again == "y":
        Play()
    elif again == "n":
        quit()
    else:
        GameOver()


def Play():
    print("Welcome to Treasure Island\n")
    print("Remember your chose will change your destiny!")
    selection = input(
        "You're at a corner would you turn l or r? left/right \n")
    selection.lower()
    if selection == "r":
        selection = input(
            "You're at a corner and there is a arrow sign to right would you turn l or r? left/right \n")
        if selection == "r":
            print("Sorry, but you fell in to pee lake. You slowly sinking.")
            Again()

        elif selection == "l":
            selection = input(
                "You're at a cornery would you turn l or r? left/right \n")
            if selection == "r":
                print("Sorry, mate some rock hit to your head and you gone blind. Then some kind of arm gets you through fire. You are eaten while alive. \n")
                Again()
            elif selection == "l":
                selection = input(
                    "You're at a corner would you turn l or r? left/right \n")
                if selection == "r":
                    print("Sorry, but you fell in to pee lake. You slowly sinking.")
                    Again()
                elif selection == "l":
                    print("You made it! You're free to fall from edge...")
                    Again()
                else:
                    GameOver()
            else:
                GameOver()
        else:
            GameOver()

    elif selection == "l":
        selection = input(
            "You're at a corner would you turn l or r? left/right \n")
        if selection == "r":
            print("You should have chosen the other way :(")
            Again()
        elif selection == "l":
            selection = input(
                "You're at a corner would you turn l or r? left/right \n")
            if selection == "r":
                selection = input(
                    "Some sounds comes from left. You're at a corner would you turn l or r? left/right \n")
                if selection == "r":
                    print(
                        "You did it you won this game. Don't use same way ther is some other correct ways too :)")
                    Again()
                elif selection == "l":
                    print(
                        "You died in the hand of Orc Vukcan. Don't use same way :(")
                    Again()
                else:
                    GameOver()
            elif selection == "l":
                print(
                    "You did it you won this game. Come on, get on the eagle and go home. :)")
                Again()
            else:
                GameOver()
        else:
            GameOver()
    else:
        GameOver()


Play()
