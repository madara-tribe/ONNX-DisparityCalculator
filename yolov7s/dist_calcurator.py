import numpy as np
from enum import Enum


class CAM_PARAM(Enum):
    W_SIDEMAXSITA = 180
    H_SIDEMAXSITA = 180
 
def dist_ratio(d):
    if d > 50:
        dif = CAM_PARAM.W_SIDEMAXSITA.value/12
    elif d > 40 and d <= 50:
        dif = CAM_PARAM.W_SIDEMAXSITA.value/10
    elif d > 30 and d <= 40:
        dif = CAM_PARAM.W_SIDEMAXSITA.value/8
    else:
        dif = 0
    return dif
    
def angle_formula(x, y, w_per_angle, h_per_angle, distance):
    x_angle = w_per_angle * x
    y_angle = h_per_angle * y
    # print("xper, x, yper, y", w_per_angle, x, h_per_angle, y)
    # dist
    #dist_diff = dist_ratio(distance)
    #print("x, w_per_angle", x, w_per_angle)
    return x_angle, y_angle
    
def distance_formula(disparity, w_element, hyp):
    B = hyp['CAM_BASELINE'] # [cm]
    f = hyp['FOCAL_LENTH'] # [cm]
    d = w_element # [cm/px]
    dist = (f/d)*(B/disparity) # [cm]
    print('(f*B/d)', f, B, d, (f*B/d))
    return dist
    
def prams_calcurator(hyp, disparity, width, height, x, y):
    w_per_angle = CAM_PARAM.W_SIDEMAXSITA.value / width # [θ]
    h_per_angle = CAM_PARAM.H_SIDEMAXSITA.value / height # [θ]
    w_element = hyp['W_PER_PIXEL_ELEMENT'] * (hyp['W_RESOLUTION'] / width)
    
    distance = distance_formula(disparity, w_element, hyp)
    angleX, angleY = angle_formula(x, y, w_per_angle, h_per_angle, distance)
    return disparity, np.round(distance, decimals=2), np.round(angleX, decimals=2), np.round(angleY, decimals=2)
 

