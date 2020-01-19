#/bin/python
from pyb import *

from time import sleep

x = 0
led1 = LED(1)
led2 = LED(2)



while True:
  led1.on()
  sleep(1)
  led1.off()
  sleep(1)
