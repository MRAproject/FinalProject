from picamera import PiCamera
from time import gmtime,strftime,sleep

camera = PiCamera()
camera.start_preview()

for i in range(6):    
    output = strftime('Camera samples/image-%d-%m %H:%M %S.jpeg',gmtime())
    camera.capture(output)

camera.stop_preview()
exit()