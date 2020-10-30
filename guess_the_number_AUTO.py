from random import randint

print("///// THIS PROGRAM STOPS WHEN BOTH 'X' and 'Y' values are the same /////\n")

while True:
    x = randint(2, 8)
    y = randint(2, 8)
    if x == y:
        print("\tBoth X and Y matched! Hooray!")
        print(f"\tX = {x} and Y = {y}")
        break
    else:
        print(f"X = {x} and Y = {y}")
        print("Numbers didn't match.\n")
