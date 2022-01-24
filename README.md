I used this link for the initial code to detect circles: https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/ It was taking too long to tune the parameters to perfectly capture the circle with the resolution of the images and the different radii of the circles but ignore the very smaller cirles in the treeline so I decided to use two different sets of parameters to detect the smaller circles and then if necessary use another set of parameters to detect the larger circle. I used the formula listed in this post: https://photo.stackexchange.com/questions/12434/how-do-i-calculate-the-distance-of-an-object-in-a-photo to estimate the distance and I made some guesses as to what types of hardware that we would use for the camera after doing a little bit of research. 

# pave_intro
Week 0 PAVE assignment

Hi everyone. Excited to get started. As I mentioned in the meeting today, this assignment will range from fairly trivial to somewhat challenging depending on you coding background, but should be very doable for everyone. Feel free to do a simple pixel-search implementation or something fancier with a CNN. Here are the goals:
1. Identify the center and radius of the "buoy" in each image.
2. Make some assumptions about the hardware, then determine the buoys' distances from the camera.
I recommend saving outputs in three lists (```centers```, ```radii```, ```distances```) where ```centers[0]``` has tuples of the centers of the buoy for ```lake0.jpeg```, ```radii[0]``` has the radius, and ```distances[0]``` has the distance in your preferred unit.

NOTE: The dataset was made so poorly that sometimes the buoy is in the trees or the sky (sorry). On the bright side, it makes for some practice of cleaning the dataset-- feel free to eliminate any images with buoys in the sky from the dataset.

If you don't have any image processing experience, my hint is to basically Google search "how to read images into Python", save the images to a directory on your hard drive, and Stackoverflow your way through it. Python is fantastic for image processing.

Let me know if you have any questions. Feel free to work in teams. After this week, we'll create a Slack and get started in subteams.
