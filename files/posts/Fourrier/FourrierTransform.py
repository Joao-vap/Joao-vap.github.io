# relevant libraries

import numpy as np
import matplotlib.pyplot as plt

# we have a file with a complex time series
# lets extract it

directory = "Paths"
latexDirectory = "Latex"
file = "JIP"
filePath = directory + "/" + file + ".txt"

data = []
with open(filePath, 'r') as my_file:
    lines = my_file.readlines()
    for line in lines:
        pt = complex(line)
        data.append(pt)

# remove 70 from real part in first 9999 points
# remove 10 from imaginary part in first 9999 points
for i in range(9999):
    data[i] = data[i] - 65 - 10j

# we have a series of complex data
# we are going to perform a fourrier transform on it.

data = np.array(data)
fourrier = np.fft.fft(data)

# lets check if we can reconstruct the original data

reconstructed = np.fft.ifft(fourrier)

# lets plot the original data and the reconstructed data

# plt.plot(reconstructed.real, reconstructed.imag, 'ro')

# lets write the fourrier transform to a file as LATEX code

freqs = np.fft.fftfreq(len(data), d=1/len(data))

# reorganize the data so that the lowest frequencies are first
# this is so that we can easily see the highest frequencies
# in the latex file

# process the fourrier transform
fourrier = fourrier/len(data)

with open(latexDirectory + "/" + file + ".txt", "w") as my_file:
    message = "F(x) = "
    for i in range((len(fourrier)//2 +1)):
        if i == 0:
            message += f"({fourrier[i]:.2f}) + "
        elif fourrier[i] == fourrier[-i]:
            break
        else:
            message += f"({fourrier[i]:.2f})" + "  * e**(" + f"{int(freqs[i])} *" + "(2*3.1415*j*x))  + "
            message += f"({fourrier[i]:.2f})" + "  * e**(" + f"{int(freqs[-i])} *" + "(2*3.1415*j*x)) + "
    my_file.write(message)

# do a gif of the fourrier transform
from PIL import Image

#set proportions
plt.axis('equal')
plt.xlim(0, -300)
plt.ylim(0, -230)

images = []
for i in range(1, 1000):
    print(i)
    t = i/1000
    value = 0
    for j in range(len(fourrier)):
        value += fourrier[j]*np.exp(2*np.pi*freqs[j]*t*1j)
    # invert the y axis
    value = -value
    plt.plot(value.real, value.imag, 'ro')      
    plt.savefig("Images/" + str(i) + ".png")
    images.append(Image.open("Images/" + str(i) + ".png"))

#append every 3rd image to the first image
images[0].save("Images/" + file + ".gif", save_all=True, append_images=images[1:], optimize=False, duration=0.05, loop=0)
