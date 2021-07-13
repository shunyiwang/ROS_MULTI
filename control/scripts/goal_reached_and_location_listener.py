#!/usr/bin/env python
#coding=utf-8
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
import threading

import time
from std_msgs.msg import String
from move_base_msgs.msg import *
from geometry_msgs.msg import PoseWithCovarianceStamped,PoseStamped

def PoseCallBack1(msg):
	data1=""
	#订阅到的坐标信息
	x1 = msg.pose.pose.position.x
	y1 = msg.pose.pose.position.y
	#订阅到的四元数的信息，用来表示朝向
	orien_z1 = msg.pose.pose.orientation.z
	orien_w1 = msg.pose.pose.orientation.w
	
	#data1 = str(x1) + "," + str(y1)+ "," + str(orien_z1)+ "," + str(orien_w1)
        F01=open('/home/tan/ROBOTS/robot1/location.txt','w+') #wenjian
        data1 = str(x1)+'\n'
        F01.write(data1)
        data1 = str(y1)+'\n'
        F01.write(data1)
        data1 = str(orien_z1)+'\n'
        F01.write(data1)
        data1 = str(orien_w1)
        F01.write(data1)
        F01.close()
def PoseCallBack2(msg):
	data2=""
	#订阅到的坐标信息
	x2 = msg.pose.pose.position.x
	y2 = msg.pose.pose.position.y
	#订阅到的四元数的信息，用来表示朝向
	orien_z2 = msg.pose.pose.orientation.z
	orien_w2 = msg.pose.pose.orientation.w
	
	#data2 = str(x2) + "," + str(y2)+ "," + str(orien_z2)+ "," + str(orien_w2)
        F02=open('/home/tan/ROBOTS/robot2/location.txt','w+') #wenjian
        data2 = str(x2)+'\n'
        F02.write(data2)
        data2 = str(y2)+'\n'
        F02.write(data2)
        data2 = str(orien_z2)+'\n'
        F02.write(data2)
        data2 = str(orien_w2)
        F02.write(data2)
        F02.close()
def PoseCallBack3(msg):
	data3=""
	#订阅到的坐标信息
	x3 = msg.pose.pose.position.x
	y3 = msg.pose.pose.position.y
	#订阅到的四元数的信息，用来表示朝向
	orien_z3 = msg.pose.pose.orientation.z
	orien_w3 = msg.pose.pose.orientation.w
	
	#data3 = str(x3) + "," + str(y3)+ "," + str(orien_z3)+ "," + str(orien_w3)
        F03=open('/home/tan/ROBOTS/robot3/location.txt','w+') #wenjian
        data3 = str(x3) +'\n'
        F03.write(data3)
        data3 = str(y3) +'\n'
        F03.write(data3)
        data3 = str(orien_z3) +'\n'
        F03.write(data3)
        data3 = str(orien_w3)
        F03.write(data3)
        F03.close()
def PoseCallBack4(msg):
	data4=""
	#订阅到的坐标信息
	x4 = msg.pose.pose.position.x
	y4 = msg.pose.pose.position.y
	#订阅到的四元数的信息，用来表示朝向
	orien_z4 = msg.pose.pose.orientation.z
	orien_w4 = msg.pose.pose.orientation.w
	
	#data4 = str(x4) + "," + str(y4)+ "," + str(orien_z4)+ "," + str(orien_w4)
        F04=open('/home/tan/ROBOTS/robot4/location.txt','w+') #wenjian
        data4 = str(x4) + '\n'
        F04.write(data4)
        data4 = str(y4) + '\n'
        F04.write(data4)
        data4 = str(orien_z4) + '\n'
        F04.write(data4)
        data4 = str(orien_w4)
        F04.write(data4)
        F04.close()
def PoseCallBack5(msg):
	data5=""
	#订阅到的坐标信息
	x5 = msg.pose.pose.position.x
	y5 = msg.pose.pose.position.y
	#订阅到的四元数的信息，用来表示朝向
	orien_z5 = msg.pose.pose.orientation.z
	orien_w5 = msg.pose.pose.orientation.w
	
	#data5 = str(x5) + "," + str(y5)+ "," + str(orien_z5)+ "," + str(orien_w5)
        F05=open('/home/tan/ROBOTS/robot5/location.txt','w+') #wenjian
        data5 = str(x5) +'\n'
        F05.write(data5)
        data5 = str(y5) +'\n'
        F05.write(data5)
        data5 = str(orien_z5) +'\n'
        F05.write(data5)
        data5 = str(orien_w5)
        F05.write(data5)
        F05.close()

