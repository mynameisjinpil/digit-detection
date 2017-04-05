import cv2 # OpenCV Package
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


def handle_image():
    File_List = glob.glob('./images/1/*.png')

    fw = open("./output/output1.txt", "w")

    for n in range(0, 10):
        # load image file
        ImgPath = (File_List[n])
        Img = cv2.imread(ImgPath, cv2.IMREAD_GRAYSCALE)

        count = 0
        fw.write(ImgPath)
        fw.write(' : ')
        fw.write('\n')
        #cv2.imshow(ImgPath, Img)
        print ("success: " + os.path.basename(File_List[n])) # file load check

        # 'px' set for zero
        px = [0] * Img.shape[0]

        print Img.shape

      # pixel count
        for y in range(0, Img.shape[1]):
            for x in range(0, Img.shape[0]):
                if Img[x, y] == 0:
                    px[x] += 1
        #print (px)

        # draw Histo
        Histo = np.zeros((Img.shape[0], Img.shape[1], 1), np.uint8)

        for i in range(0, Img.shape[0]):
             for j in range(0, len(px)):
                 Histo[px[i]][i] = [255]

        #print len(px)
        fw.write('[')

        for i in range(len(px)):
            if px[i] != 0:

                fw.write(str(px[i]))
                fw.write(',')
                fw.write(' ')
                count+=1

        for i in range(0, 119 - count):
            fw.write('0')
            fw.write(',')
            fw.write(' ')

        fw.write(']')

        fw.write(str(n))
        fw.write('\n')


        cv2.imshow(ImgPath + 'histo', Histo)

        print count

if __name__ == '__main__':
    handle_image()
    cv2.waitKey()