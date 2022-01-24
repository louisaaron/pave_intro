import cv2

# double array that stores RGB values of associated pixels from image
img = cv2.imread("images\lake00.jpeg")

# image height (pixels).. number of rows
height = len(img)

# image length (pixels).. number of columns
length = len(img[0])

# loop to find the topmost pixel of the buoy
for i in range(height): # row
    for j in range(length): # column
        B = img[i][j][0]
        G = img[i][j][1]
        R = img[i][j][2]

        red = R > G and R > B

        if red:
            break

    if red:
        break

# at this point, i is row of topmost pixel, and j is column

# diameter of buoy (pixels)
diameter = 0

# loop to find diameter
for k in range(i, height):
    B = img[k][j][0]
    G = img[k][j][1]
    R = img[k][j][2]

    red = R > G and R > B

    if red:
        diameter = diameter + 1
    else:
        break

# at this point, i is row of topmost pixel, and j is column
# k is row of bottommost pixel

# radius of buoy (pixels)
radius = int(diameter / 2)

# center as (x, y) coordinates in pixels! Bottom left corner is origin
center = (j, height - (i + radius))
