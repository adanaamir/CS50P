def main():
    ans = input("What time is it? ")
    #passing ans to convert func in order to be converted in string
    time = convert(ans)
    if time >=7 and time <=8:
        print("breakfast time")
    elif time>= 12 and time <=13:
        print("lunch time")
    elif time >=18 and time<=19:
        print("dinner time")

def convert(time):
    #splitting hours and minutes
    hours, minutes = time.split(":")
    #converting time to float
    new_min = float(minutes) / 60
    return float(hours) + new_min

#The main guard ensures the script runs correctly when executed directly.
if __name__ == "__main__":
    main()
