from time import gmtime, strftime
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (800,400)
camera.hflip = True
camera.start_preview()

output = strftime('myPice.jpeg',gmtime())
  