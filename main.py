import os
import sys
import cv2
import numpy as np

color_hsv = np.array([[[0, 0, 0], [180, 255, 35]], [[0, 0, 35],[180, 43, 220]],
                      [[0, 0, 221], [180, 30, 255]],[[156,43, 35],[180, 255, 255]],
                     [[11, 43, 35], [25, 255, 255]], [[26, 43, 35],[34, 255, 255]],
                      [[35, 43, 35], [77, 255, 255]], [[78, 43, 35],[99, 255,255]],
                      [[100, 43, 35],[124, 255,255]], [[125, 43, 46],[155, 255, 255]]])

index_color_dict = {0:'black', 1: 'gray', 2:'white', 3:'red', 4:'orange',
                    5: 'yellow',6: 'cyan',7:'green', 8: 'blue', 9:'purple'}


if __name__ == '__main__':
    img_root = './data/'
    with open('./data/img.lst') as f:
        lines = f.readlines()
        for line in lines:
            img_path = os.path.join(img_root, line.strip())
            img = cv2.imread(img_path)

            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            H, S, V = cv2.split(img_hsv)

            count_list = [0 for i in range(color_hsv.shape[0])]

            for i in range(color_hsv.shape[0]):

                mask_black = cv2.inRange(img_hsv, color_hsv[i][0], color_hsv[i][1])
                mask_white = cv2.inRange(img_hsv, color_hsv[i][1], color_hsv[i][0])

                result = mask_black + mask_white

                count_list[i] = list(result.flatten()).count(255)

            color_index = count_list.index(max(count_list))
            print('color: ', index_color_dict[color_index])



















