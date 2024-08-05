import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #searching for this format in the users input
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        ip =  matches.groups()

        #iterating over each number and then checking if the num is in the specified range
        for part in ip:
            if not 0 <= int(part) <= 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()