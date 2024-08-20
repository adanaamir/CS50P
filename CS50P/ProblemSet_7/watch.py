import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    #checking this condition if the user provided input matches the following, if not then None will be returned
    if matches := re.search(r"^<iframe[^>]*src=\"(https?://(?:www\.)?youtube\.com/embed/(\w+))\"[^>]*></iframe>", s, re.IGNORECASE):
        #extracting group 1 (required for cs50 check)
        url = matches.group(1)
        video_id = matches.group(2)

        return f"https://youtu.be/{video_id}"
    
if __name__ == "__main__":
    main()

