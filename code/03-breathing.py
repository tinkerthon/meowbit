#/bin/python
from pyb import *

from time import sleep

x = 0
brightness = 100
led1 = LED(1)
led2 = LED(2)



brightness = 0
while True:
  for count in range(50):
    led1.intensity(brightness)
    brightness += 1
    sleep(0.05)
  for count in range(50):
    led1.intensity(brightness)
    brightness += -1
    sleep(0.05)
