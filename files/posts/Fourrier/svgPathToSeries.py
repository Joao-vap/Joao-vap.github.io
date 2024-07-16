# define constants
directory = "Paths"
fileDir = "Originaldraw"
file = "dice"
filepath = fileDir + "/" + file + ".svg"
nPoints = 10000 # per path

# Importing relevant libraries
from svgpathtools import parse_path
from xml.dom import minidom
from matplotlib import pyplot as plt

# parse svg file
svg_dom = minidom.parse(filepath)

# get path strings
path_strings = [path.getAttribute('d') for path in svg_dom.getElementsByTagName('path')]

# for each path string, parse it
data = []
for path_string in path_strings:
    path_data = parse_path(path_string)
    data.append(path_data)

with open(directory + "/" + file + ".txt", "w") as my_file:
    for elem in data:
        for p in range(1,nPoints):
            p = p/nPoints
            pt = elem.point(p)
            my_file.write(str(-pt) + "\n")

