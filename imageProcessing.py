import MarkingVehicleNumber
import GetValueVehicleNumber

imagePath = 'D:/tmp/imageM.jpeg'

MarkingVehicleNumber.Work(imagePath)
VehicleNumber = GetValueVehicleNumber.Work(imagePath)

print(VehicleNumber)
