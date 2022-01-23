/*  This program assumes that either the upper and lower edges, or the left and right
    edges of the red sphere in the given picture exist in the frame (i.e. the circle is not
    cut off by more than one side of the image). Then it finds the center of the circle
    by taking the average of two of these coordinates, the radius by calculating
    half of the distance between them, and distance to the camera using the formula
    below:

    object size in image = Object size * focal length / object distance from camera
    assume 35 mm focal length, obj size in image = radius, real obj radius = 1 m; DPI of photo is 96
    ( pixels * 25.4 ) / 96 = length in mm
    dist in meters = 1 m * 0.035 m / (10^-3 * radius in pixels * 25.4 / 96) = 132.28 / radius in pixels

    Run with the command "java BuoyFinder reader.txt"
    */

import java.awt.Color;

public class BuoyFinder {
    // returns the coordinates for the upper edge of the red circle in the picture
    public static int[] findUpperEdge(Picture that) {
        int width = that.width();
        int height = that.height();
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                Color pixel = that.get(j, i);
                int red = pixel.getRed();
                if (red > 200) {
                    int right = width;
                    for (int t = j; t < width; t++) {
                        red = that.get(t, i).getRed();
                        if (red < 200) {
                            right = t - 1;
                            break;
                        }
                    }
                    int[] edge = { i, (j + right) / 2 };
                    return edge;
                }
            }
        }
        return null;
    }

    // returns the coordinates for the LOWER edge of the red circle in the picture
    // given the coordinates for the upper edge (null if lower edge is not in the frame)
    public static int[] findLowerEdge(Picture that, int[] edge) {
        int height = that.height();
        int j = edge[1];
        for (int i = edge[0]; i < height; i++) {
            int blue = that.get(j, i).getBlue();
            int red = that.get(j, i).getRed();
            if (blue > 200 && red < 180) {
                int[] lowerEdge = { i - 1, j };
                return lowerEdge;
            }
        }
        return null;
    }

    // returns the coordinates for the left edge of the red circle in the picture
    public static int[] findLeftEdge(Picture that) {
        int width = that.width();
        int height = that.height();
        for (int j = 0; j < width; j++) {
            for (int i = 0; i < height; i++) {
                Color pixel = that.get(j, i);
                int red = pixel.getRed();
                if (red > 200) {
                    int right = height;
                    for (int t = i; t < height; t++) {
                        int newRed = that.get(j, t).getRed();
                        if (newRed < 200) {
                            right = t - 1;
                            break;
                        }
                    }
                    int[] edge = { (i + right) / 2, j };
                    return edge;
                }
            }
        }
        return null;
    }

    // returns the coordinates for the LOWER edge of the red circle in the picture
    // given the coordinates for the upper edge (null if lower edge is not in the frame)
    public static int[] findRightEdge(Picture that, int[] edge) {
        int width = that.width();
        int i = edge[0];
        for (int j = edge[1]; j < width; j++) {
            int blue = that.get(j, i).getBlue();
            int red = that.get(j, i).getRed();
            if (blue > 200 && red < 180) {
                int[] rightEdge = { i, j - 1 };
                return rightEdge;
            }
        }
        return null;
    }

    // runs the methods on a hundred different examples
    public static void main(String[] args) {
        // Reads the file names from a .txt file
        In files = new In(args[0]);
        int[][] centers = new int[100][2];
        int[] radii = new int[100];
        double[] distances = new double[100];

        int i = 0;
        while (!files.isEmpty()) {
            String file = files.readString();
            Picture current = new Picture(file);
            int[] upperEdge = findUpperEdge(current);
            int[] lowerEdge = null;
            // if upper edge was found, goes on to calculate lower edge
            if (upperEdge != null) {
                lowerEdge = findLowerEdge(current, upperEdge);
                if (lowerEdge != null) {
                    centers[i][0] = (upperEdge[0] + lowerEdge[0]) / 2;
                    centers[i][1] = upperEdge[1];
                    radii[i] = (lowerEdge[0] - upperEdge[0] + 1) / 2;
                    distances[i] = 132.28 / radii[i];
                }
            }

            // if either one of the edges wasn't found, tries to find the left and right edges
            if (upperEdge == null || lowerEdge == null) {
                int[] leftEdge = findLeftEdge(current);
                if (leftEdge != null) {
                    int[] rightEdge = findRightEdge(current, leftEdge);
                    if (rightEdge != null) {
                        centers[i][1] = (leftEdge[1] + rightEdge[1]) / 2;
                        centers[i][0] = leftEdge[0];
                        radii[i] = (rightEdge[1] - leftEdge[1] + 1) / 2;
                        distances[i] = 132.28 / radii[i];
                    }
                }
            }
            i++;
        }
        for (int j = 0; j < 100; j++) {
            if (radii[j] > 0) {
                System.out.println(j + " Radius in pixels: " + radii[j]
                                           + ", Center: (" + centers[j][0] + ", "
                                           + centers[j][1] + "). Distance to camera in meters: "
                                           + distances[j]);
            }
            else {
                System.out.println(j + " no buoy found.");
            }
        }

    }
}
