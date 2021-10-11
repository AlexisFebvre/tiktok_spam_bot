import publish_tiktok
from time import localtime, ctime,time
from dynamic_text_size import create_image
from generate_video import *

def create_full_video():
    create_image()
    generate_video()
    add_effect_and_sound(define_song_path())

create_full_video()
    
#while True:
#    if int(localtime(time()).tm_sec) == 0:
#        print(f"tiktok publishing at {ctime(time())}")
#        publish_tiktok.publish_tiktok()