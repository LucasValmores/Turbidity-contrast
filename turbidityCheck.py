import cv2

#import images
imgLeftTestTube = cv2.imread("samplePhotos/left test tube.jpeg", cv2.IMREAD_GRAYSCALE)
imgRightTestTube = cv2.imread("samplePhotos/right test tube gray scale.jpeg", cv2.IMREAD_GRAYSCALE)
imgBackground= cv2.imread("samplePhotos/background sample.jpeg", cv2.IMREAD_GRAYSCALE)

#take average grayscale value of all three images
leftmean = cv2.mean(imgLeftTestTube, mask=None)[0]
rightMean = cv2.mean(imgRightTestTube, mask=None)[0]
BackgroundMean = cv2.mean(imgBackground, mask=None)[0]


print("average grayscale values of left test tube:", leftmean)
print("average grayscale values of right test tube:", rightMean)
print("average grayscale values of background:", BackgroundMean)

LeftContrast = leftmean - BackgroundMean
RightContrast = rightMean - BackgroundMean

#display contrast
print("left testTube contrast: ", LeftContrast)
print("right testTube contrast: ", RightContrast)





