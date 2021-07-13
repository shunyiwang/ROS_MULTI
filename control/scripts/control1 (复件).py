#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import time
import subprocess
from std_msgs.msg import String

way=[['3111210','3111210','310','310'],['210','210','110','110'],['4111210','4111210','410','410'],['1121','1121','0','0']]
reway=[['2212320','220','2212420','22120'],['2212320','220','2212420','22120'],['320','120','420','0']]

A1x='7.18476343155'
A1y='9.92148017883'
A1z='-0.664694074842'
A1w='0.74711564491'

A2x='9.14318847656'
A2y='10.0050935745'
A2z='-0.675894487056'
A2w='0.736998400519'

A3x='11.1006660461'
A3y='10.1694965363'
A3z='-0.689228681256'
A3w='0.724543873712'

T1x='7.46755075455'
T1y='13.4293432236'
T1z='0.999971873072'
T1w='0.00750020427963'

T2x='10.6127157211'
T2y='13.5289487839'
T2z='0.016870182639'
T2w='0.999857688343'

T3x='10.9968938828'
T3y='11.4368419647'
T3z='0.719708274802'
T3w='0.69427660135'

T4x='8.07962799072'
T4y='11.4846496582'
T4z='-0.0182607683594'
T4w='0.999833258268'

Axlist=[A1x,A2x,A3x,T4x]
Aylist=[A1y,A2y,A3y,T4y]
Azlist=[A1z,A2z,A3z,T4z]
Awlist=[A1w,A2w,A3w,T4w]

Txlist=[T1x,T2x,T3x,T4x]
Tylist=[T1y,T2y,T3y,T4y]
Tzlist=[T1z,T2z,T3z,T4z]
Twlist=[T1w,T2w,T3w,T4w]

N11x='9.14050769806'
N11y='11.2622289658'
N11z='0.706878673218'
N11w='0.707334815593'

N12x='9.09942913055'
N12y='11.4476442337'
N12z='-0.696207305267'
N12w='0.717840781854'

N21x='9.00552940369'
N21y='13.2619743347'
N21z='0.697704669817'
N21w='0.716385506355'

N22x='8.99278831482'
N22y='13.1605739594'
N22z='-0.691871273668'
N22w='0.72202087274'

N31x='7.24790620804'
N31y='11.2326488495'
N31z='0.0109409243684'
N31w='0.999940146296'

N32x='7.19061422348'
N32y='11.1886053085'
N32z='-0.707810511672'
N32w='0.706402349633'

N41x='10.8994255066'
N41y='11.4274682999'
N41z='0.999813176686'
N41w='-0.0193290383699'

N42x='10.9435272217'
N42y='11.3163661957'
N42z='-0.67073349425'
N42w='0.741698442557'

Nxlist=[[N11x,N12x],[N21x,N22x],[N31x,N32x],[N41x,N42x]]
Nylist=[[N11y,N12y],[N21y,N22y],[N31y,N32y],[N41y,N42y]]
Nzlist=[[N11z,N12z],[N21z,N22z],[N31z,N32z],[N41z,N42z]]
Nwlist=[[N11w,N12w],[N21w,N22w],[N31w,N32w],[N41w,N42w]]

def pub_target(x,y,z,w):
    child = subprocess.Popen("rostopic pub /robot1/move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: \"map\"}, pose: {position: {x: "+x+", y: "+y+"}, orientation: {z: "+z+", w: "+w+"}}}'",shell=True)

