import music
from microbit import *
from Passive_Buzzer import Passive_Buzzer

sound=Passive_Buzzer(pin0)
sound.play(music.BLUES)
sound.play_time(music.BIRTHDAY, 3000)