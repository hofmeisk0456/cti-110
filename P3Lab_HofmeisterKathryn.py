# Kathryn Hofmeister
# 6/29/25
# P3LAB_HofmeisterKathryn
# This program takes a float input of money and breaks it down into the most efficient number
# of dollars, quarters, dimes, nickels, and pennies.

# Get the input amount
amount = float(input("Enter the amount of money as a float: $"))

# Convert to cents to avoid float inaccuracies
cents = int(round(amount * 100))

if cents == 0:
    print("No change")
else:
    if cents >= 100:
        dollars = cents // 100
        cents %= 100
        print(f"{dollars} Dollar" + ("s" if dollars > 1 else ""))
    if cents >= 25:
        quarters = cents // 25
        cents %= 25
        print(f"{quarters} Quarter" + ("s" if quarters > 1 else ""))
    if cents >= 10:
        dimes = cents // 10
        cents %= 10
        print(f"{dimes} Dime" + ("s" if dimes > 1 else ""))
    if cents >= 5:
        nickels = cents // 5
        cents %= 5
        print(f"{nickels} Nickel" + ("s" if nickels > 1 else ""))
    if cents >= 1:
        pennies = cents
        print(f"{pennies} Penn" + ("ies" if pennies > 1 else "y"))
