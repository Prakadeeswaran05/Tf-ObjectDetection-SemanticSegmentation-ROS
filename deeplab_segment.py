import collections
import os
import io
import sys
import tarfile
import tempfile
import urllib
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image as ros_img
from notcv_bridge import *
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image 
import cv2

from model import DeepLabModel

import get_dataset_colormap

_TARBALL_NAME = 'deeplab_mnv3_large_cityscapes_trainfine_2019_11_15.tar.gz'


model_dir = '/home/ros/tf_ws/src/obj_det/scripts'


file_path = os.path.join(model_dir, _TARBALL_NAME)


model = DeepLabModel(file_path)
 
 
def callback(data):
    out = imgmsg_to_cv2(data)
    cv2_im = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im)
        
     # Run model
    resized_im, seg_map = model.run(pil_im)
        
     # Adjust color of mask
    seg_image = get_dataset_colormap.label_to_color_image(
    seg_map, get_dataset_colormap.get_cityscapes_name()).astype(np.uint8)
        
    # Convert PIL image back to cv2 and resize
    frame = np.array(pil_im)
    r = seg_image.shape[1] / frame.shape[1]
    dim = (int(frame.shape[0] * r), seg_image.shape[1])[::-1]
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    seg_image = cv2.cvtColor(seg_image, cv2.COLOR_RGB2BGR)
    resized = cv2.cvtColor(resized, cv2.COLOR_RGB2BGR)
        
    # Stack horizontally color frame and mask
    color_and_mask = np.hstack((resized, seg_image))
    print(color_and_mask.shape)

    cv2.imshow('frame', color_and_mask)
    cv2.waitKey(1)
    
    
    
def main():
    rospy.init_node('image_sub', anonymous=True)
    rospy.Subscriber('camera/image_raw',ros_img,callback)
    rospy.spin()
    

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()


