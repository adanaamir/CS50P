def main():
    #asking user for input
    n = input("Enter anything: ")
    #passing n(user input) to convert function so the user input can be converted and then storing it to a new variable "message" so that it is easy to print
    message = convert(n)
    #printing message
    print(message)

#passing the user input to th convert function
def convert(n):
    n = n.replace(":)", "🙂")
    n = n.replace(":(", "🙁")
    #returning value of n so that it can be used in the above function
    return n
    
main()
    