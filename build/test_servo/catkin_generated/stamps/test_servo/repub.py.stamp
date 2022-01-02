#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 	B. Burak Payzun
# Date: 	2021-08-27
#
###########################

import rospy
import getch
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Header, Float64MultiArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

pub = 0
def callback(data):
	angles = data.data	
	msg = JointTrajectory()
	msg.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6"]
	
	pts = JointTrajectoryPoint()
	pts.positions = angles
	pts.time_from_start = rospy.Duration.from_sec(0.005)

	msg.points.append(pts)
	
	pub.publish(msg) # publish arm positions

rospy.init_node("command_republisher")

sub = rospy.Subscriber('/arm_controller/command', Float64MultiArray, callback)
pub = rospy.Publisher('/rover_arm_controller/command', JointTrajectory, queue_size=10)
rospy.spin()
