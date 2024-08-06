#L2 Challenge 2: Task 1
#Guessing game - User guesses a secret number
#Then tells user if too large or too small
#keep count of amount of tries
#at the end - put number of tries (same number doesnt increase count)
#if guess right print "You Won!"
#python L2_Challenge2_Task1.py

def secret_num():
    import random
    for i in range(1):
        return(random.randrange(1,100))

def get_number():
    return int(input("Guess the number between 1-100: "))

def game():
    secret_number = secret_num()
    guess = get_number()
    guess_count = 1
    while True:
        if guess == secret_number:
            if guess_count == 1:
                return ("You Won! You guessed it in {} try.".format(guess_count))
            else:
                return ("You Won! You guessed it in {} tries.".format(guess_count))
        elif guess > secret_number:
            print ("Too high...guess again")
            guess = get_number()
        elif guess < secret_number:
            print ("Too low...guess again")
            guess = get_number()
        guess_count += 1

print(game())

print(game())
