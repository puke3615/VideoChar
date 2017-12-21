# coding=utf-8
import numpy as np
from utils import *
import time
import cv2
import sys
import os

args = sys.argv[1:]
params = dict(arg.split('=') for arg in args)

targetW = int(params['w']) if params.__contains__('w') else 50
cap = cv2.VideoCapture('2.mp4')
W, H = int(cap.get(4)), int(cap.get(3))
targetH = int(targetW * H / W)
print '(%d, %d) => (%d, %d)' % (W, H, targetW, targetH)
print get_char((targetW, targetH))

while (cap.isOpened()):
    ret, frame = cap.read()

    if frame is not None:
        # cv2.imshow('image', frame)

        os.system('clear')
        sys.stdout.write(img2char(frame, (targetW, targetH)))
        sys.stdout.flush()
    time.sleep(0.1)
    k = cv2.waitKey(20)
    # q键退出
    if k & 0xff == ord('q'):
        break

sys.stdout.close()
cap.release()
cv2.destroyAllWindows()
