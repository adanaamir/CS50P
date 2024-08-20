camelcase = input("camelCase: ")
snakecase = print("snake_case: ", end="")
#iterating through the input to see if there is any capital word, if yes then replace it with "_" and lower
#that word, if not then (else) then simply, print that word. end="" so that it remains on the same line
for i in camelcase:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")

