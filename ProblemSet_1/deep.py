answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
if answer.lower().strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
else:
    print("No")