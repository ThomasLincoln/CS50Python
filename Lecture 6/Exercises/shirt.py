import os
import sys
from PIL import Image

tshirt = sys.argv[1]
after = sys.argv[2]
def verify_file():
    tamanho = len(sys.argv)
    try: 
        extensao1 = os.path.splitext(tshirt)[1]
        extensao2 = os.path.splitext(after)[1]
        
        if extensao1 != '.jpg' and extensao1 != ".png" and extensao1 != ".jpeg":
            print("Invalid input")
            sys.exit()
        if extensao2 != '.jpg' and extensao2 != ".png" and extensao2 != ".jpeg":
            print("Invalid input")
            sys.exit()
        if tamanho > 3:
            print("Too many command-line arguments")
            sys.exit()
        if extensao1 != extensao2:
            print("Input and output have different extensions")
            sys.exit()
    except:
        if tamanho < 3:
            print("Too few command-line arguments ")
            sys.exit()

verify_file()

def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage

def convert():
    after = sys.argv[2]
    tshirt = sys.argv[1]
    im = Image.open(tshirt)    
    juju = Image.open(after)

    im = im.convert("RGBA")
    juju = juju.convert("RGBA")

    juju = changeImageSize(im.size[0], im.size[1], juju)

    w = im.size[0] + juju.size[0]
    h = max(im.size[1], juju.size[1])

    alphaComposited = Image.alpha_composite(im, juju)
    alphaComposited.save("merged_image.png")  


convert()