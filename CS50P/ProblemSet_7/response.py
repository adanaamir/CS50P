from validator_collection import checkers

text = input("Whats your email address? ")

#taking email as an argument bcz we are checking for email
def valid_email(email):
    #checker function checks whether the input is valid
    return checkers.is_email(email)

if valid_email(text):
    print("Valid")
else:
    print("Invalid")
