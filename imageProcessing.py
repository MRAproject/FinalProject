import APICall
import MarkingNumber
import cv2

imagePath = 'D:/tmp/skoda.jpeg'
data = APICall.Work(imagePath)

MarkingNumber.Work(data, imagePath)
carNumber = data['plate']

print("carNumber = ", carNumber)
cv2.waitKey()
