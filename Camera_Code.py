
from picamera import PiCamera
from time import sleep

# Create a PiCamera object
camera = PiCamera()

# Capture an image
camera.capture('example_image.jpg')

# Optionally, preview the image for a few seconds
camera.start_preview()
sleep(5)
camera.stop_preview()

