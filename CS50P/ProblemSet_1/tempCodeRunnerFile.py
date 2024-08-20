expression = input("Expression: ")
x, y, z = expression.split(" ")
new_x = float(x)
new_z = float(z)
if y == "+":
    ans = new_x+new_z
elif y== "-":
    ans = new_x-new_z
elif y== "*":
    ans = new_x*new_z
elif y == "/":
    if z == 0:
        print("Zero Division Error")
    else:
        ans = new_x/new_z
else:
    print("huh?")
print(round(ans, 1))