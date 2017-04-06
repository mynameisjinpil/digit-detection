import cv2 # OpenCV Package
import numpy as np
import glob
import os
import peakutils
from oct2py import octave

from matplotlib import pyplot as plt

print cv2

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
        s_px = []

        print Img.shape

      # pixel count
        for y in range(0, Img.shape[1]):
            for x in range(0, Img.shape[0]):
                if Img[x, y] == 0:
                    px[x] += 1
        #print (px)

        cb = np.array(px)

        # 1.
        # indexes = peakutils.indexes(cb, thres = 0.02/max(cb), min_dist = 100)
        # interpolatedIndexes = peakutils.interpolate(np.arange(0, len(cb)), cb, ind=indexes)
        #
        # print interpolatedIndexes
        #
        # plt.plot(interpolatedIndexes)

        #2.
        octave.eval("pkg load signal")
        (peaks, indexes) = octave.findpeaks(cb, 'DoubleSided', 'MinPeakHeight', 0.04, 'MinPeakDistance', 100, 'MinpeakWidth', 0)


        #print len(px)
        #fw.write('[')

        # for i in range(len(cb)):
        #     if cb[i] != 0:
        #
        #         fw.write(str(cb[i]))
        #         fw.write(',')
        #         fw.write(' ')
        #         count+=1
        #
        # for i in range(0, 119 - count):
        #     fw.write('0')
        #     fw.write(',')
        #     fw.write(' ')
        #
        # fw.write(']')
        #
        # fw.write(str(n))
        # fw.write('\n')

        #fw.write(str(interpolatedIndexes[0]))
        fw.write('\n')

        #cv2.imshow(ImgPath + 'histo', Histo)

        print count

if __name__ == '__main__':
    handle_image()
    plt.show()