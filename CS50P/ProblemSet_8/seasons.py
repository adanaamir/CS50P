from datetime import date
import sys, inflect

def main():
    #format YYY/MM/DD
    try:
        birthday = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid Input")

    today = date.today()
    p = inflect.engine()

    total = int(time(today, birthday))
    str_word = p.number_to_words(total).capitalize()

    ttl_min = str_word.replace("and", "").replace("thous", "thousand").replace("  ", " ")

    print(f"{ttl_min} minutes")

def time(today, birthday):
    #subtracting todays date from the date entered
    total_time = today - birthday
    total_minutes = total_time.days * 24 * 60
     #returns a timedelta object, which cannot be a tuple
    return total_minutes

if __name__ == "__main__":
    main()
