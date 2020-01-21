#/bin/python
from pyb import *

from tft import *

x = 0


fb.fill(0x000000)
fb.text("Hello Meowbit",25,60,0xFFFFFF)
tft.show(fb)
