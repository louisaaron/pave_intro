# pave_intro

## Some comments

This method is probably not the simplest or most accurate way to achieve the desired result considering the fact that the colors in the images have uniform color and regular shapes, but I believe it is well suited for the irregularity in shape and color that may come from a real image. That said, it could take a lot of time to tune the thresholds to get accurate results in the real world, possibly leading other image segmentation algorithms to be more feasible. Using a threshold to find certain color pixels is useful when the pixels are not uniform and using the maximum distance between two pixels in a shape as an effective diameter is useful when the shape is irregular. On the other hand, my method for detecting whether the buoy is above the treeline is only accurate when the treeline is perfectly horizontal. This could be fixed by using more complex segmentation algorithms, but I thought it wasn't worth implementing them for this purpose. Also see 'derivation.jpeg' for how I arrived at my formula for the distance to the buoy.

## Week 0 PAVE assignment

Hi everyone. Excited to get started. As I mentioned in the meeting today, this assignment will range from fairly trivial to somewhat challenging depending on you coding background, but should be very doable for everyone. Feel free to do a simple pixel-search implementation or something fancier with a CNN. Here are the goals:

1. Identify the center and radius of the "buoy" in each image.
2. Make some assumptions about the hardware, then determine the buoys' distances from the camera.
   I recommend saving outputs in three lists (`centers`, `radii`, `distances`) where `centers[0]` has tuples of the centers of the buoy for `lake0.jpeg`, `radii[0]` has the radius, and `distances[0]` has the distance in your preferred unit.

NOTE: The dataset was made so poorly that sometimes the buoy is in the trees or the sky (sorry). On the bright side, it makes for some practice of cleaning the dataset-- feel free to eliminate any images with buoys in the sky from the dataset.

If you don't have any image processing experience, my hint is to basically Google search "how to read images into Python", save the images to a directory on your hard drive, and Stackoverflow your way through it. Python is fantastic for image processing.

Let me know if you have any questions. Feel free to work in teams. After this week, we'll create a Slack and get started in subteams.
