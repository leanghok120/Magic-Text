# Made by Astrox/Leanghok
from pyfiglet import figlet_format


print("This python program will convert your text to Ascii arts")
print(
    """          Note
----------------------------
Type q to quit the program\n"""
)
text = None
ascii_font = input(
    "Enter a font for your ascii art.\nslant, standard, 5lineoblique, doh, digital, alligator, letters\n--> "
)

while not text == "q":
    text = input("Type somthing: ")
    ascii_string = figlet_format(text, font=ascii_font.lower())
    print(ascii_string)
print("\nGoodbye! Thanks for using this program.")
