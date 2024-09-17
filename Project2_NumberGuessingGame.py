import random

randnum= random.randint(1,100)
takein=0
count=0

while takein!=randnum:
    count+=1
    try:
        takein= int(input("Enter your guess: "))

    except TypeError:
        print("Error! Wrong type of data!")
    if takein<randnum:
        print("Too low!")
    elif takein>randnum:
        print("Too high!")
    else: print(f"Congratulations! You've guessed the number in {count} attempts")




