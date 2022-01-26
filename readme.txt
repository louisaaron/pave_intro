"images" is a directory containing the dataset for this project.

"Buoy.pdf" shows the relevant hand calculations used in finding the
distance between the camera and buoy in each image.

"main.py" is the main program method that detects buoys in the dataset
along with the required information.

"Output.txt" lists the name of each image, followed by the x- and y-
coordinates of the center of the detected buoy (in pixels, with the
bottom left of the image set as the origin), the radius of the detected
buoy (in pixels), and the calculated distance between the camera and the
buoy in the image (in meters). If no buoy is detected, a corresponding
message is printed.

To detect each buoy, each individual pixel in an image is iterated over.
When a red pixel is detected, the program breaks out of the double
for-loop in use and instead iterates directly down the current column
until the pixels are no longer red--registering the number of pixels
iterated over as the diameter in pixels.
