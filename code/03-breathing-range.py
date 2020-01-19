#/bin/python
from pyb import *
from time import sleep

led1 = LED(1)

while True:
  for i in range(50):
    led1.intensity(i)
    sleep(0.05)
  for i in range(50):
    led1.intensity(50 - i)
    sleep(0.05)
