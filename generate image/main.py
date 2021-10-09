from time import sleep
from PIL import Image, ImageDraw, ImageFont


def change_image(text_input):


    # image settings
    img_size = (1080, 1920)
    img_color = (76, 76, 76)

    # text settings
    text = text_input
    text_color = (255, 255, 255)
    font = ImageFont.truetype("assets/font/Bella Safira.otf", 100)
    text_xy = (int((img_size[0]/2) - (font.getsize(text)[0]) / 2), int((img_size[1]/2) - font.getsize(text)[1]) / 1.25)
    print(f"{font.getsize(text)[0]} px")
    print(f"{len(text)} chars\n")

    # create image and set it drawable
    img = Image.new('RGB', img_size, img_color)
    draw = ImageDraw.Draw(img)

    # draw the text on the image
    draw.text(text_xy, text, text_color, font=font)

    # save the image
    img.save("image.jpg")

while True:
    a = input("enter chars\n")
    sleep(1)
    change_image(a)