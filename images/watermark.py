# attribution to https://github.com/theitrain/watermark/blob/master/watermark.py

import os

from PIL import Image

EXTS = ('.jpg', '.png')


def addWatermark(filename, lgo, pos='bottomright'):
    logo = Image.open(lgo)
    logoWidth = logo.width
    logoHeight = logo.height

    for filename in os.listdir(path):
        if any([filename.lower().endswith(ext) for ext in EXTS]) and filename != lgo:
            image = Image.open(path + '/' + filename)
            imageWidth = image.width
            imageHeight = image.height

            try:
                if pos == 'topleft':
                    image.paste(logo, (0, 0), logo)
                elif pos == 'topright':
                    image.paste(logo, (imageWidth - logoWidth, 0), logo)
                elif pos == 'bottomleft':
                    image.paste(logo, (0, imageHeight - logoHeight), logo)
                elif pos == 'bottomright':
                    image.paste(logo, (imageWidth - logoWidth,
                                       imageHeight - logoHeight), logo)
                elif pos == 'center':
                    image.paste(logo, ((imageWidth - logoWidth)/2,
                                       (imageHeight - logoHeight)/2), logo)
                else:
                    print('Error: ' + pos + ' is not a valid position')
                    print(
                        'Adding watermark')

                image.save(path + '/' + filename)
                print('Added watermark to ' + filename)

            except:
                image.paste(logo, ((imageWidth - logoWidth)/2,
                                   (imageHeight - logoHeight)/2), logo)
                image.save(path + '/' + filename)
                print('Added default watermark')
