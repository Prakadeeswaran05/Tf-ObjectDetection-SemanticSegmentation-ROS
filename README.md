# Simple-Tf-ObjectDetection-ROS

## Dependencies

Create a virtual environment<br/>
```virtualenv --system-site-packages detection -p python3 ```<br/>
Activate the environment <br/>
``` source detection/bin/activate ``` <br/>
Install opencv <br/>
```  pip install opencv-contrib-python ```<br/>
Create workspace<br/>
```mkdir tf_ws```<br/>
```cd tf_ws/```<br/>
```mkdir src```<br/>
```catkin_make```<br/>
```cd src/```<br/>

Create package<br/>
```catkin_create_pkg obj_det rospy roscpp std_msgs geometry_msgs sensor_msgs cv_bridge image_transport```<br/>




Go inside src folder and create a scripts folder and inside scripts folder paste all the files in my repo<br/>
Now open new terminal and type<br/>

```roscore```<br/>
In the previous terminal<br/>
```python image_publisher_tf_detect.py``` <br/>

In another new terminal<br/>
```python image_subscriber_tf.py``` <br/>






## Output
















<p align="left">
  <img src="obj_detect.gif" />
</p>



