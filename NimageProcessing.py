import GetValueVehicleNumber
from PIL import Image
import glob
import delete

def Work(folder):
    image_list = []
    for filename in glob.glob(folder+'*.jpeg'):
        im = Image.open(filename)
        image_list.append(im.filename)

    VehicleNumber = None

    for image in image_list:
        try:
            VehicleNumber = GetValueVehicleNumber.Work(image)
        except:
            continue
        
    #print(VehicleNumber)
    delete.Work(folder)
    return(VehicleNumber)
    #exit()
