import GetValueVehicleNumber
from PIL import Image
import glob

def Work():
    image_list = []
    for filename in glob.glob('Camera samples/*.jpeg'):
        im = Image.open(filename)
        image_list.append(im.filename)

    VehicleNumber = None

    for image in image_list:
        try:
            VehicleNumber = GetValueVehicleNumber.Work(image)
        except:
            continue
        
    print(VehicleNumber)       
    exit()
