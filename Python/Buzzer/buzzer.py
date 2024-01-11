from machine import Pin, PWM
import time

# Buzzer +pin to NodeMCU pin D5
#        -pin to GND
#
# https://pages.mtu.edu/~suits/notefreqs.html
#

tempo = 2
tones = {
# Play middle C scale
    'c': 261, # C4
    'd': 294, # D4
    'e': 330, # E4
    'f': 349, # F4
    'g': 392, # G4
    'a': 440, # A4
    'b': 494, # B4
    'C': 523, # C5
    ' ': 0,   # Reset and Shut up!
# Play high C scale
#    'c': 523, # C5
#    'd': 587, # D5
#    'e': 659, # E5
#    'f': 698, # F5
#    'g': 784, # G5
#    'a': 880, # A5
#    'b': 988, # B5
#    'C': 1046, # C6 Note not possible on ESP8266 since max PWM is 1023
#    ' ': 0,   # Reset and Shut up!
}

beeper = PWM(Pin(14, Pin.OUT), freq=440, duty=512)
melody = 'cdefgabC'
rhythm = [8, 8, 8, 8, 8, 8, 8, 8]

for tone, length in zip(melody, rhythm):
    beeper.freq(tones[tone])
    time.sleep(tempo/length)
beeper.deinit()
