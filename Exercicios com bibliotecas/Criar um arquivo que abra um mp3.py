from pygame import *

mixer.init()
mixer.music.load('Kalimba.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)