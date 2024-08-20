import sys

#creating an empty list to which i can save all the lines(rows)
rows = []

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

else:
    try:
        #a read file so that we can iterate over the rows and see how many lines are there
            with open(filename) as file:
                for line in file:
                    linestrip = line.strip()
                    #in the filechecking if any line does not start with # and when the extra whitespace has been removed then add the line to the list
                    if not linestrip.startswith("#") and linestrip:
                        rows.append(linestrip)
                        #then print out the total lines of code excluding the comments and empty lines
    except FileNotFoundError:
        #if an error filenotfound is raised , then contine
        sys.exit("file does not exist")

print(len(rows))