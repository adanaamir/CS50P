import inflect

#creating an object
p = inflect.engine()

#creating an empty list to store the names
names_list = []

while True:
    try:
        names = input("Name: ")
        
        #adding names to list
        names_list.append(names)

    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(names_list)}")