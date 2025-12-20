import random

roll = random.randint(1, 6)
dice = int(input("Enter a number between 1 and 6: "))

if dice == roll:
    print("Amazing! You guessed it!")
    
else:
    print(f"Sorry, it’s not this number {dice}.")
    
    print(f"Correct dice roll is: {roll}.")
    
print("Nice playing with you.")