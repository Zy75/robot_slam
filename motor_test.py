#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

def callback(data):

    LR = data.axes[0]
    FR = data.axes[1]

    print "LR"

def listener():
 
    rospy.init_node('motor_out', anonymous=True)

    rospy.Subscriber('joy', Joy, callback)

    rospy.spin()

if __name__ == '__main__':
    print "start******"
    listener()
