# Main script
from dictionary import *


def write_text(text):
    center = (1, 1.5)
    padding = 0.5
    for i in text:
        if i in dictionary.keys():
            symb = dictionary[i].copy()
            print(str(symb.move(center[0], center[1])))
            center = (center[0] + LETTER_WIDTH + padding, center[1])


text = input('Enter a text\n')
write_text(text)