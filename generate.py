#generates a image with a random text 
#and a random background

import os
import random
import sys
from PIL import Image, ImageDraw, ImageFont

#generate random word
def randomword(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(length))

#generate random background color
def randomcolor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

#generate random text color
def randomtextcolor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

#set working directory to desktop
os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop'))

#generate image with variation of text location
def generateimagevariation(word):
    img = Image.new('RGB', (300,50), color=randomcolor())
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts/arial.ttf'), size=40)
    draw.text((random.randint(0,50),random.randint(0,50)), word, font=font, fill=randomtextcolor())
    return img
    #save image
    img.save(namefile(word))



#name file with the word and background color
def namefile(word):
    return word + '.jpg'


