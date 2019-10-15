from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw

x = input("Please enter in a x coordinate: ")
y = input("Please enter in a y coordinate: ")
obj = input("Select which object do you want displayed: 1 or 2? ")
    
f1 =  [
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,0],
    [1,0,1,1,1,1,0,1],
    [1,0,0,1,1,0,0,1],
    [1,0,0,1,1,0,0,1],
    [0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0] ]

pm = [[0,0,0,1,1,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,0,1,1,1,1,1,1,1,0,0],
    [0,0,0,1,1,1,1,1,0,0,0] ]


if obj == "1":
    obj = f1
elif obj == "2":
    obj = pm

def displayObject(obj,x,y):
    x1 = int(x)
    y1 = int(y)
    for i in obj:
        x += 1
        for j in i:
            pix = int(j)
            lcd.set_pixel(x1, y1, pix) 
            y += 1        
    lcd.show()

displayObject(obj,x,y)

