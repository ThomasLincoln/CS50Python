from PIL import ImageOps, Image
import os
import sys

def main():
    entrada, saida = get_nomes(sys.argv)
    verificacao(entrada, saida)

    try:
        shirt = Image.open('shirt.png')
        muppet = Image.open(entrada)
    except FileNotFoundError:
        sys.exit('Input does not exist')
    size = shirt.size
    muppet = ImageOps.fit(muppet, size)
    muppet.paste(shirt, shirt)
    muppet.save(saida)

def get_nomes(arguments):
    if len(arguments) != 3:
        if len(arguments) < 3:
            sys.exit('Too few command-line arguments')
        else:
            sys.exit('Too mant command-line arguments')
    return [sys.argv[1],sys.argv[2]]

def verificacao(entrada, saida):
    origem_root, origem_ext = os.path.splitext(entrada)
    fora_root, fora_ext = os.path.splitext(saida)

    if origem_ext.lower() != fora_ext.lower():
        sys.exit('Input and output have different extensions')

    if origem_ext.lower() == '.jpg' or origem_ext.lower() == '.jpeg' or origem_ext.lower() == '.png':
        pass
    else:
        sys.exit('Invalid input')

    if fora_ext.lower() == '.jpg' or fora_ext.lower() == '.jpeg' or fora_ext.lower() == '.png':
        pass
    else:
        sys.exit('Invalid output')

if __name__ == '__main__':
    main()