from pynput.mouse import Controller, Button
from time import sleep

mouse = Controller()

def get_mouse_position(element):
    input(f"wait for input to locate {element}")
    print(f"you have 3 seconds to reach {element}")
    sleep(3)
    pos = mouse.position
    print(f"{element} is at {pos}")
    with open("location.txt", "a") as file:
        file.write(f"{element} is at : {pos}\n")
        sleep(0.5)

element_to_get = ["new video", "select file button", "file path", "select file", "confirm file", "legende", "publish", "view profil"]

for element in element_to_get:
    get_mouse_position(element=element)