# Lets display the Mandelbrot set

import numpy as np
import matplotlib.pyplot as plt

# this function will return the number of iterations it took for the point to escape the circle of radius 2
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# this function returns a 2D array of the mandelbrot set
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],max_iter)
    return n3

# main function to display the mandelbrot set
def display(xmin,xmax,ymin,ymax,width,height,max_iter):

    # configure the image size and resolution
    dpi = 72
    img_width = width
    img_height = height

    # get the 2D array of iterations to scape
    z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,max_iter)

    # configure the plot
    _, ax = plt.subplots(figsize=(img_width/dpi, img_height/dpi), dpi=dpi)
    ticks = np.arange(0,img_width,3*dpi)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    plt.yticks(ticks, y_ticks)
    ax.set_title("Mandelbrot Set")

    # display the image
    ax.imshow(z.T,origin='lower',cmap='hot',extent=[xmin,xmax,ymin,ymax])
    plt.show()

# display uses the entries
xmin = -2.0
xmax = 0.5
ymin = -1.25
ymax = 1.25

width = 1024
height = 1024

max_iter = 100

display(xmin,xmax,ymin,ymax,width,height,max_iter)