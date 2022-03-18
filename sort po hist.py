import os
from matplotlib import pyplot as plt
import cv2
import numpy as np
import shutil


path = "img//"
files = os.listdir(path)
glare=list()
for i in range(len(files)):
    img = cv2.imread(path+files[i])
    hist, bins = np.histogram(img, 256, [0, 256])
    index = np.argmax(hist)
    if index >= 250:
        glare.append(files[i])

if not os.path.isdir('output1'):
    os.mkdir('output1')

path_save = 'output1//'

for i in range(len(glare)):
    shutil.copyfile(f'{path}{glare[i]}', f'{path_save}{glare[i]}')
