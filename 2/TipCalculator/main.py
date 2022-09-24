def Calculate():
    print("Welcome to Tip Calculator\n")
    bill = float(input("What was the total bill?\n"))
    tip = float(input("What percentage tip you like to giv?\n"))
    people = int(input("How many people to split bill?\n"))
    final_bill = ((bill / 100) * tip + bill) / people
    round(final_bill, 2)
    print(f"Each person must pay {final_bill}")
    again = input("Would you like to calculate another? y/n\n")
    if again == "y":
        Calculate()
    else:
        quit()


Calculate()
