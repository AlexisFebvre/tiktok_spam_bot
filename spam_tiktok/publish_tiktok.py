from time import sleep
import pynput.mouse as m
import pynput.keyboard as k
from random import uniform

mouse = m.Controller()
keyboard = k.Controller()


def click(pos):
    mouse.position = pos
    mouse.press(m.Button.left)
    mouse.release(m.Button.left)

def type_text(text):
    keyboard.type(text)


# order :
#   new video
#   select file btn
#   file path
#   select file
#   confirm file
#   legend
#   publish
#   view profile

positions = [(1075, 108), (476, 434), (442, 50), (238, 168), (582, 443), (653, 322), (1118, 757), (784, 525)]
to_type = ["", "", "C:/Users/Alexis/Desktop/spam_tiktok/video", "", "", "a new video #fyp #spam_bot", "", ""]
    
def publish_tiktok():
    for i in range(len(positions)):
        click(positions[i])
        sleep(uniform(2.5, 3.6))      
        type_text(to_type[i])