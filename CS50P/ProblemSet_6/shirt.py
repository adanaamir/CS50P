import sys
from os.path import splitext
from PIL import Image, ImageOps

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

firstfile =  sys.argv[1]
secondfile = sys.argv[2]

#means we're splitting out text when we have a dot, [1] means that we are accessing the second element of the pair ie after the dot
file_1 = splitext(firstfile)[1].lower()
file_2 = splitext(secondfile)[1].lower()

if not (firstfile.endswith(".jpg") or firstfile.endswith(".jpg") or firstfile.endswith(".png")):
    sys.exit("Invalid output")

if not (secondfile.endswith(".jpg") or secondfile.endswith(".jpeg") or secondfile.endswith(".png")):
    sys.exit("Invalid output")

if file_1 != file_2:
    sys.exit("Input and output have different extensions")

#trying to open the firstfile(if it exists)
try: 
    muppet_file = Image.open(firstfile)
except FileNotFoundError:
    sys.exit("Input does not exist")

#opening the shirt image
shirt_overlay = Image.open("shirt.png")
    
#getting the size of the shirt
size = shirt_overlay.size

#resizing muppet to fit the shirt
muppet = ImageOps.fit(muppet_file,size)

#psting the muppet on the shirt, the second one masks the rgbs/tranparencies used
muppet.paste(shirt_overlay, shirt_overlay)

#the second arg that we will provide will be the file in which we will be saving
muppet.save(secondfile)