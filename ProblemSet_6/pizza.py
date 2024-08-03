from tabulate import tabulate
import sys
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

#an empty lst to which we will add the data
table = []

try:
    with open(filename) as file:
        reader = csv.reader(file)
        #next(reader) reads the heading of the file entered(reads the first line of csv file which is assumed to be the heading)
        headers = next(reader)
        #while row for row in reader reads the remaining data in the file ie iterating over each row 
        #not appending headers as it is already included, so appending it would result in repetition
        for row in reader:
            table.append(row)
         
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table, headers,  tablefmt="grid"))