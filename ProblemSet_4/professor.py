import random

def main():
    level_no = get_level()
    score = 0
    for _ in range(10):
        attempts = 0
        n1, n2 = generate_integer(level_no)  

        while attempts < 3:
            try:
                ans = int(input(f"{n1} + {n2} = "))
                if ans == n1+n2:
                    #if ans is correct then break the statement
                    score +=1
                    break
                #else contine and ask the same question
                else:
                    attempts+=1
                    print("EEE")
                    if attempts == 3:
                        print(f"{n1} + {n2} = {n1+n2}")  

            except ValueError:
                print("EEE")

    print("Score:", score )

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    #if entered level is 1 then print numbers according to those digits
        for _ in range(10):
            if level == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
                return x,y
            elif level == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)
                return x,y
            else:
                x = random.randint(100,999)
                y = random.randint(100,999)
                return x,y

if __name__ == "__main__":
    main()