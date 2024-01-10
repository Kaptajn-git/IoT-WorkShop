# fancy-RGB.py
import machine, neopixel
import time
n = 8 # Number of neopixels
p = 4 # GPIO4 (NodeMCU pin D2)
np = neopixel.NeoPixel(machine.Pin(p), n) # Set Neopixel-mode on GPIO4

# Run with rgbdemo(np)

def rgbdemo(np):
    n = np.n

    # cycle red
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 0, 0)
        np.write()
        time.sleep_ms(50)

    # cycle green
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (0, 255, 0)
        np.write()
        time.sleep_ms(50)

    # cycle blue
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (0, 0, 255)
        np.write()
        time.sleep_ms(50)

    # bounce red
    for i in range(4 * n):
        for j in range(n):
            np[j] = (64, 0, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(100)

    # bounce green
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 64, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(100)

    # bounce blue
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 64)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(100)

    # fade in/out
    for i in range(0, 10 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, val, val)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()