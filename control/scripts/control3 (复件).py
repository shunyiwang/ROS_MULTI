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

A1x='9.0746421814'
A1y='9.94549751282'
A1z='0.671979283936'
A1w='0.740569944004'

A2x='11.2407026291'
A2y='9.89167976379'
A2z='0.671979283936'
A2w='0.740569944004'

A3x='13.3221769333'
A3y='9.97048091888'
A3z='0.671979283936'
A3w='0.740569944004'

T1x='8.97227287292'
T1y='13.326795578'
T1z='-0.00428849587124'
T1w='0.999990804359'

T2x='13.1838998795'
T2y='13.4910173416'
T2z='0.996529988307'
T2w='-0.0832345024848'

T3x='13.363483429'
T3y='11.5204906464'
T3z='0.36877589371'
T3w='0.929518337753'

X1x='10.045372963'
X1y='11.5094490051'
X1z='-0.000435545052007'
X1w='0.99999990515'

X2x='10.4381313324'
X2y='11.4597663879'
X2z='0.00163211151043'
X2w='0.999998668105'


Axlist=[A1x,A2x,A3x,X2x]
Aylist=[A1y,A2y,A3y,X2y]
Azlist=[A1z,A2z,A3z,X2z]
Awlist=[A1w,A2w,A3w,X2w]

Txlist=[T1x,T2x,T3x,X1x]
Tylist=[T1y,T2y,T3y,X1y]
Tzlist=[T1z,T2z,T3z,X1z]
Twlist=[T1w,T2w,T3w,X1w]

N11x='11.289059639'
N11y='11.231139183'
N11z='0.706878673218'
N11w='0.696603487253'

N12x='11.2516889572'
N12y='11.1401977539'
N12z='-0.688800895809'
N12w='0.724950567924'

N21x='11.1138181686'
N21y='13.5977745056'
N21z='0.702959780085'
N21w='0.711229602578'

N22x='11.2688550949'
N22y='13.4387168884'
N22z='-0.701783744781'
N22w='0.712390044541'

N31x='9.24890708923'
N31y='11.2392702103'
N31z='0.112249316798'
N31w='0.993680074711'

N32x='9.27569293976'
N32y='11.175113678'
N32z='-0.793809477465'
N32w='0.608166517894'

N41x='13.1991558075'
N41y='11.285615921'
N41z='0.994572082655'
N41w='0.104049855372'

N42x='13.1733388901'
N42y='11.2852287292'
N42z='-0.551478953883'
N42w='0.834188805621'

Nxlist=[[N11x,N12x],[N21x,N22x],[N31x,N32x],[N41x,N42x]]
Nylist=[[N11y,N12y],[N21y,N22y],[N31y,N32y],[N41y,N42y]]
Nzlist=[[N11z,N12z],[N21z,N22z],[N31z,N32z],[N41z,N42z]]
Nwlist=[[N11w,N12w],[N21w,N22w],[N31w,N32w],[N41w,N42w]]

def pub_target(x,y,z,w):
    child = subprocess.Popen("rostopic pub /robot3/move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: \"map\"}, pose: {position: {x: "+x+", y: "+y+"}, orientation: {z: "+z+", w: "+w+"}}}'",shell=True)

