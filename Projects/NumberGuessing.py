import random

real_num = random.randint(1,100)
tries = 0
while True:
    tries+=1
    guess_num = int(input("Guess a number between 1 and 100: "))
    if real_num > guess_num:
        print("Wrong guess, go higher!!")
    elif real_num < guess_num:
        print("Wrong guess, go lower!!")
    else:
        print(f"Congratulations!! You have guessed the right number in {tries} tries.")
        break
