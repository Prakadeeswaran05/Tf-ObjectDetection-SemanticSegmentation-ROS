#!/usr/bin/env python
#!coding=utf-8
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import cv2
from notcv_bridge import *
import numpy as np
import sys
def image_pub():
    rospy.init_node('image_pub', anonymous=True)
    pub = rospy.Publisher('camera/image_raw', Image, queue_size=2)
    rate = rospy.Rate(5)
    cap = cv2.VideoCapture('/home/ros/tf_ws/src/obj_det/scripts/people.mp4')
    #bridge = CvBridge()
    if not cap.isOpened():
        sys.stdout.write("Camera/video is failed to use!")
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            img_msg =cv2_to_imgmsg(frame)
            pub.publish(img_msg)
            print("Publishing image now..")
        else:
            rospy.loginfo("Capturing image failed.")
        rate.sleep()
 
 
if __name__ == '__main__':
    try:
        image_pub()
        #rospy.spin()
    except rospy.ROSInterruptException:
        pass