def control():
    pub = rospy.Publisher('/robot3/video_command', String, queue_size=10)
    rospy.init_node('video_talker_robot3', anonymous=False)
    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
    STATE.write('0')
    STATE.close()
    GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','w+')
    GOAL.write('0')
    GOAL.close()
    BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','w+')
    BREAK.write('0')
    BREAK.close()
    TASK=open('/home/tan/ROBOTS/robot3/TASKCAR.txt','w+')
    TASK.close()
    while 1:
        TASK=open('/home/tan/ROBOTS/robot3/TASKCAR.txt','r+')
	TASK_NOW=open('/home/tan/ROBOTS/robot3/TASK_NOW.txt','w+')
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
        c_list=c_str.split()
	TASK_NOW.write(c_str)
        TASK_NOW.close()
        print(c_str)
        i=0
        if c_list[i]=='TRANS':#
            i=i+1
            if c_list[i]=='A1':#
                start=1
            elif c_list[i]=='A2':
                start=2
            elif c_list[i]=='A3':
                start=3
            elif c_list[i]=='X1':
                start=4
            i=i+1            
            if c_list[i]=='T1':#
                target=1
            elif c_list[i]=='T2':
                target=2
            elif c_list[i]=='T3':
                target=3
            elif c_list[i]=='X1':
                target=4
            i=i+1
            video_str = "10"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('2')
            STATE.close()
            time.sleep(20)
	    if start==1 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
	    elif start==2 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
	    elif start==3 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
            video_str = "11"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('1')
            STATE.close()
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
                    GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            	        STATE.write('6')
            		STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
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
                GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            video_str = "20"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('3')
            STATE.close()
            time.sleep(20)
	    if target==1 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
	    elif target==2 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
	    elif target==3 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
            video_str = "21"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('0')
            STATE.close()

        elif c_list[i]=='RETURN':#
            i=i+1
            if c_list[i]=='T1':#
                start=1
            elif c_list[i]=='T2':
                start=2
            elif c_list[i]=='T3':
                start=3
            i=i+1
            if c_list[i]=='A1':#
                target=1
            elif c_list[i]=='A2':
                target=2
            elif c_list[i]=='A3':
                target=3
            elif c_list[i]=='X1':
                target=4
            i=i+1
            #
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
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
                    GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
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
                GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('0')
            STATE.close()
            
        elif c_list[i]=='RESCUE':#
            i=i+1
            if c_list[i]=='A1':#
                start=1
            elif c_list[i]=='A2':
                start=2
            elif c_list[i]=='A3':
                start=3
            elif c_list[i]=='X1':
                start=4
            i=i+1            
            if c_list[i]=='T1':#
                target=1
            elif c_list[i]=='T2':
                target=2
            elif c_list[i]=='T3':
                target=3
            elif c_list[i]=='X1':
                target=4
            i=i+1
            video_str = "50"
	    pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('5')
            STATE.close()
            time.sleep(20)
            video_str = "11"
	    pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('1')
            STATE.close()
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
                    GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
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
                GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            video_str = "20"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('3')
            STATE.close()
            time.sleep(20)
	    if target==1 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
	    elif target==2 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
	    elif target==3 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
            video_str = "21"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('0')
            STATE.close()

	elif c_list[i]=='BREAKDOWN1':#
            i=i+1
            if c_list[i]=='A1':#
                start=1
            elif c_list[i]=='A2':
                start=2
            elif c_list[i]=='A3':
                start=3
            elif c_list[i]=='X1':
                start=4
            i=i+1            
            if c_list[i]=='T1':#
                target=1
            elif c_list[i]=='T2':
                target=2
            elif c_list[i]=='T3':
                target=3
            elif c_list[i]=='X1':
                target=4
            i=i+1
            video_str = "10"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('2')
            STATE.close()
            time.sleep(20)
	    if start==1 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
	    elif start==2 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
	    elif start==3 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
            video_str = "11"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('1')
            STATE.close()
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
                    GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	        STATE.write('6')
                        STATE.close()
                        TASK.close()
                        exit()
                    elif Breakdown=='2' :
                        video_str = "40"
                        pub.publish(video_str)
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
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
                GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                elif Breakdown=='2' :
                    video_str = "40"
                    pub.publish(video_str)
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('7')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
            video_str = "30"
            pub.publish(video_str)#
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('6')
            STATE.close()
            BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','w+')
            BREAK.write('1')
            BREAK.close()
	    EMERGENCY=open('/home/tan/ROBOTS/robot1/TASKCAR.txt','r+')
	    e=EMERGENCY.read()
	    EMERGENCY.write('4 RETURN T2 X1 0 0 0\n')
	    p1=c_list[i]
	    p2=c_list[i+1]
	    p3=c_list[i+2]
	    EMERGENCY.write('5 RESCUE X1 T3 '+p1+' '+p2+' '+p3+'\n')
	    EMERGENCY.close()
            TASK.close()
            exit()

	elif c_list[i]=='BREAKDOWN2':#
            i=i+1
            if c_list[i]=='A1':#
                start=1
            elif c_list[i]=='A2':
                start=2
            elif c_list[i]=='A3':
                start=3
            elif c_list[i]=='X1':
                start=4
            i=i+1            
            if c_list[i]=='T1':#
                target=1
            elif c_list[i]=='T2':
                target=2
            elif c_list[i]=='T3':
                target=3
            elif c_list[i]=='X1':
                target=4
            i=i+1
            video_str = "10"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('2')
            STATE.close()
            time.sleep(20)
	    if start==1 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
	    elif start==2 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
	    elif start==3 :
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','w+')
		GOODS.write(str(int(P_list[0])-int(c_list[i]))+' '+str(int(P_list[1])-int(c_list[i+1]))+' '+str(int(P_list[2])-int(c_list[i+2])))
		GOODS.close()
            video_str = "11"
            pub.publish(video_str)
            STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
            STATE.write('1')
            STATE.close()
            #
            waylist=list(way[start-1][target-1])
	    j=0
            while 1:
		if j==0:
		    video_str = "40"
		    pub.publish(video_str)#
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
                    STATE.write('7')
                    STATE.close()
                    BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','w+')
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
                    GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                    Goal_reached=GOAL.read(1)
                    if Goal_reached=='1':
                        GOAL.seek(-1,1)
                        GOAL.write('0')
                        GOAL.close()
                        break
                    GOAL.close()
                    BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                    Breakdown=BREAK.read(1)
                    BREAK.close()
                    if Breakdown=='1': #
                        LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                        STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	        STATE.write('6')
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
                GOAL=open('/home/tan/ROBOTS/robot3/goal_reached.txt','r+')
                Goal_reached=GOAL.read(1)
                if Goal_reached=='1':
                    GOAL.seek(-1,1)
                    GOAL.write('0')
                    GOAL.close()
                    break
                GOAL.close()
                BREAK=open('/home/tan/ROBOTS/robot3/BREAKDOWN.txt','r+')
                Breakdown=BREAK.read(1)
                BREAK.close()
                if Breakdown=='1': #
                    LOCA=open('/home/tan/ROBOTS/robot3/location.txt','r+') #wenjian
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
                    STATE=open('/home/tan/ROBOTS/robot3/STATE.txt','w+')
         	    STATE.write('6')
                    STATE.close()
                    TASK.close()
                    exit()
                time.sleep(0.2)
	    if target==1 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
	    elif target==2 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
	    elif target==3 :
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','r+')
		P_str=GOODS.read()
		P_list=P_str.split()
		GOODS.close()
		GOODS=open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','w+')
		GOODS.write(str(int(P_list[0])+int(c_list[i]))+' '+str(int(P_list[1])+int(c_list[i+1]))+' '+str(int(P_list[2])+int(c_list[i+2])))
		GOODS.close()
            TASK.close()
            exit()
        TASK.close()
        time.sleep(0.2)


if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
