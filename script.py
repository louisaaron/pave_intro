import csv
import os
from PIL import Image
import numpy as np
from scipy import ndimage as ndi

# USER DEFINED VARIABLES
dir = "images"
r_threshold = 200  # threshold used to classify a pixel as red
g_threshold = 110  # threshold used to classify a pixel as green
g_threshold_r = 110  # max threshold for r channel used to classify a pixel as green
g_threshold_b = 150  # max threshold for b channel used to classify a pixel as green
skip_threshold = (
    10  # skip image if the number of red pixels is fewer than this threshold
)
fov = 0.25 * np.pi  # camera field of view in rads
rad_actual = 1  # actual radius of buoy in meters

# SCRIPT
centers = []  # vector from top left to center of buoy in pixels
radii = (
    []
)  # apparent radius of buoy in pixels (actual radius is assumed to be 1m to calculate distance)
distances = []  # distance to buoy in meters

count = 0

# sort images in ascending order
images = os.listdir(dir)  # arbitrary order
images.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

for file in images:

    path = os.path.join(dir, file)

    image = Image.open(path)
    image.convert("RGB")  # ensure image is in RGB mode
    # image.show()

    im_array = np.array(image)  # convert image to an array
    im_dim = im_array.shape[0:2]
    im_width = im_dim[1]

    # separate image channels
    im_red = im_array[:, :, 0]  # extract red values as grayscale image
    im_green = im_array[:, :, 1]  # extract green values as grayscale image
    im_blue = im_array[:, :, 2]  # extract blue values as grayscale image

    # FIND BUOY PIXELS

    buoy_bin = np.zeros(im_dim)

    id_red = np.where(
        im_red >= r_threshold
    )  # find indices of pixels with red values above threshold
    # in a real implementation, also check that green and blue values are below a certain threshold if buoy is red

    # check if there even is a buoy
    if id_red[0].size < skip_threshold:
        continue

    buoy_bin[id_red] = 1  # set those pixels to be white
    buoy_bin = ndi.binary_fill_holes(buoy_bin)  # fill holes in buoy

    # TEST
    #buoy_bin_test = buoy_bin
    #buoy_bin_test[buoy_bin_test == 1] = 255
    #Image.fromarray(buoy_bin).save("tests/out%d.jpeg" % (count))

    id_buoy_y, id_buoy_x = np.where(buoy_bin == 1)  # find buoy pixels

    # CHECK IF BUOY IS IN SKY OR TREES

    # find tree pixels
    notwater_bin = np.zeros(im_dim)

    mask = np.logical_and(
        im_green >= g_threshold, im_red < g_threshold_r, im_blue < g_threshold_b
    )
    id_notwater = np.where(mask)

    notwater_bin[id_notwater] = 1
    notwater_bin = ndi.binary_fill_holes(notwater_bin)

    # TEST
    #tree_bin_test = buoy_bin
    #tree_bin_test[tree_bin_test == 1] = 255
    #Image.fromarray(notwater_bin).save("tests/out%d.jpeg" % (count))

    # check if lowest buoy pixels are above lowest tree pixels
    id_lowest_buoy = np.amax(id_buoy_y)
    id_lowest_tree = np.amax(id_notwater[0])

    if id_lowest_buoy < id_lowest_tree:
        continue

    # FIND BUOY STATS

    center = (
        round(np.mean(id_buoy_x)),
        round(np.mean(id_buoy_y)),
    )  # find average location of pixels with red value above threshold
    centers.append(center)

    # take the average of the diameter found length and heightwise
    diameterA = np.amax(id_buoy_x) - np.amin(id_buoy_x)
    diameterB = np.amax(id_buoy_y) - np.amin(id_buoy_y)
    rad_apparent = 0.5 * np.mean([diameterA, diameterB])
    radii.append(rad_apparent)

    # find the distance in meters to the buoy assuming its real radius and the camera's field of view
    distance = im_width / (2 * rad_apparent * np.tan(0.5 * fov))
    distances.append(round(distance, 2))

    count += 1

# write data to csv file
out = open("output.txt", "w")
writer = csv.writer(out)
writer.writerow(centers)
writer.writerow(radii)
writer.writerow(distances)
out.close()


# SOURCES
# https://www.pythontutorial.net/python-basics/python-write-csv-file/
# https://stackoverflow.com/questions/33159106/sort-filenames-in-directory-in-ascending-order
# https://betterprogramming.pub/edge-based-and-region-based-segmentation-using-python-f5364607bff0
