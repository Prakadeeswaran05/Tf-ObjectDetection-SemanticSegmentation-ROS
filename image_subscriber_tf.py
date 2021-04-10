#!/usr/bin/env python
#!coding=utf-8
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import cv2
from notcv_bridge import *
import numpy as np
import sys
#bridge = CvBridge()
 
def callback(data):
    out = imgmsg_to_cv2(data)
        
   
    cv2.imshow("Image",out)
    cv2.waitKey(1)
    
    
    
def main():
    rospy.init_node('image_sub', anonymous=True)
    rospy.Subscriber('camera/image_raw',Image,callback)
    rospy.spin()
    
        
 
if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()




