#!/usr/bin/env python
#!coding=utf-8
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import cv2
from notcv_bridge import *
import numpy as np
import sys
config_file= '/home/ros/tf_ws/src/obj_det/scripts/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model= '/home/ros/tf_ws/src/obj_det/scripts/frozen_inference_graph.pb'
file_name="/home/ros/tf_ws/src/obj_det/scripts/Labels.txt"
def image_pub():
    rospy.init_node('image_pub', anonymous=True)
    pub = rospy.Publisher('camera/image_raw', Image, queue_size=2)
    rate = rospy.Rate(10)
    font_scale=3
    font=cv2.FONT_HERSHEY_PLAIN
    classLabels=[]
    with open(file_name,'rt') as fpt:
        classLabels=fpt.read().rstrip('\n').split('\n')
    model= cv2.dnn_DetectionModel(frozen_model,config_file)
    model.setInputSize(320,320)
    model.setInputScale(1.0/127.5)
    model.setInputMean((127.5,127.5,127.5))
    model.setInputSwapRB(True)
    cap = cv2.VideoCapture('/home/ros/tf_ws/src/obj_det/scripts/people.mp4')
    #bridge = CvBridge()
 
    if not cap.isOpened():
        sys.stdout.write("Camera/video is failed to use!")
 
    count = 0
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            #frame = cv2.resize(frame,(640,480))
            print(type(frame))
            ClassIndex,confidence,bbox=model.detect(frame,confThreshold=0.6)
            if (len(ClassIndex)!=0):
                for ClassInd,conf,boxes in zip(ClassIndex.flatten(),confidence.flatten(),bbox):
                    if (ClassInd<=80):
                        cv2.rectangle(frame,boxes,(255,0,0),2)
                        cv2.putText(frame,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40),font,fontScale=font_scale,color=(0,255,0),thickness=3)
 
            
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




