import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../data/test/1451545258636_spine.jpg',0)          # queryImage
img2 = cv2.imread('../data/test/1451711419823_spine.jpg',0) # trainImage

# Initiate SIFT detector
# sift = cv2.SIFT()
surf = cv2.SURF(400)

# find the keypoints and descriptors with SIFT
# kp1, des1 = sift.detectAndCompute(img1,None)
# kp2, des2 = sift.detectAndCompute(img2,None)
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
matches = sorted(matches, key = lambda x:x[0].distance)
Distance = []
for m in matches:
    Distance.append(m[0].distance)
    # print m[0].distance

print np.average(Distance)
# Apply ratio test
# good = []
# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])

# # create BFMatcher object
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#
# # Match descriptors.
# matches = bf.match(des1,des2)
#
# # Sort them in the order of their distance.
# matches = sorted(matches, key = lambda x:x.distance)
# for m in matches:
#     print m.distance
# cv2.drawMatchesKnn expects list of lists as matches.
# img3 = dr/awMatches(img1,kp1,img2,kp2,matches)

# plt.imshow(img3),plt.show()
