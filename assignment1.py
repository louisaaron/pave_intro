import cv2
import numpy as np
import math
import os

l = os.listdir('/Users/cynthia/pave_intro/images')
centers = []
radii = []
distances = []

def find_circle(image):
    #load image, convert to grayscale
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.blur(gray, (3, 3))
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 0, maxRadius = 40)
    n = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for j in circles[0, :]:
            #Drawing the circumference
            cv2.circle(img, (j[0], j[1]), j[2], (0, 255, 0), 2)
            #Drawing the center
            cv2.circle(img, (j[0], j[1]), 1, (0, 255, 0), 3)
            #Adding to the radius, distance, and center arrays
            centers.append("(" + str(j[0]) + ", " + str(j[1]) + ")")
            radii.append(str(j[2]))
            distances.append(distance_to_camera(j[2]))


# focal length of iphone 12 pro = 5.1mm on 1x zoom
# PPI of iphone 12 pro is 72, inches to mm is 1:25.4
# distance = size of object * focal length of the lens / size of the object on the sensor
# assuming pixels per millimeter ratio is 120 px/mm and actual radius of bouy is 15" (381 mm)
def distance_to_camera(radius):
    # height, width, channels = img.shape
    return 381 * 5.1 / (math.pi * (radius / 2.8346) ** 2)

for i in range(0, len(l)):
    num = str(i)
    if i < 10:
        num = "0" + str(i)
    find_circle('/Users/cynthia/pave_intro/images/lake'+num+'.jpeg')
    # print(centers)
    # print(radii)
    print(distances)

#sources
#https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
#https://www.photoreview.com.au/tips/outputting/image-size-and-resolution-requirements/
#https://stackoverflow.com/questions/14038002/opencv-how-to-calculate-distance-between-camera-and-object-using-image
