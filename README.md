# graph_grabber
Grabs data from image of a graph

1. Import an image file. It will get scaled and displayed on the window. At the moment it is not possible to zoom in or out of the image.
2. Calibrate the image:
  i. Click on the image using the mouse and enter the x-value (horizontal) at that point.
  ii. Click on another position and enter the x-value there.
  iii. Repeat for y-axis (vertical).
  iv. If it is a log plot, check the checkbox and make sure that you use major ticks to calibrate. Minor ticks can be used to calibrate only for linear plots, and not for log plots.
  v. Once all 4 values, 2 for x-sxis and 2 for y-axis have been entered, the program calibrates the image. 
 3. After calibration, click anywhere on the image to get the x- and y-coordinates.
 4. Right click to save the coordinate.
 5. Click print saved points to print the list of coordinates in python terminal.
