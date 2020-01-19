#/bin/python
from pyb import *
from time import sleep

x = 0
flag = 0
led1 = LED(1)
led2 = LED(2)

def onBtnRIGHTPressed(evt):
  global x,flag
  x += 10

ExtInt(Pin('RIGHT'), ExtInt.IRQ_FALLING, Pin.PULL_UP, onBtnRIGHTPressed) 

def onBtnLEFTPressed(evt):
  global x,flag
  x += -20

ExtInt(Pin('LEFT'), ExtInt.IRQ_FALLING, Pin.PULL_UP, onBtnLEFTPressed) 

def onBtnBTNAPressed(evt):
  global x,flag
  # LED aus
  flag = 0

ExtInt(Pin('BTNA'), ExtInt.IRQ_FALLING, Pin.PULL_UP, onBtnBTNAPressed) 

def onBtnBTNBPressed(evt):
  global x,flag
  # LED an
  flag = 1

ExtInt(Pin('BTNB'), ExtInt.IRQ_FALLING, Pin.PULL_UP, onBtnBTNBPressed) 

flag = 1
x = 100
while True:
  if flag == 0:
    led1.off()
  else:
    if flag == 1:
      led1.intensity(x)
      sleep(0.1)
