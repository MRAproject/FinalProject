from picamera import PiCamera
from time import gmtime,strftime,sleep
import datetime
import NimageProcessing
import delete
import threading
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


camera = PiCamera()
folder = 'Camera samples/'
def Work():
    print('insert')
    for i in range(3):    
        output = strftime(folder+'image-'+str(i)+'.jpeg')
        camera.capture(output)
        
    NimageProcessing.Work(folder)

print('starting...')
rt = RepeatedTimer(13, Work) # it auto-starts, no need of rt.start()
try:
    sleep(1000000) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!