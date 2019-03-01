from picamera import PiCamera
from time import gmtime,strftime,sleep
import datetime
import NimageProcessing
import delete
import threading
from threading import Timer
import requests
from pprint import pprint

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def SetLedRed():
    print('Led red are show...')

def SetLedGreen():
    print('Led green are show...')
   
SetLedRed()
camera = PiCamera()
FOLDER = 'Camera samples/'

def Work():
    print('Take 3 pic..')
    for i in range(3):    
        output = strftime(FOLDER+'image-'+str(i)+'.jpeg')
        camera.capture(output)
    
    print('Processing images..')
    carNumber = NimageProcessing.Work(FOLDER)
    if(carNumber != None):
        rt.stop()
        data = {"carNumber": carNumber}
        print('car number:' + carNumber)
        backendResponse = requests.get("http://10.100.102.15:3001/check_car", params=data)
        print(backendResponse)
        if(backendResponse.status_code == requests.codes.ok):            
            if((backendResponse.json()['status']) == 1):
                SetLedGreen()
        else:
            print('Car Number: '+ carNumber+' are not allowed!')
        rt.start()
    
print('Starting...')
rt = RepeatedTimer(17, Work) # it auto-starts, no need of rt.start()
try:
    sleep(1000000) # your long-running job goes here...
finally:
    rt.stop()


    
#pprint(backendResponse.json())
#pprint(backendResponse.json()['status'])


