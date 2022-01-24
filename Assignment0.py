import cv2
import math

initCenter = [(None, None)]
initRadius = [0]
initDistance = [None]

centers = initCenter * 100
radii = initRadius * 100
distances = initDistance * 100

for i in range(100): 
    
    # Read image.
    img = cv2.imread('/Users/willowyang/PAVE/Assignment0/images/lake%d.jpeg'
                     %i, cv2.IMREAD_COLOR)
    
    # Convert to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))
      
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred, 
                       cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                   param2 = 20, minRadius = 1, maxRadius = 200)
      
    # Add to centers, radii, distances for circles that are detected.
    if detected_circles is not None:
        
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            
            x = list(centers[i])
            x[0] = pt[0]
            x[1] = pt[1] 
            centers[i] = tuple(x)
            
            radii[i] = pt[2]
            
            # distance_mm = object_real_world_mm * 
            # focal-length_mm / object_image_sensor_mm
            # Assuming actual object's radius = 15mm
            # Assuming focal length of the lens = 4.15mm 
            # Assuming 133 px/mm
            
            area = (math.pi)*(pt[2] ** 2)
            areaMili = area / 133
            
            
            distances[i] = round((100 * 4.15 / areaMili), 2)
            
centers = tuple(centers)
radii = tuple(radii)
distances = tuple(distances)

print(centers)
print(radii)
print(distances)

# citation:
# https://stackoverflow.com/questions/14038002/opencv-how-to-calculate-distance-between-camera-and-object-using-image
# https://www.geeksforgeeks.org/circle-detection-using-opencv-python/




            
            



