import numpy as np 
import cv2 

# function to find circle using opencv Hough Circles method, returns center and radius 
def find_circle(filename): 
    img = cv2.imread(filename, 1)  

    # convert circle to grayscale and blur for Hough Circle algorithm
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15,15), 0)

    # do an initial pass using more sensitive settings to pick up small circles 
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=25, minRadius=0, maxRadius=500)
    
    # check if found a circle (basically to ignore images with small circles in treeline or in sky )
    if circles is not None: 
        # sometimes the algorithm with really big circles and big images detects multiple circles so this call is less sensitive 
        if len(circles[0]) > 1: 
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,20, param1=50, param2=40, minRadius=0, maxRadius=500)
            return circles[0][0]
        else:       
            return circles[0][0]
    else: 
        return None   

# physical characteristics of cameera and buoy 
buoy_height = 100 # mm
sensor_height = 9.6 # mm 1 inch lens 
focal_distance = 35 # mm 

# reading in all of the files 
f = open("buoy.txt", "w")
for i in range(100): 
    filename = f"images/lake{i:02}.jpeg"
    bouy = find_circle(filename)
    # checking if it found a buoy  
    if bouy is not None:    
        # used some triangle similarity: https://photo.stackexchange.com/questions/12434/how-do-i-calculate-the-distance-of-an-object-in-a-photo
        distance = (focal_distance * buoy_height * 2000)/(bouy[2] * 2 * sensor_height) / 1000 # convert to meters
        f.write(f"{i:02}:({bouy[0]}, {bouy[1]}) {bouy[2]} {distance}\n")
    else:    
        f.write(f"{i:02}:No buoy detected\n")

f.close()