from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
import click 

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

def getKeystroke(x,y):
    key = input(click.getchar())
    if key == '\x1b[A':
        h = y - 1
        lcd.set_pixel(x, h, 1)
        lcd.show()
    elif key == '\x1b[B':
        h = y + 1
        lcd.set_pixel(x, h, 1)
        lcd.show()
    elif key == '\x1b[C':
        w = x - 1
        lcd.set_pixel(w, y, 1)
        lcd.show()
    elif key == '\x1b[D':
        w = x + 1
        lcd.set_pixel(w, y, 1)
        lcd.show()
    elif key == "s":
        clearScreen(lcd) 
    elif key == "q":
        quit

def getWrap(lcd):
    if x > 127:
        x = 0
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif x < 0:
        x = 127
        lcd.set_pixel(x,y,1)
        lcd.show()

    if y > 63:
        y = 0
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif y < 0:
        y = 63
        lcd.set_pixel(x,y,1)
        lcd.show()
    
