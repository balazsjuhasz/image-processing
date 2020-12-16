import sys
import os
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]


def ConvertImages():
    if not os.path.exists(input_folder):
        print('Input path is not exists!')
        return False

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image in os.listdir(input_folder):
        img = Image.open(f'{input_folder}{image}')
        image_name = os.path.splitext(image)[0]
        img.save(f'{output_folder}{image_name}.png', 'png')

    print('Conversion complete')


if __name__ == "__main__":
    ConvertImages()
