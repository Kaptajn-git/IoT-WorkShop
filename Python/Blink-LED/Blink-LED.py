from machine import Pin
import time

pin_led = Pin(2, mode=Pin.OUT)

while True:

    pin_led.on()
    time.sleep(1)
    pin_led.off()
    time.sleep(1)
