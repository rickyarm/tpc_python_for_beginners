import random

print("---------------------------")
print("       New M&M Guessing game!")
print("---------------------------")

mm_count = random.randint(0, 10000)
attempts_limit = 5
attempts = 0

while attempts < attempts_limit:
    guess_text = input("How many M&Ms are in the jar?  ")
    guess = int(guess_text)

    if mm_count == guess:
        print("You Win")
        break
    elif mm_count > guess:
        print("Too Low")
    elif mm_count < guess:
        print("Too High")

    attempts += 1