def control():
    pub = rospy.Publisher('/robot1/video_command', String, queue_size=10)
    rospy.init_node('video_talker1', anonymous=False)
    while 1:
        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
        STATE.write('0')
        STATE.close()
        TASK=open('/home/tan/ROBOTS/robot1/TASKCAR.txt','r+')
	TASK_NOW=open('/home/tan/ROBOTS/robot1/TASK_NOW.txt','w+')
	#TASK_NOW.write(" TRANS A3 T1 1 2 3\n")
        while 1:
            c=TASK.read(1)
            if c=='':
                break
            if c!='0':    
                TASK.seek(-1,1)
                TASK.write('0')
                break
            c_str=TASK.readline()
        if c=='':
            TASK.close()
            TASK_NOW.close()
            time.sleep(0.2)
            continue
        c_str=TASK.readline()
        c_list=list(c_str)
	TASK_NOW.write(c_str)
        TASK_NOW.close()
        print(c_str)
        i=0
        while 1:
            if c_list[i]!=' ':#
                break
            i=i+1
        if c_list[i]=='T' and c_list[i+1]=='R' and c_list[i+2]=='A' and c_list[i+3]=='N' and c_list[i+4]=='S':#
            i=i+5
            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            if c_list[i]=='A' and c_list[i+1]=='1':#
                start=1
            elif c_list[i]=='A' and c_list[i+1]=='2':
                start=2
            elif c_list[i]=='A' and c_list[i+1]=='3':
                start=3
            i=i+2
            video_str = "10"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('2')
            STATE.close()
            time.sleep(20)
            video_str = "11"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('1')
            STATE.close()

            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            
            if c_list[i]=='T' and c_list[i+1]=='1':#
                target=1
            elif c_list[i]=='T' and c_list[i+1]=='2':
                target=2
            elif c_list[i]=='T' and c_list[i+1]=='3':
                target=3
            elif c_list[i]=='T' and c_list[i+1]=='4':
                target=4
            i=i+2
            #
            waylist=list(way[start-1][target-1])
	    j=0
            while 1:
		if waylist[j]=='0':
		    break
		x=Nxlist[int(waylist[j])-1][int(waylist[j+1])-1]
		y=Nylist[int(waylist[j])-1][int(waylist[j+1])-1]
		z=Nzlist[int(waylist[j])-1][int(waylist[j+1])-1]
		w=Nwlist[int(waylist[j])-1][int(waylist[j+1])-1]
		pub_target(x,y,z,w)
                print('N'+waylist[j])
		j=j+2
                while 1:
                    GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                        x=LOCA.read(7)
               	        y=LOCA.readline()
               	        y=LOCA.read(7)
               	        z=LOCA.readline()
               	        z=LOCA.read(7)
               	        w=LOCA.readline()
               	        w=LOCA.read(7)
                        LOCA.close()
                        pub_target(x,y,z,w)
                        video_str = "30"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            	        STATE.write('6')
            		STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            	        STATE.write('7')
            		STATE.close()
                        TASK.close()
                        exit()
                    time.sleep(0.2)
            x=Txlist[target-1]
            y=Tylist[target-1]
            z=Tzlist[target-1]
            w=Twlist[target-1]
            pub_target(x,y,z,w)
            print('T'+str(target))
            while 1:
                GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                    x=LOCA.read(7)
                    y=LOCA.readline()
         	    y=LOCA.read(7)
               	    z=LOCA.readline()
               	    z=LOCA.read(7)
               	    w=LOCA.readline()
               	    w=LOCA.read(7)
                    LOCA.close()
                    pub_target(x,y,z,w)
                    video_str = "30"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            child = subprocess.Popen("roslaunch multi_navigation rotation_180.launch robot_name:=\"robot1\"",shell=True)
            video_str = "20"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('3')
            STATE.close()
            time.sleep(20)
            video_str = "21"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('0')
            STATE.close()

        elif c_list[i]=='R' and c_list[i+1]=='E' and c_list[i+2]=='T' and c_list[i+3]=='U' and c_list[i+4]=='R' and c_list[i+5]=='N':#
            i=i+6
            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            if c_list[i]=='T' and c_list[i+1]=='1':#
                start=1
                print(T1x+','+T1y)
            elif c_list[i]=='T' and c_list[i+1]=='2':
                start=2
                print(T2x+','+T2y)
            elif c_list[i]=='T' and c_list[i+1]=='3':
                start=3
                print(T3x+','+T3y)
            i=i+2

            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            
            if c_list[i]=='A' and c_list[i+1]=='1':#
                target=1
                print(T1x+','+T1y)
            elif c_list[i]=='A' and c_list[i+1]=='2':
                target=2
                print(T2x+','+T2y)
            elif c_list[i]=='A' and c_list[i+1]=='3':
                target=3
                print(T3x+','+T3y)
            elif c_list[i]=='T' and c_list[i+1]=='4':
                target=4
                print(T4x+','+T4y)
            i=i+2
            #
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('4')
            STATE.close()
            waylist=list(reway[start-1][target-1])
	    j=0
            while 1:
		if waylist[j]=='0':
		    break
		x=Nxlist[int(waylist[j])-1][int(waylist[j+1])-1]
		y=Nylist[int(waylist[j])-1][int(waylist[j+1])-1]
		z=Nzlist[int(waylist[j])-1][int(waylist[j+1])-1]
		w=Nwlist[int(waylist[j])-1][int(waylist[j+1])-1]
		pub_target(x,y,z,w)
                print('N'+waylist[j])
		j=j+2
                while 1:
                    GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                        x=LOCA.read(7)
               	        y=LOCA.readline()
               	        y=LOCA.read(7)
               	        z=LOCA.readline()
               	        z=LOCA.read(7)
               	        w=LOCA.readline()
               	        w=LOCA.read(7)
                        LOCA.close()
                        pub_target(x,y,z,w)
                        video_str = "30"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('7')
                        STATE.close()
                        TASK.close()
                        exit()
                    time.sleep(0.2)
            x=Axlist[target-1]
            y=Aylist[target-1]
            z=Azlist[target-1]
            w=Awlist[target-1]
            pub_target(x,y,z,w)
            print('A'+str(target))
            while 1:
                GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                    x=LOCA.read(7)
                    y=LOCA.readline()
         	    y=LOCA.read(7)
               	    z=LOCA.readline()
               	    z=LOCA.read(7)
               	    w=LOCA.readline()
               	    w=LOCA.read(7)
                    LOCA.close()
                    pub_target(x,y,z,w)
                    video_str = "30"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            child = subprocess.Popen("roslaunch multi_navigation rotation_180.launch robot_name:=\"robot1\"",shell=True)
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('0')
            STATE.close()
            
        elif c_list[i]=='R' and c_list[i+1]=='E' and c_list[i+2]=='S' and c_list[i+3]=='C' and c_list[i+4]=='U' and c_list[i+5]=='E':#
            i=i+6
            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            if c_list[i]=='T' and c_list[i+1]=='1':#
                start=1
                print(T1x+','+T1y)
            elif c_list[i]=='T' and c_list[i+1]=='2':
                start=2
                print(T2x+','+T2y)
            elif c_list[i]=='T' and c_list[i+1]=='3':
                start=3
                print(T3x+','+T3y)
            i=i+2

            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            
            if c_list[i]=='A' and c_list[i+1]=='1':#
                target=1
                print(T1x+','+T1y)
            elif c_list[i]=='A' and c_list[i+1]=='2':
                target=2
                print(T2x+','+T2y)
            elif c_list[i]=='A' and c_list[i+1]=='3':
                target=3
                print(T3x+','+T3y)
            elif c_list[i]=='T' and c_list[i+1]=='4':
                target=4
                print(T4x+','+T4y)
            i=i+2
            #
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('5')
            STATE.close()
            waylist=list(reway[start-1][target-1])
	    j=0
            while 1:
		if waylist[j]=='0':
		    break
		x=Nxlist[int(waylist[j])-1][int(waylist[j+1])-1]
		y=Nylist[int(waylist[j])-1][int(waylist[j+1])-1]
		z=Nzlist[int(waylist[j])-1][int(waylist[j+1])-1]
		w=Nwlist[int(waylist[j])-1][int(waylist[j+1])-1]
		pub_target(x,y,z,w)
                print('N'+waylist[j])
		j=j+2
                while 1:
                    GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                        x=LOCA.read(7)
               	        y=LOCA.readline()
               	        y=LOCA.read(7)
               	        z=LOCA.readline()
               	        z=LOCA.read(7)
               	        w=LOCA.readline()
               	        w=LOCA.read(7)
                        LOCA.close()
                        pub_target(x,y,z,w)
                        video_str = "30"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('7')
                        STATE.close()
                        TASK.close()
                        exit()
                    time.sleep(0.2)
            x=Txlist[target-1]
            y=Tylist[target-1]
            z=Tzlist[target-1]
            w=Twlist[target-1]
            pub_target(x,y,z,w)
            print('T'+str(target))
            while 1:
                GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                    x=LOCA.read(7)
                    y=LOCA.readline()
         	    y=LOCA.read(7)
               	    z=LOCA.readline()
               	    z=LOCA.read(7)
               	    w=LOCA.readline()
               	    w=LOCA.read(7)
                    LOCA.close()
                    pub_target(x,y,z,w)
                    video_str = "30"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            video_str = "50"
	    pub.publish(video_str)
            time.sleep(20)
            video_str = "51"
	    pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('1')
            STATE.close()
            #
	    waylist=list(way[target-1][start-1])
	    j=0
            while 1:
		if waylist[j]=='0':
		    break
		x=Nxlist[int(waylist[j])-1][int(waylist[j+1])-1]
		y=Nylist[int(waylist[j])-1][int(waylist[j+1])-1]
		z=Nzlist[int(waylist[j])-1][int(waylist[j+1])-1]
		w=Nwlist[int(waylist[j])-1][int(waylist[j+1])-1]
		pub_target(x,y,z,w)
                print('N'+waylist[j])
		j=j+2
                while 1:
                    GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                        x=LOCA.read(7)
               	        y=LOCA.readline()
               	        y=LOCA.read(7)
               	        z=LOCA.readline()
               	        z=LOCA.read(7)
               	        w=LOCA.readline()
               	        w=LOCA.read(7)
                        LOCA.close()
                        pub_target(x,y,z,w)
                        video_str = "30"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('7')
                        STATE.close()
                        TASK.close()
                        exit()
                    time.sleep(0.2)
            x=Txlist[start-1]
            y=Tylist[start-1]
            z=Tzlist[start-1]
            w=Twlist[start-1]
            pub_target(x,y,z,w)
            print('T'+str(target))
            while 1:
                GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                    x=LOCA.read(7)
                    y=LOCA.readline()
         	    y=LOCA.read(7)
               	    z=LOCA.readline()
               	    z=LOCA.read(7)
               	    w=LOCA.readline()
               	    w=LOCA.read(7)
                    LOCA.close()
                    pub_target(x,y,z,w)
                    video_str = "30"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            child = subprocess.Popen("roslaunch multi_navigation rotation_180.launch robot_name:=\"robot1\"",shell=True)
            video_str = "20"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('3')
            STATE.close()
            time.sleep(20)
            video_str = "21"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('0')
            STATE.close()

	elif c_list[i]=='B' and c_list[i+1]=='R' and c_list[i+2]=='E' and c_list[i+3]=='A' and c_list[i+4]=='K' and c_list[i+5]=='D' and c_list[i+6]=='O' and c_list[i+7]=='W' and c_list[i+8]=='N' and c_list[i+9]=='1':#
            i=i+10
            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            if c_list[i]=='A' and c_list[i+1]=='1':#
                start=1
                print(T1x+','+T1y)
            elif c_list[i]=='A' and c_list[i+1]=='2':
                start=2
                print(T2x+','+T2y)
            elif c_list[i]=='A' and c_list[i+1]=='3':
                start=3
                print(T3x+','+T3y)
            i=i+2
            video_str = "10"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('2')
            STATE.close()
            time.sleep(20)
            video_str = "11"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('1')
            STATE.close()

            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            
            if c_list[i]=='T' and c_list[i+1]=='1':#
                target=1
                print(T1x+','+T1y)
            elif c_list[i]=='T' and c_list[i+1]=='2':
                target=2
                print(T2x+','+T2y)
            elif c_list[i]=='T' and c_list[i+1]=='3':
                target=3
                print(T3x+','+T3y)
            elif c_list[i]=='T' and c_list[i+1]=='4':
                target=4
                print(T4x+','+T4y)
            i=i+2
            #
            waylist=list(way[start-1][target-1])
	    j=0
            while 1:
		if waylist[j]=='0':
		    break
		x=Nxlist[int(waylist[j])-1][int(waylist[j+1])-1]
		y=Nylist[int(waylist[j])-1][int(waylist[j+1])-1]
		z=Nzlist[int(waylist[j])-1][int(waylist[j+1])-1]
		w=Nwlist[int(waylist[j])-1][int(waylist[j+1])-1]
		pub_target(x,y,z,w)
                print('N'+waylist[j])
		j=j+2
                while 1:
                    GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                        x=LOCA.read(7)
               	        y=LOCA.readline()
               	        y=LOCA.read(7)
               	        z=LOCA.readline()
               	        z=LOCA.read(7)
               	        w=LOCA.readline()
               	        w=LOCA.read(7)
                        LOCA.close()
                        pub_target(x,y,z,w)
                        video_str = "30"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('7')
                        STATE.close()
                        TASK.close()
                        exit()
                    time.sleep(0.2)
            x=Txlist[target-1]
            y=Tylist[target-1]
            z=Tzlist[target-1]
            w=Twlist[target-1]
            pub_target(x,y,z,w)
            print('T'+str(target))
            while 1:
                GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                    x=LOCA.read(7)
                    y=LOCA.readline()
         	    y=LOCA.read(7)
               	    z=LOCA.readline()
               	    z=LOCA.read(7)
               	    w=LOCA.readline()
               	    w=LOCA.read(7)
                    LOCA.close()
                    pub_target(x,y,z,w)
                    video_str = "30"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            video_str = "30"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
            STATE.write('6')
            STATE.close()
            BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
            BREAK.write('1')
            BREAK.close()
            TASK.close()
            exit()

	elif c_list[i]=='B' and c_list[i+1]=='R' and c_list[i+2]=='E' and c_list[i+3]=='A' and c_list[i+4]=='K' and c_list[i+5]=='D' and c_list[i+6]=='O' and c_list[i+7]=='W' and c_list[i+8]=='N' and c_list[i+9]=='2':#
            i=i+10
            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            if c_list[i]=='A' and c_list[i+1]=='1':#
                start=1
                print(T1x+','+T1y)
            elif c_list[i]=='A' and c_list[i+1]=='2':
                start=2
                print(T2x+','+T2y)
            elif c_list[i]=='A' and c_list[i+1]=='3':
                start=3
                print(T3x+','+T3y)
            i=i+2
            video_str = "10"
            pub.publish(video_str)
            time.sleep(20)
            video_str = "11"
            pub.publish(video_str)

            while 1:
                if c_list[i]!=' ':
                    break
                i=i+1
            
            if c_list[i]=='T' and c_list[i+1]=='1':#
                target=1
                print(T1x+','+T1y)
            elif c_list[i]=='T' and c_list[i+1]=='2':
                target=2
                print(T2x+','+T2y)
            elif c_list[i]=='T' and c_list[i+1]=='3':
                target=3
                print(T3x+','+T3y)
            elif c_list[i]=='T' and c_list[i+1]=='4':
                target=4
                print(T4x+','+T4y)
            i=i+2
            #
            waylist=list(way[start-1][target-1])
	    j=0
            while 1:
		if j==0:
		    video_str = "40"
		    pub.publish(video_str)#
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
                    STATE.write('7')
                    STATE.close()
                    BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                    BREAK.write('2')
                    BREAK.close()
		if waylist[j]=='0':
		    break
		x=Nxlist[int(waylist[j])-1][int(waylist[j+1])-1]
		y=Nylist[int(waylist[j])-1][int(waylist[j+1])-1]
		z=Nzlist[int(waylist[j])-1][int(waylist[j+1])-1]
		w=Nwlist[int(waylist[j])-1][int(waylist[j+1])-1]
		pub_target(x,y,z,w)
                print('N'+waylist[j])
		j=j+2
                while 1:
                    GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                        x=LOCA.read(7)
               	        y=LOCA.readline()
               	        y=LOCA.read(7)
               	        z=LOCA.readline()
               	        z=LOCA.read(7)
               	        w=LOCA.readline()
               	        w=LOCA.read(7)
                        LOCA.close()
                        pub_target(x,y,z,w)
                        video_str = "30"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	        STATE.write('7')
                        STATE.close()
                        TASK.close()
                        exit()
                    time.sleep(0.2)
            x=Txlist[target-1]
            y=Tylist[target-1]
            z=Tzlist[target-1]
            w=Twlist[target-1]
            pub_target(x,y,z,w)
            print('T'+str(target))
            while 1:
                GOAL=open('/home/tan/ROBOTS/robot1/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot1/location.txt','r+') #wenjian
                    x=LOCA.read(7)
                    y=LOCA.readline()
         	    y=LOCA.read(7)
               	    z=LOCA.readline()
               	    z=LOCA.read(7)
               	    w=LOCA.readline()
               	    w=LOCA.read(7)
                    LOCA.close()
                    pub_target(x,y,z,w)
                    video_str = "30"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot1/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            TASK.close()
            exit()
        TASK.close()
        time.sleep(0.2)


if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
