from machine import Pin
from time import sleep

# Pir-sensor.py
motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

led = Pin(2, Pin.OUT) # NodeMCU buildin LED
pir = Pin(13, Pin.IN) # GPIO13 NodeMCU pin D7

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected! Interrupt caused by:', interrupt_pin)
    led.value(0)
    sleep(5)
    led.value(1)
    print('Motion stopped!')
    motion = False
    
