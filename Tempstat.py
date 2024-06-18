# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/temperature-2022-06-26-18-00-07.py"

from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.temp
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)

