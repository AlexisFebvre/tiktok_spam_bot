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

def enter_path():
    type_text("C:/Users/Alexis/Desktop/tiktok_spam_bot/spam_tiktok/video")
    keyboard.press(k.Key.enter)
    keyboard.release(k.Key.enter)

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
to_type = ["", "", "path", "", "", "a new video #fyp #spam_bot", "end", ""]
    
def publish_tiktok():
    for i in range(len(positions)):
        click(positions[i])
        sleep(uniform(2.5, 3.6))      
        if to_type[i] == "path" :
            enter_path()
        elif to_type[i] == "end":
            sleep(5)
        else:
            type_text(to_type[i])


publish_tiktok()