def callback1(msg):
    robot1_Goal_reached='0'
    if msg.status.text =="Goal reached.":
    	robot1_Goal_reached='1'
    else:
    	robot1_Goal_reached='0'
    F1=open('/home/tan/ROBOTS/robot1/goal_reached.txt','w+') #wenjian
    F1.write(robot1_Goal_reached)
    F1.close()
def callback2(msg):
    robot2_Goal_reached='0'
    if msg.status.text =="Goal reached.":
    	robot2_Goal_reached='1'
    else:
    	robot2_Goal_reached='0'
    F2=open('/home/tan/ROBOTS/robot2/goal_reached.txt','w+') #wenjian
    F2.write(robot2_Goal_reached)
    F2.close()
def callback3(msg):
    robot3_Goal_reached='0'
    if msg.status.text =="Goal reached.":
    	robot3_Goal_reached='1'
    else:
    	robot3_Goal_reached='0'
    F3=open('/home/tan/ROBOTS/robot3/goal_reached.txt','w+') #wenjian
    F3.write(robot3_Goal_reached)
    F3.close()
def callback4(msg):
    robot4_Goal_reached='0'
    if msg.status.text =="Goal reached.":
    	robot4_Goal_reached='1'
    else:
    	robot4_Goal_reached='0'
    F4=open('/home/tan/ROBOTS/robot4/goal_reached.txt','w+') #wenjian
    F4.write(robot4_Goal_reached)
    F4.close()
def callback5(msg):
    robot5_Goal_reached='0'
    if msg.status.text =="Goal reached.":
    	robot5_Goal_reached='1'
    else:
    	robot5_Goal_reached='0'
    F5=open('/home/tan/ROBOTS/robot5/goal_reached.txt','w+') #wenjian
    F5.write(robot5_Goal_reached)
    F5.close()

def callback_b1(data):
    if data.data !="":
	tb1=float(data.data)
        Fb1=open('/home/tan/TIME/BW/receive1','w+') #wenjian
        Fb1.write(str(tb1))
        Fb1.close()
	Fb1=open('/home/tan/TIME/BW/send','r+') #wenjian
        tb10=Fb1.read()
        Fb1.close()
	if tb10=='':
	    tb10='0'
	tb10=tb10.split()
	tb10=tb10[0]
	tb10=float(tb10)
        tb1=tb1-tb10
        Fb1=open('/home/tan/TIME/BW/sub1','w+') #wenjian
        Fb1.write(str(tb1))
        Fb1.close()

def callback_b2(data):
    if data.data !="":
	tb2=float(data.data)
        Fb2=open('/home/tan/TIME/BW/receive2','w+') #wenjian
        Fb2.write(str(tb2))
        Fb2.close()
	Fb2=open('/home/tan/TIME/BW/send','r+') #wenjian
        tb20=Fb2.read()
        Fb2.close()
	if tb20=='':
	    tb20='0'
	tb20=tb20.split()
	tb20=tb20[0]
	tb20=float(tb20)
        tb2=tb2-tb20
        Fb2=open('/home/tan/TIME/BW/sub2','w+') #wenjian
        Fb2.write(str(tb2))
        Fb2.close()

def callback_b3(data):
    if data.data !="":
	tb3=float(data.data)
        Fb3=open('/home/tan/TIME/BW/receive3','w+') #wenjian
        Fb3.write(str(tb3))
        Fb3.close()
	Fb3=open('/home/tan/TIME/BW/send','r+') #wenjian
        tb30=Fb3.read()
        Fb3.close()
	if tb30=='':
	    tb30='0'
	tb30=tb30.split()
	tb30=tb30[0]
	tb30=float(tb30)
        tb3=tb3-tb30
        Fb3=open('/home/tan/TIME/BW/sub3','w+') #wenjian
        Fb3.write(str(tb3))
        Fb3.close()

def callback_b4(data):
    if data.data !="":
	tb4=float(data.data)
        Fb4=open('/home/tan/TIME/BW/receive4','w+') #wenjian
        Fb4.write(str(tb4))
        Fb4.close()
	Fb4=open('/home/tan/TIME/BW/send','r+') #wenjian
        tb40=Fb4.read()
        Fb4.close()
	if tb40=='':
	    tb40='0'
	tb40=tb40.split()
	tb40=tb40[0]
	tb40=float(tb40)
        tb4=tb4-tb40
        Fb4=open('/home/tan/TIME/BW/sub4','w+') #wenjian
        Fb4.write(str(tb4))
        Fb4.close()

