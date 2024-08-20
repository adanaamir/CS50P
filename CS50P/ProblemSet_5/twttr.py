def main():
    word = input("input: ")
    print("Output:", shorten(word))


def shorten(word):
    result=""
    for vowel in word:
        if vowel.lower() not in ["a", "e", "i", "o", "u"]:
            result+=vowel
    return result


if __name__ == "__main__":
    main()