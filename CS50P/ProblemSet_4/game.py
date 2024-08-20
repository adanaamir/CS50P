import random

while True:
    try:
        n = int(input("Level: "))
        
        rand_num = random.randint(1,n)

        while True:
            try:
                guess = int(input("Guess: "))
                if guess > 0:
                    if guess == rand_num:
                        print("Just right!")
                        break
                    elif guess > rand_num:
                        print("Too large!")
                    else:
                        print("Too small!")
            except ValueError:
                pass
        break   

    except ValueError:
        pass

