# coding=utf-8
from utils import *
import sys
import cv2

args = sys.argv[1:]
params = dict(arg.split('=') for arg in args)

targetW = int(params['w']) if params.__contains__('w') else 50
image = params['image']

img = cv2.imread(image,cv2.IMREAD_COLOR)
H, W = img.shape[:2]
targetH = int(targetW * H / W)
chars = img2char(img, (targetW, targetH))
print chars