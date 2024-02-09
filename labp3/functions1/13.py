import random

def guess_the_number():

    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    guess = 0

    while guess != secret_number:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break

    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")

if __name__ == "__main__":
    guess_the_number()
