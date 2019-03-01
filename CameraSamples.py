import NimageProcessing
import delete
import requests
from picamera import PiCamera
from time import strftime,sleep
from threading import Timer

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
        try:         
            backendResponse = requests.get("http://10.100.102.15:3001/check_car", params=data, timeout=5)
            print('status code: '+ str(backendResponse.status_code))
            if(backendResponse.status_code == requests.codes.ok):            
                if((backendResponse.json()['status']) == 1):
                    print('-- Car Number: '+ carNumber+' are allowed! --')
                    SetLedGreen()
                else:
                    print('-- Car Number: '+ carNumber+' are not allowed! --')
            else:
                print('Error with status code:'+ str(backendResponse.status_code))       
        except requests.ConnectionError or requests.ConnectTimeout:
            print('Error - Timeout')
        rt.start()
    
print('Starting...')
rt = RepeatedTimer(10, Work) # it auto-starts, no need of rt.start()
try:
    sleep(1000000) # your long-running job goes here...
finally:
    rt.stop()

