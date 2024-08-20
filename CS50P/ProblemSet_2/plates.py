def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #first condition to make sure the entered is not less than 2 or greater than 6
    if len(s) < 2 or len(s) > 6:
        return False
    
    #2nd cond, to check if the first and second letter is not an alphabet then invaLid
    #.isalpha() return true if the word contains an alphabet
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    
    #3rd cond, aslong as i=0 is false ie it is not an alphabet, then checking if it is a zero,
    #if it is then return false, else break the statement and then increament i by 1
    i=0
    while i< len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i +=1

    #4th cond, chechking for punctuations
    for c in s:
        if c in [" ", "!", ".", "?"]:
            return False
        
    #if neither of the above conditions are met , then return true    
    return True

main()