from machine import Pin, PWM
import time

# Buzzer +pin to NodeMCU pin D5
#        -pin to GND
#
# https://pages.mtu.edu/~suits/notefreqs.html

tempo = 2
tones = {

    'c': 131, # C3
    'd': 147, # D3
    'e': 165, # E3
    'f': 175, # F3
    'g': 196, # G3
    'a': 220, # A3
    'b': 247, # B3
    'C': 262, # C4
    'D': 294, # D4
    'E': 330, # E4
    'F': 349, # F4
    'G': 392, # G4
    'A': 440, # A4
    'B': 494, # B4
    '1': 523, # C5
    '2': 587, # D5
    '3': 659, # E5
    '4': 698, # F5
    '5': 784, # G5
    '6': 880, # A5
    '7': 988, # B5
#    '8': 1046, # C6 Note not possible on ESP8266 since max PWM is 1023
    ' ': 0,   # Shut up!
}

beeper = PWM(Pin(14, Pin.OUT), freq=440, duty=512)
melody = 'cdefgabCDEFGAB1234567'
rhythm = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

for tone, length in zip(melody, rhythm):
    beeper.freq(tones[tone])
    time.sleep(tempo/length)
beeper.deinit()
