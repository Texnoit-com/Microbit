from microbit import *

from Reed_Switch import Reed_Switch

switch = Reed_Switch(pin0)

while True:
    if switch.is_pressed():
        display.show(Image.YES)
        sleep(1000)
