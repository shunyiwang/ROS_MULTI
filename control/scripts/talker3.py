#!/usr/bin/env python
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


t0=-1
def callback(msg):
    global t0
    t0=rospy.get_time()
    if msg.status.text =="Goal reached.":
    	rospy.loginfo(rospy.get_caller_id() + ' I heard %s normal', msg.status.text)
    else:
    	rospy.loginfo(rospy.get_caller_id() + ' I heard %s error', msg.status.text)

def callback2(data):
    global t0
    t0=rospy.get_time()
    if data.data =="0":
    	rospy.loginfo(rospy.get_caller_id() + ' I heard %s normal', data.data)
    else:
    	rospy.loginfo(rospy.get_caller_id() + ' I heard %s error', data.data)
    time.sleep(5)


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/robot2/move_base/result', MoveBaseActionResult, callback)
    rospy.Subscriber('chatter0', String, callback2)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    child = subprocess.Popen('./ndnputchunks3 /c1/'+str3+' <'+str3+".avi"  ,shell=True)


if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:
        pass




