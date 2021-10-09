import publish_tiktok
from time import localtime, ctime,time

    
while True:
    if int(localtime(time()).tm_sec) == 0:
        print(f"tiktok publishing at {ctime(time())}")
        publish_tiktok.publish_tiktok()