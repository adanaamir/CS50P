expression = input("Expression: ")
#using split function for strings, when you have to split a string in tbe brackets add on 
# which point you want the strings to be split example in this case (" ") its a single space
x, y, z = expression.split(" ")
#converting the types of x and z
new_x = float(x)
new_z = float(z)
#conditions for operations
if y == "+":
    ans = new_x+new_z
elif y== "-":
    ans = new_x-new_z
elif y== "*":
    ans = new_x*new_z
elif y == "/":
    ans = new_x/new_z
#rounding the answer to 1 decimal places
print(round(ans, 1))
