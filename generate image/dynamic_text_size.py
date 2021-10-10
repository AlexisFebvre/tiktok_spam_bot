from PIL import Image, ImageDraw, ImageFont
from generate_text import do_sentence


#########################################
#   Maximum text with font to 100:      #
#       21 chars                        #
#       = 1034 px                       #
#########################################
 

# image settings
img_size = (1080, 1920)
img_color = (76, 76, 76)

# text settings
font_size = 100
# text = do_sentence()
text = do_sentence()
text_color = (255, 255, 255)
font = ImageFont.truetype("assets/font/SunDeep.otf", font_size, encoding="UTF-8")
print(do_sentence())

if font.getsize(text)[0] > 1034:
    font_size = int(1034 / (len(text)/2))
    font = ImageFont.truetype("assets/font/Bella Safira.otf", font_size)
    print(f"{font.getsize(text)[0]} px\n{len(text)} chars")

text_xy = (int((img_size[0]/2) - (font.getsize(text)[0]) / 2), int((img_size[1]/2) - font.getsize(text)[1]) / 1.25)


# create image and set it drawable
img = Image.new('RGB', img_size, img_color)
draw = ImageDraw.Draw(img)

# draw the text on the image
draw.text(text_xy, text, text_color, font=font)

# save the image
img.save("image.jpg")