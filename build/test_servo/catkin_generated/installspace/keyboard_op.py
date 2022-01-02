#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Author: 	B. Burak Payzun
# Date: 	2021-08-27
#
###########################

import rospy
import getch
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Header

rospy.init_node("joystick_op")

publisher = rospy.Publisher('/servo_server/delta_twist_cmds', TwistStamped, queue_size = 10)

rate = rospy.Rate(20)

while not rospy.is_shutdown():
	print(joy_msg)
	msg = TwistStamped()
	msg.header = Header()
	msg.header.stamp = rospy.Time.now()
	print(rospy.Time.now())
	msg.twist.linear.x = 0
	msg.twist.linear.y = 0
	msg.twist.linear.z = 0
	msg.twist.angular.x = 0
	msg.twist.angular.y = 0
	msg.twist.angular.z = 0
	user_input = getch.getch().encode()
	if user_input == 'd':
		msg.twist.linear.y = 1
		print("Move Right")
	elif user_input == 'a':
		msg.twist.linear.y = -1
		print("Move Left")
	elif user_input == 'w':
		msg.twist.linear.x = -1
		print("Move Forward")
	elif user_input == 's':
		msg.twist.linear.x = 1
		print("Move Backward")
	elif user_input == 'e':
		msg.twist.linear.z = 1
		print("Move Up")
	elif user_input == 'c':
		msg.twist.linear.z = -1
		print("Move Down")
	print(msg)
	publisher.publish(msg)
