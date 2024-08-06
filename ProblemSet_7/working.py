import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^(\d{1,2})(?::(\d{2}))? ([A-Z]+) to (\d{1,2})(?::(\d{2}))? ([A-Z]+)$", s):

        #extracting the time
        # "or 0" make sures that if this part of code is not provided then none or 0 is returned
        start_hours = int(matches.group(1))
        start_minutes = int(matches.group(2) or 0)
        end_hours = int(matches.group(4))
        end_minutes = int(matches.group(5) or 0)
        str_1 = matches.group(3)
        str_2 = matches.group(6)

        #converting 12hour format to 24 hour format
        if str_1 == "PM" and start_hours !=12:
            start_hours += 12
        if str_1 == "AM" and start_hours == 12:
            start_hours = 0

        if str_2 == "PM" and end_hours !=12:
            end_hours += 12
        if str_2 == "AM" and end_hours == 12:
            end_hours = 0

        #time condition
        if not (0 <= start_hours < 24 and 0 <= end_hours < 24):
            raise ValueError
            
        if not (0 <= start_minutes < 60 and 0 <= end_minutes < 60):
            raise ValueError
            
        return f"{start_hours:02}:{start_minutes:02} to {end_hours:02}:{end_minutes:02}"
        
    else:
        raise ValueError

if __name__ == "__main__":
    main()