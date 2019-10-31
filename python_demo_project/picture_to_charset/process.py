from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type = int,default = 80)
parser.add_argument('--height',type = int,default = 80)
#get the parameter of the shell input
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    index = (alpha + 1)/length
    return ascii_char[int(gray/index)]

if __name__ == '__main__':
    img = Image.open(IMG)
    img = img.resize((WIDTH,HEIGHT),Image.NEAREST)
    output_txt = ''

    for i in range(HEIGHT):
        for j in range(WIDTH):
            output_txt += get_char(*img.getpixel((j,i)))
        output_txt += '\n'

    #output the txt string to output file
    if OUTPUT:
        with open(OUTPUT,'w') as outputFile:
            outputFile.write(output_txt)
    else:
        with open('output.txt','w') as outputFile:
            outputFile.write(output_txt)