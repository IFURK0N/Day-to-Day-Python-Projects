import random

ready_name = ["Stage Revolution", "Velvet Concord", "Ecstasy", "Afternoon Daydream", "Turning Jane",
              "Elaborate Constellations", "Double Helix", "Zombie Hoax", "Hero of Refusal", "Armageddon Day",
              "Perpetual Sorrow", "Kinetic Street", "Greatest Day", "Tokyo Lights", "Ghost Town", "Ultraviolet",
              "Titan Walk", "Pretty Ugly", "Boys of Creation", "Lies and Lullabies", "Country Band Names",
              "The Ole Fiddler and His Merrymen", "The Whiskey River Rats", "Montana Sunrise", "Cowboys & Heartbreaks",
              "Dirt Circles", "Bootleggers", "Tennesse Dreamin’", "Big Fish", "Son of a"
              ]


def Process():
    print("Welcome to Band Name Generator\n")
    ready = input("Do you want to use preset names? y/n \n")
    if ready == "y":
        print("Your band name " + random.choice(ready_name))
    else:
        city_name = input("What's name of the city you grew up?\n")
        pet_name = input("What's name of your first pet or toy?\n")
        print(f"Your band name is {city_name}'s {pet_name}")
    try_again = input("Would you like to try again? y/n \n")
    if try_again == "y":
        Process()
    else:
        quit()


Process()
