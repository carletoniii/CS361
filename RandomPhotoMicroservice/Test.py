import matplotlib.image as mpimg
import time

import matplotlib.pyplot as plt

while True:
    time.sleep(5)
    operation = open("Request.txt", "w")
    operation.write("1")
    operation.close()
    operation2 = open("PhotoFilename.txt", "r")
    line = operation2.readline()
    operation2.close()
    img = mpimg.imread(line)
    imgplot = plt.imshow(img)
    plt.show()
