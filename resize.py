import cv2
import numpy as np

def resize(boxes):
    for (sX, eX, eY, sY) in boxes:
        x_diff = eX - sX
        y_diff = eY - sY
        if x_diff > 150:
            dX = x_diff - 150
            print(dX)

resize([(63, 198, 227, 47), (186, 390, 255, 74)])