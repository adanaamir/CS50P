while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        new_x = int(x)
        new_y = int(y)
        frac = new_x/new_y
                
        # If the fraction (frac) is less than or equal to 1 (i.e., the numerator is less than or equal to the 
        # denominator), the loop breaks, meaning the program will exit the loop.
        if frac <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

#ensuring to round to the nearest integer. using "round"
value = round(frac*100)
if value <= 0:
    print("E")
elif value>=99:
    print("F")
else:
    print(f"{value}%")

