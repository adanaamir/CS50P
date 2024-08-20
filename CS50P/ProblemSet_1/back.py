#taking greetings
answer = input("Greeting: ")
#lowering if user enters in capital or adds more space
ans = answer.lower().strip()
#a condition for strings where you can check a specific word in a sentence
if "hello" in ans:
    print("$0")
#checking if only the first word is h
elif "h"== ans[0]:
    print("$20")
else:
    print("$100")