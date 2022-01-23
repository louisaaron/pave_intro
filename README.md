# Code

I basically found code online that could detect circles, altered some of the conditions so that it worked best for this dataset, and used this to compute the centers and radii of the buoys. I explain how I calculated distance in the code.


# pave_intro
Week 0 PAVE assignment

Hi everyone. Excited to get started. As I mentioned in the meeting today, this assignment will range from fairly trivial to somewhat challenging depending on you coding background, but should be very doable for everyone. Feel free to do a simple pixel-search implementation or something fancier with a CNN. Here are the goals:
1. Identify the center and radius of the "buoy" in each image.
2. Make some assumptions about the hardware, then determine the buoys' distances from the camera.
I recommend saving outputs in three lists (```centers```, ```radii```, ```distances```) where ```centers[0]``` has tuples of the centers of the buoy for ```lake0.jpeg```, ```radii[0]``` has the radius, and ```distances[0]``` has the distance in your preferred unit.

NOTE: The dataset was made so poorly that sometimes the buoy is in the trees or the sky (sorry). On the bright side, it makes for some practice of cleaning the dataset-- feel free to eliminate any images with buoys in the sky from the dataset.

If you don't have any image processing experience, my hint is to basically Google search "how to read images into Python", save the images to a directory on your hard drive, and Stackoverflow your way through it. Python is fantastic for image processing.

Let me know if you have any questions. Feel free to work in teams. After this week, we'll create a Slack and get started in subteams.
