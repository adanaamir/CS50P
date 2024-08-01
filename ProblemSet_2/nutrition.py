fruits = {
    "apple" : 130,
    "avacado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapoefruit" : 60,
    "grapes" : 90,
    "banana" : 50, 
    "honeydew melon" : 90,
    "kiwifruit" : 15,
    "lemon" : 20,
    "lime" : 60,
    "nectarine" : 80,
    "peach" : 60, 
    "pear" : 100, 
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

item = input("Item: ")
new_item = item.lower().strip()

#iterating throught the dictionary
for i in fruits:
    #if i matches the input, then print the calories.
    if i == new_item:
        print("Calories:", fruits[i] )
