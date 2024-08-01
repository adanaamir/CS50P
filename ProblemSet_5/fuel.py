def main():
    while True:
        try:
            text = input("Fraction: ")
            frac = convert(text)
            perc = gauge(frac)
            print(perc)
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid")

def convert(fraction):       
    x,y = fraction.split("/")
    new_x = int(x)
    new_y = int(y)

    if new_y == 0:
        raise ZeroDivisionError
    
    percentage = new_x/new_y
           
    if percentage <= 1:
        return percentage
    else:
        raise ValueError

def gauge(percentage):
    value = round(percentage * 100)
    if value <= 1:
        return "E"
    elif value >= 99:
        return "F"
    else:
        return (f"{value}%")

if __name__ == "__main__":
        main()