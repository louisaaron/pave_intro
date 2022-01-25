import cv2
import os

# function that finds circle's radius (pixels)
def find_radius(double_arr, i, j, height):
    diameter = 0

    for k in range(i, height):
        B = double_arr[k][j][0]
        G = double_arr[k][j][1]
        R = double_arr[k][j][2]

        red = R > G and R > B

        if red:
            diameter = diameter + 1
        else:
            break

    return int(diameter / 2)

# function that finds circle's coordinates (pixels) and radius (pixels)
# returns False if no circle
def find_circle(double_arr):
    has_circle = False
    height = len(double_arr)
    length = len(double_arr[0])

    for i in range(height):
        for j in range(length):
            B = double_arr[i][j][0]
            G = double_arr[i][j][1]
            R = double_arr[i][j][2]

            red = R > G and R > B

            if red:
                has_circle = True
                break

        if red:
            break

    if has_circle:
        radius = find_radius(double_arr, i, j, height)
        x = j
        y = height - (i + radius)
        center = [x, y]

        return [center, radius]
    else:
        return False

# list of file names of images
imgs = os.listdir("images")

# number of pictures in "images" directory
number_of_images = len(imgs)

# list of the coordinates of the buoy in each image (pixels)
centers = [None] * number_of_images

# list of the radius of the buoy in each image (pixels)
radii = [None] * number_of_images

# list of the distances of the buoy from the camera in each image
distances = [None] * number_of_images

# image index
index = 0;

for img in imgs:
    pixels = cv2.imread("images\\"+img)
    value = find_circle(pixels)

    if value == False:
        centers[index] = "No buoy detected."
        radii[index] = "No buoy detected."
        distances[index] = "No buoy detected"
    else:
        centers[index] = value[0]
        radii[index] = value[1]
        distances[index] = 0

    index = index + 1

for i in range(number_of_images):
    print(imgs[i])
    print(centers[i])
    print(radii[i])
    print(distances[i])
