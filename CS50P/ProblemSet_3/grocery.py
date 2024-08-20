grocery_list ={}

while True:
    try:
        items = input().lower()

        if items in grocery_list:
        #if item i alr present in dic, then add 1 to it
            grocery_list[items] += 1
        #otherwise initializing our item = 1 , which means only 1 of it is present
        else:
            grocery_list[items] = 1 

    except EOFError:
        #sorting the keys in alphabetical order
        for key in sorted(grocery_list.keys()):
            print( grocery_list[key],key.upper())
        break