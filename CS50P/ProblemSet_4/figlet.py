from pyfiglet import Figlet
import sys
import random

#creating a figlet object
figlet = Figlet()
av_font = figlet.getFonts()

#if no font is provided by the user then suffle the available fonts and pick any random(first in thsi case) and display the text in that font
if len(sys.argv) == 1:
    random.shuffle(av_font)
    rand_font = av_font[0]
    figlet.setFont(font = rand_font)

#if the font is provided but the font is incorrect then display an error message
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
        
    #else set the entered font 
    else:
        #set the specified font
        font_name = sys.argv[2]
        if font_name not in av_font:
            sys.exit("Invalid Usage")

        figlet.setFont(font = font_name)
else:
    sys.exit("invalid usage")

#program first verifies the command line arguments if there are any error messages it exits if not any, then it asks for input
text = input("Input: ")

#and then in the end the text is rendered and printed to the console
rendered_text = figlet.renderText(text)
print(rendered_text)


