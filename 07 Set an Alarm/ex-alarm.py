import time
import os

def set_alarm(sound, message,t = time.time()+1):
    os.system(sound)
    return print(message)

if __name__ == '__main__':
    sound = 'afplay /System/Library/Sounds/Sosumi.aiff'
    set_alarm( sound, 'wake up!')
    