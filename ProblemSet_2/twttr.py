text = input("input: ")

print("output: ", end="")
for vowel in text:
    #if there are no a,e,i,o,u in text (using vowel to iterate) then print each letter of input 
    #else if there are , then skip the vowels and print the rest
    if not vowel.lower() in ["a","e","i","o","u"]:
        print(vowel, end="")
 
print()
