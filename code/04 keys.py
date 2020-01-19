from pyb import *

led1 = LED(1)

def on_btn_up_pressed(evt):
    led1.on()

ExtInt(Pin('UP'), ExtInt.IRQ_FALLING, Pin.PULL_UP, on_btn_up_pressed)

def on_btn_down_pressed(evt):
    led1.off()

ExtInt(Pin('DOWN'), ExtInt.IRQ_FALLING, Pin.PULL_UP, on_btn_down_pressed)
