import cv2
import numpy as np

    
def compute_flow(impath_1, impath_2):
    first_frame = cv2.imread(impath_1)

    if first_frame is None:
        print("Error reading frame:", impath_1)
        return None

    resize_dim = 224
    max_dim = max(first_frame.shape)
    scale = resize_dim/max_dim

    first_frame = cv2.resize(first_frame, None, fx=scale, fy=scale)
    prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

    second_frame = cv2.imread(impath_2)

    resize_dim = 224
    max_dim = max(second_frame.shape)
    scale = resize_dim/max_dim

    second_frame = cv2.resize(second_frame, None, fx=scale, fy=scale)
    next_gray = cv2.cvtColor(second_frame, cv2.COLOR_BGR2GRAY)



    flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None, 
                                        pyr_scale = 0.5, 
                                        levels = 5, 
                                        winsize = 11, 
                                        iterations = 5, 
                                        poly_n = 5, 
                                        poly_sigma = 1.1, 
                                        flags = 0)

    return flow