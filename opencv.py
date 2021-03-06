import cv2 as cv
import numpy as np
import os

stream = cv.VideoCapture("temp.mp4")

# Dummy example, just iterate through all frames

count = 0
while stream.isOpened():
    success, frame = stream.read()
    if not success:
        break
    else:
      count += 1

    print(count)

# Write some dummy results
with open(os.environ['UPLOAD_FILE_NAME'], 'w') as f:
    f.write('Test\n')

print("Done")