from picamera import PiCamera
from time import gmtime,strftime,sleep
import datetime
import NimageProcessing

camera = PiCamera()
for i in range(3):    
    output = strftime('Camera samples/image-'+str(i)+'.jpeg')
    camera.capture(output)

NimageProcessing.Work()
exit()

