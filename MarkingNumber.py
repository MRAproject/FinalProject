import cv2


def Work(data, imagePath):
    xmin = data['box']['xmin']
    xmax = data['box']['xmax']
    ymin = data['box']['ymin']
    ymax = data['box']['ymax']
    img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
    img = cv2.resize(img, (800, 600))
    cv2.imshow('image', img)