def callback_r1(data):
    if data.data !="":
	tr1=float(data.data)
        Fr1=open('/home/tan/TIME/RE/receive1','w+') #wenjian
        Fr1.write(str(tr1))
        Fr1.close()
	Fr1=open('/home/tan/TIME/RE/send','r+') #wenjian
        tr10=Fr1.read()
        Fr1.close()
	if tr10=='':
	    tr10='0'
	tr10=tr10.split()
	tr10=tr10[0]
	tr10=float(tr10)
        tr1=tr1-tr10
        Fr1=open('/home/tan/TIME/RE/sub1','w+') #wenjian
        Fr1.write(str(tr1))
        Fr1.close()

def callback_r2(data):
    if data.data !="":
	tr2=float(data.data)
        Fr2=open('/home/tan/TIME/RE/receive2','w+') #wenjian
        Fr2.write(str(tr2))
        Fr2.close()
	Fr2=open('/home/tan/TIME/RE/send','r+') #wenjian
        tr20=Fr2.read()
        Fr2.close()
	if tr20=='':
	    tr20='0'
	tr20=tr20.split()
	tr20=tr20[0]
	tr20=float(tr20)
        tr2=tr2-tr20
        Fr2=open('/home/tan/TIME/RE/sub2','w+') #wenjian
        Fr2.write(str(tr2))
        Fr2.close()

def callback_r3(data):
    if data.data !="":
	tr3=float(data.data)
        Fr3=open('/home/tan/TIME/RE/receive3','w+') #wenjian
        Fr3.write(str(tr3))
        Fr3.close()
	Fr3=open('/home/tan/TIME/RE/send','r+') #wenjian
        tr30=Fr3.read()
        Fr3.close()
	if tr30=='':
	    tr30='0'
	tr30=tr30.split()
	tr30=tr30[0]
	tr30=float(tr30)
        tr3=tr3-tr30
        Fr3=open('/home/tan/TIME/RE/sub3','w+') #wenjian
        Fr3.write(str(tr3))
        Fr3.close()

def callback_r4(data):
    if data.data !="":
	tr4=float(data.data)
        Fr4=open('/home/tan/TIME/RE/receive4','w+') #wenjian
        Fr4.write(str(tr4))
        Fr4.close()
	Fr4=open('/home/tan/TIME/RE/send','r+') #wenjian
        tr40=Fr4.read()
        Fr4.close()
	if tr40=='':
	    tr40='0'
	tr40=tr40.split()
	tr40=tr40[0]
	tr40=float(tr40)
        tr4=tr4-tr40
        Fr4=open('/home/tan/TIME/RE/sub4','w+') #wenjian
        Fr4.write(str(tr4))
        Fr4.close()

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    F=open('/home/tan/TIME/BW/send','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/send','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/receive1','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/receive2','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/receive3','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/receive4','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/sub1','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/sub2','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/sub3','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/BW/sub4','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/receive1','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/receive2','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/receive3','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/receive4','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/sub1','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/sub2','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/sub3','w+') #wenjian
    F.close()
    F=open('/home/tan/TIME/RE/sub4','w+') #wenjian
    F.close()
    rospy.init_node('goal_reached_and_location_listener', anonymous=False)

    rospy.Subscriber('/robot1/move_base/result', MoveBaseActionResult, callback1)
    rospy.Subscriber('/robot2/move_base/result', MoveBaseActionResult, callback2)
    rospy.Subscriber('/robot3/move_base/result', MoveBaseActionResult, callback3)
    rospy.Subscriber('/robot4/move_base/result', MoveBaseActionResult, callback4)
    rospy.Subscriber('/robot5/move_base/result', MoveBaseActionResult, callback5)

    rospy.Subscriber('/robot1/amcl_pose',PoseWithCovarianceStamped,PoseCallBack1)
    rospy.Subscriber('/robot2/amcl_pose',PoseWithCovarianceStamped,PoseCallBack2)
    rospy.Subscriber('/robot3/amcl_pose',PoseWithCovarianceStamped,PoseCallBack3)
    rospy.Subscriber('/robot4/amcl_pose',PoseWithCovarianceStamped,PoseCallBack4)
    rospy.Subscriber('/robot5/amcl_pose',PoseWithCovarianceStamped,PoseCallBack5)

    rospy.Subscriber('/robot1/bandwidth_feedback', String, callback_b1)
    rospy.Subscriber('/robot2/bandwidth_feedback', String, callback_b2)
    rospy.Subscriber('/robot3/bandwidth_feedback', String, callback_b3)
    rospy.Subscriber('/robot4/bandwidth_feedback', String, callback_b4)

    rospy.Subscriber('/robot1/response_feedback', String, callback_r1)
    rospy.Subscriber('/robot2/response_feedback', String, callback_r2)
    rospy.Subscriber('/robot3/response_feedback', String, callback_r3)
    rospy.Subscriber('/robot4/response_feedback', String, callback_r4)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:
        pass




