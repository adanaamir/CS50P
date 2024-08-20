# months_names = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# while True:
#     #case 1 when entered format is MM/DD/YYYY
#     try:
#         date = input("Date: ")
#         #splitting the entered date 
#         month,day,year = date.split("/")
#         month = int(month)
#         day = int(day)
#         year=int(year)
#         #now the cond where no month is great than 31 days and there are 12 months
#         if (1 <= day <= 31) and (1 <= month <=12):
#             break

#     #second condition
#     except:
#         try:
#             #entered in the format: September 21, 1998
#             month, day, year = date.split(" ")

#             #checking cond, if the entered day is not ending with "," then contine ie reprompt
#             if not day.endswith(","):
#                 continue
#             #splitting the day and taking the first one[0] ie the date entered
#             #either splitting way OR day = day.split(",")[0]
#             day = day.replace("," , "")
#             day=int(day)
#             year=int(year)
#             #printed form: YYYY/MM/DD
#             #since the entered month will be in strings we have to convert it into numbers, so we caniterate throught
#             #our list and compare its len
#             for i in range(len(months_names)):
#                 if month == months_names[i]:
#                     month = i+1
#             #OR an easier way is to use index but for this, with except u need to write "ValueError" bcz index raises a valerror
#             # month_num = months_names.index(month)+1

#             if (1 <= int(day) <= 31) and (1 <= int(month) <=12):
#                 break

#         except:
#             print()
#             pass

# #here i need to convert month and day in int,they are still strings bcz when i put :02 it adds 0 to it so convert in int
# print(f"{year}-{int(month):02}-{int(day):02}")

                               # A PRETTIER VERSION:

months_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    #case 1 MM/DD/YYYY
    try:
        date = input("Date: ")
         
        month,day,year = date.split("/")
        month = int(month)
        day = int(day)
        year=int(year)

        if (1 <= day <= 31) and (1 <= month <=12):
            break

    #case 2 Month Day, Year
    except ValueError:
        try:
            month, day, year = date.split(" ")

            #checking cond, if the entered day is not ending with "," then contine ie reprompt
            if not day.endswith(","):
                continue

            day = day.replace("," , "")
            day=int(day)
            year=int(year)
            month = months_names.index(month) +1

            if (1 <= int(day) <= 31) and (1 <= int(month) <=12):
                break

        except (ValueError, IndexError):
            pass

print(f"{year}-{month:02}-{day:02}")

