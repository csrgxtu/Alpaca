import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/img/787538868524-1450531970275_spine.jpg', 0)

surf = cv2.SURF(300)

kp, des = surf.detectAndCompute(img,None)
print type(des)
print des.shape
print des
# print des.tostring()

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

# plt.imshow(img2),plt.show()
