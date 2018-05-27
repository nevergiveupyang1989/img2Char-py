#--*-- coding:utf-8 ---*--
import os
from PIL import Image as image

acsii_char = list("$@B%8&WM#*oahkbdpqwmZOABCDEFGHIOPUVW0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def process(img_path,delta=100):
    img = image.open(img_path)

    width,height = img.size
    
    if width > height:
        maxSize = width
    else:
        maxSize = height

    scale = maxSize / delta
    width,height = int(width/scale), int(height/scale)
    
    img = img.resize((width,height))
    
    return img

def rgb2Char(r,g,b, alpha = 256): 
    if alpha == 0:
        return ''
    
    length = len(acsii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0+1)/length

    return acsii_char[int(gray/unit)]

def img2Char(img, savePath):
    txt = ''
    width, height = img.size
    
    for i in xrange(height):
        line = ''
        for j in xrange(width):
            line += rgb2Char(*img.getpixel((j,i)))
        txt = txt + line + '\n'
    
    with open(savePath, 'w') as f:
        f.write(txt)

if __name__ == '__main__':
    img_path = os.path.join(os.getcwd(), 'test3.jpg')
    save_path = os.path.join(os.getcwd(), 'test3.txt')
    img = process(img_path)
    img2Char(img,save_path)
