from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
import click 

text = "Etch a Sketch"
x = 30
y = 30
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
    x = (width - w) // 2
    y = (height - h) // 2
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

def getKeystroke(x,y,lcd):
    
    c = click.getchar()
    if c == 's':
        clearScreen(lcd) 
    elif c == 'q':
        exit()
    elif c == '\x1b[A':
        y - 1
        lcd.set_pixel(x, y, 1)
        lcd.show()
        
    elif c == '\x1b[B':
        y + 1
        lcd.set_pixel(x, y, 1)
        lcd.show()
        
    elif c == '\x1b[C':
        x + 1
        lcd.set_pixel(x, y, 1)
        lcd.show()
        
    elif c == '\x1b"[D"':
        x - 1
        lcd.set_pixel(x, y, 1)
        lcd.show()
       


    

def getWrap(x,y):
    if x > 127:
        x = 0
        return x
    elif x < 0:
        x = 127
        return x 
    else:
        return x

    if y > 63:
        y = 0
        return y
    elif y < 0:
        y = 63
        return y
    else:
        return y


displayText(text,lcd,x,y)

while True:
    getKeystroke(x,y,lcd)



