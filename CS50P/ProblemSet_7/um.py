import re

def main():
    print(count(input("Text: ")))


def count(s):
    # \b means to check that specific character/word, it acts like a boundary
    match =  re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(match)

if __name__ == "__main__":
    main()