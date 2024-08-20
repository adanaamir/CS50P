import sys, csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

firstfile = sys.argv[1]
secondfile = sys.argv[2]

try:
    #read this csv as first input file
    with open(firstfile) as b_file:
        
        #using DictReader to handle headers
        reader = csv.DictReader(b_file)

        #new csv file to write as output
        with open(secondfile, "w", newline='') as a_file:

            #writing names of headers
            fieldnames = ["first", "last", "house"]

            writer = csv.DictWriter(a_file, fieldnames=fieldnames)

            #  if you've defined the fieldnames in csv.DictWriter line, you just need to 
            # put writer.writeheader() to put them into the csv file
            writer.writeheader()

            #iterating over each row of the firstfile and then splitting the names (of row) into first and last 
            for row in reader:
                last, first = row["name"].split(",")

                #writing the rows to the second csv file (writing unser the filenames)
                writer.writerow({"last": last.strip(), "first": first.strip(), "house": row["house"].strip()})

except FileNotFoundError:
    sys.exit(f"Could not read {firstfile}")