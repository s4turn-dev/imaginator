from PIL import Image
from math import floor
from time import sleep
import sys

ABC = '`+*/lOZH8@'[::]
TERMINAL_SIZE = []

def pixels_to_ascii(pixel_array: tuple) -> str:
    result = ''
    for pixel in pixel_array:
        avrg = floor((pixel[0] + pixel[1] + pixel[2]) / 3)
        brightness = avrg // 25
        char = ABC[0 if brightness == 0 else brightness - 1]
        result += char
    return result


def image_to_ascii(gif):
    img = gif.resize(TERMINAL_SIZE)
    data = list(img.getdata())
    if type(data[0]) is tuple:
        print(pixels_to_ascii(data))


sys.argv += [''] * (2 - len(sys.argv[3:]))

TERMINAL_SIZE = int(sys.argv[1]), int(sys.argv[2])
filename = sys.argv[3] or input('Filename: ')
try: delay = float(sys.argv[4])
except ValueError: delay = 0.1

try:
    IMG = Image.open(filename)
except FileNotFoundError:
    print(f'No such file: {filename}')
else:
    if filename.split('.')[-1] == 'gif': 
        while True:
            try:
                for frame in range(IMG.n_frames): 
                    IMG.seek(frame)
                    image_to_ascii(IMG)
                    sleep(delay)
            except KeyboardInterrupt:
                break
    else:
        image_to_ascii(IMG)
finally:
    IMG.close()
