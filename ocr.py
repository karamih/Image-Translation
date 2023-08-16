import cv2
import numpy as np
import easyocr
from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
from tranlation import translation_chain


reader = easyocr.Reader(lang_list=['en'], gpu=False)


def ocr(path, file_name, font_size=40, color=(0, 0, 0, 0)):
    font = ImageFont.truetype("Ubuntu-Arabic_B.ttf", font_size)

    img = cv2.imread(path)

    contents = reader.readtext(img, paragraph=True)

    pil_image = Image.fromarray(img)
    draw = ImageDraw.Draw(pil_image)

    for content in contents:
        coordinates, txt = content

        txt = translation_chain.run(txt)
        txt = arabic_reshaper.reshape(txt)
        txt = get_display(txt)

        draw.text((coordinates[0][0], coordinates[0][1]), txt, fill=color, font=font)

    img = np.array(pil_image)

    cv2.imwrite(f'statics/{file_name}', img)


ocr("statics/ocr2.jpg","output_ocr2.jpg", font_size=120, color=(0, 0, 255, 0))