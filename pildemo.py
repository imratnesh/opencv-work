# -*- coding: utf-8 -*-
from PIL import Image

import numpy as np
import pandas as pd

import cv2

size_40 = (40,40)
size_80 = (80,80)

img = Image.open('./images/jpgs/HappyFish.jpg')

#img = img.rotate(90)
img.thumbnail(size_80)
#img.save('./images/thumb_80.png')

img.show()