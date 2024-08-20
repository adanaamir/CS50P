file = input("File name: ")
new_file = file.lower().strip()
if ".gif" in new_file:
    print("image/gif")
elif ".png" in new_file:
    print("image/png")
elif ".jpg" in new_file:
    print("image/jpeg")
elif ".jpeg" in new_file:
    print("image/jpeg")
elif ".pdf" in new_file:
    print("application/pdf")
elif ".zip" in new_file:
    print("application/zip")
elif ".txt" in new_file:
    print("text/plain")
else:
    print("application/octet-stream")
