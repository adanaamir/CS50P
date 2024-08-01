def main():
    s = input("Input: ")
    if is_valid(s) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #checking first condition
    if len(s) < 2 or len(s) > 6:
        return False
    
    #checking second condition
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    
    #checking third condiiton
    i=0
    #this loop means the last digit will not be checked, so if it is 0 (if the cond was =len(s)) then it wouldbe been false
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i+=1

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    #checking forth condition
    for punc in s:
        if punc in ["?", ",", ".", "!", " "]:
            return False
    
    return True

if __name__ == "__main__":
    main()