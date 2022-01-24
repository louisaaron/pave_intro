from PIL import Image
import numpy as np
import os
import math as Math

centers = []
radii = []
distances = []

data_dir = "./images/"

for entry in os.listdir(data_dir):
    ## Read in files; obtain width, height, & color channels;
    image = Image.open(os.path.join(data_dir, entry))
    image.convert("RGB")
    img_arr = np.array(image)
    
    w = img_arr.shape[0]
    h = img_arr.shape[1]
    
    # Keeps track of the leftmost, rightmost, highest, and lowest
    # red pixels, as we iterate
    highest = -1;
    lowest = h-1;
    leftmost = w-1;
    rightmost = -1; 
    
    # NOTE: I had trouble identifying the color channels for the red pixels.
    # Though I took them to be [99, 109, 74], the answer may be different.
    
    ## Iterate over the pixels in the image. To reduce time taken, we skip in steps of 10 pixels
    
    red_pixels = 0 # tracks number of red_pixels
    
    for i in range(math.floor(w/10)):
        for j in range(math.floor(h/10)):
            x = 10 * i
            y = 10 * j
            if (np.allclose(img_arr[x, y, :], [99, 109, 74])):
                if (x < leftmost):
                    leftmost = x
                if (x > rightmost):
                    rightmost = x
                if (y < lowest):
                    lowest = y
                if (y > highest):
                    highest = y   
                red_pixels += 1
                
    ## Verify there is a red buoy!
    if (red_pixels < 3): 
        print("No buoy detected.")
        exit()
        
    ## Determine the center and radius
    center = ((leftmost + rightmost)/2, (highest + lowest)/2)
    
    ball_height = abs(highest - lowest)
    ball_width = abs(rightmost - leftmost)
    radius = max(ball_height/2, ball_width / 2) # Take the maximum to account for when the 
    # ball is cutoff by the screen
    
    centers.append(center)
    radii.append(radius)
    
    ## Now, calculate how far away the treeline is, and
    # how tall it is to detrmine a pixel-distance conversion
    
    top_tree = -1;
    bottom_tree = h-1;
    
    for k in range(Math.floor(h / 10)):
        if (np.allclose(img_arr[0, 0, 10 * k], [176, 194, 218])): ## Again, numbers may be wrong
            if (k < bottom_tree):
                bottom_tree = k
            if (k > top_tree):
                top_tree = k
    
    height_trees = top_tree - bottom_tree
    
    distance_trees = bottom_tree
    
    # Assumptions: 
    # - The treeline is a mile away
    # - The size of an object is proportional to its distance away from the bottom of the lens
    
    
    y_cood = center[1]
    scale_factor = (y_cood) / distance_trees
    distance_ball = scale_factor * 1 ## in miles 
    
    distances.append(distance_ball)

print("Centers:")
print(centers)
print("Radii:")
print(radii)
print("Distances:")
print(distances)