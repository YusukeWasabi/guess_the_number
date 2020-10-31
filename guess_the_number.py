from random import randint

print("///// MATCH YOUR NUMBER WITH THE COMPUTER'S NUMBER /////")
print("///// Press '0' at any time to quit. /////\n")

while True:
    x = randint(1, 6)
    y = int(input("Write your number: "))
    if x == y:
        print("\nBoth your and the PC's number matched! Hooray!")
        print(f"Computer's number: {x} // Your number: {y}\n")
        break
    elif y == (int(0)):
        print("Quitting........")
        break
    else:
        print(f"\nComputer's number: {x} // Your number: {y}")
        print("Numbers didn't match, try again!\n")
