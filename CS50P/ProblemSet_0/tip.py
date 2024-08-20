def main():
    #asking user input and then calling the fucntion
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #maths to figure out how much tip should be given
    tip = dollars*percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    #replacing $ sign with empty space bcz $ cannot be calculated
    d= d.replace("$", "")
    #returning the result as float
    return float(d)

def percent_to_float(p):
    p = float(p.replace("%", ""))
    #the reason why p was converted first: string cannot be divided by 100, so first convert string(p) to float then divide it by 100
    # dividing by 100 so it can be converted into percentage 
    return p/100
main()