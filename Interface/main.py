# -*- coding: utf-8 -*-
import sys
import rospy
import threading
import subprocess
from std_msgs.msg import String
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QPalette,QBrush
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import time
import pra0911

cars_task = ["trans","return","rescue"]
cars_state = ["空闲","运输","装货","卸货","返回","救援","机械故障","通信故障"]
cars_error = ["正常","机械故障","通信故障"]
#find "pra0911.py" | xargs sed -i 's/PlaceholderText/Text/g'
#  x 520~1171  y 20~701 
T1P1 = 0; T1P2 = 0; T1P3 = 0
T2P1 = 0; T2P2 = 0; T2P3 = 0
T3P1 = 0; T3P2 = 0; T3P3 = 0

def convert(ui): #得到输入，进行计算，得到并显示输出
    #A1点的p1p2p3三种货物
    A1P1 = ui.lineEdit.text();A1P2 = ui.lineEdit_2.text();A1P3 = ui.lineEdit_3.text()
    # A2点的p1p2p3三种货物
    A2P1 = ui.lineEdit_5.text();A2P2 = ui.lineEdit_6.text();A2P3 = ui.lineEdit_7.text()
    # A3点的p1p2p3三种货物
    A3P1 = ui.lineEdit_8.text();A3P2 = ui.lineEdit_9.text();A3P3 = ui.lineEdit_10.text()
    # 任务点T1的p1p2p3三种货物
    T1P1 = ui.lineEdit_11.text();T1P2 = ui.lineEdit_12.text();T1P3 = ui.lineEdit_13.text()
    # 任务点T2的p1p2p3三种货物 #这里给师兄的源码有误，应该是T2而不是T1
    T2P1 = ui.lineEdit_14.text();T2P2 = ui.lineEdit_15.text();T2P3 = ui.lineEdit_16.text()
    # 三个任务点的最晚完成时间
    time1 = ui.lineEdit_20.text();time2 = ui.lineEdit_21.text();time3 = ui.lineEdit_22.text()

    #将物资量写入集结点文件
    wuzilist1 = [A1P1 + ' ' + A1P2 + ' ' + A1P3]
    WUZI1=open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','w+')
    WUZI1.writelines(wuzilist1)
    WUZI1.close()

    wuzilist2 = [A2P1 + ' ' + A2P2 + ' ' + A2P3]
    WUZI2=open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','w+')
    WUZI2.writelines(wuzilist2)
    WUZI2.close()

    wuzilist3 = [A3P1 + ' ' + A3P2 + ' ' + A3P3]
    WUZI3=open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','w+')
    WUZI3.writelines(wuzilist3)
    WUZI3.close()

def add_T3():
# 通过checkbox判断是否有新增任务，若有，则读入任务点T3
    if ui.checkBox.isChecked() == True :  #判断checkbox是否勾选，若勾选了，则读入T3的数据
        T3P1 = ui.lineEdit_17.text();T3P2 = ui.lineEdit_18.text();T3P3 = ui.lineEdit_19.text()
        maptask3 = QPixmap("任务点3.jpg")
        ui.label_22.setPixmap(maptask3)  # 将任务点3图像放在label里
        ui.label_22.setScaledContents(True) #自动调整图像大小以适应label
	ui.lineEdit_38.setStyleSheet("background:transparent;border-width:1")
    	ui.lineEdit_39.setStyleSheet("background:transparent;border-width:1")
    	ui.lineEdit_40.setStyleSheet("background:transparent;border-width:1")

def show_T3():#此函数只执行显示T3物资量的功能，无输入输出
	#读入并输出T3的物资量
	taskpoint3 = open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','r+')
	tasklist3 = taskpoint3.read()
	tasklist3 = tasklist3.split()
	taskpoint3.close()
	if tasklist3 != '':
        	ui.lineEdit_39.setText(tasklist3[0])
		ui.lineEdit_38.setText(tasklist3[1])
		ui.lineEdit_40.setText(tasklist3[2])
        #if ui.checkBox.isChecked() == False :  #即如果没有选择添加任务点T3，则清空该项任务(也可能不需要这项，应该只点击一次确定)

def show_map():  #显示地图和小车的位置
    map = QPixmap("map5.jpg")  #使用QPixmap获取图像
    ui.label_6.setPixmap(map)   #将图像放在label里，这里用ui.label_6即可，不需要使用pra0911.Ui_Conversion
    ui.label_6.setScaledContents(True) #自动调整图像大小以适应label
    ui.label_9.setPixmap(QPixmap("v1.png"));ui.label_9.setScaledContents(True)
    ui.label_10.setPixmap(QPixmap("v2.png"));ui.label_10.setScaledContents(True)
    ui.label_11.setPixmap(QPixmap("v3.png"));ui.label_11.setScaledContents(True)
    ui.label_13.setPixmap(QPixmap("v4.png"));ui.label_13.setScaledContents(True)

def show_movingcars():
    minute1 = 0; minute0 = 0; second1 = 0; second0 = 0; s = 0
    flag1 = 0; flag2 = 0; flag3 =0
    while 1:
        #设置计时器
        ui.textBrowser_9.setText("计时：" + str(minute1) + str(minute0) + ':' + str(second1)+ str(second0))
	#读取并计算车1的位置
	lo= open('/home/tan/ROBOTS/robot1/location.txt','r+')
	posex0 = lo.read(6)
        posey0=lo.readline()
        posey0=lo.read(6)
	lo.close()
	if (posex0 !='') & (posey0 != ''):
		posex1 = int(round((125.5*float(posex0))-593))
		posey1 = int(round((-101.2*float(posey0))+1432))
	#判断小车图片是否飞出
	if posex1>1171:
		posex1=1171
	if posex1<520:
		posex1=520
	if posey1>701:
		posey1=701
	if posey1<20:
		posey1=20
	BR1 = open('/home/tan/ROBOTS/robot1/BREAKDOWN.txt','r+')
	err1 = BR1.read()
	BR1.close()
	#读取并计算车2的位置
	lo2= open('/home/tan/ROBOTS/robot2/location.txt','r+')
	posex02 = lo2.read(6)
        posey02=lo2.readline()
        posey02=lo2.read(6)
	lo2.close()
	if (posex02 !='') & (posey02 != ''):
		posex2 = int(round((125.5*float(posex02))-593))
		posey2 = int(round((-101.2*float(posey02))+1432))
	if posex2>1171:
		posex2=1171
	if posex2<520:
		posex2=520
	if posey2>701:
		posey2=701
	if posey2<20:
		posey2=20
	#读取并计算车3的位置
	lo3= open('/home/tan/ROBOTS/robot3/location.txt','r+')
	posex03 = lo3.read(6)
        posey03=lo3.readline()
        posey03=lo3.read(6)
	lo3.close()
	if (posex03 !='') & (posey03 != ''):
		posex3 = int(round((125.5*float(posex03))-593))
		posey3 = int(round((-101.2*float(posey03))+1432))
	if posex3>1171:
		posex3=1171
	if posex3<520:
		posex3=520
	if posey3>701:
		posey3=701
	if posey3<20:
		posey3=20
        #读取并计算车4的位置
	lo4= open('/home/tan/ROBOTS/robot4/location.txt','r+')
	posex04 = lo4.read(6)
        posey04=lo4.readline()
        posey04=lo4.read(6)
	lo4.close()
	if (posex04 !='') & (posey04 != ''):
		posex4 = int(round((125.5*float(posex04))-593))
		posey4 = int(round((-101.2*float(posey04))+1432))
	if posex4>1171:
		posex4=1171
	if posex4<520:
		posex4=520
	if posey4>701:
		posey4=701
	if posey4<20:
		posey4=20
        #设置动态小车V1
        ui.label_9.setGeometry(QtCore.QRect(posex1,posey1,46,36))
	v1state = open('/home/tan/ROBOTS/robot1/STATE.txt','r+')
	v1statestr = v1state.read()
	v1state.close()
	if v1statestr == '':
		v1statestr = 0
        ui.label_18.setText("V1:"+cars_state[int(v1statestr)])
        ui.label_18.setGeometry(QtCore.QRect(posex1-15,posey1-20,90,21))
        #设置动态小车V2
        ui.label_10.setGeometry(QtCore.QRect(posex2,posey2,46,36))
	v2state = open('/home/tan/ROBOTS/robot2/STATE.txt','r+')
	v2statestr = v2state.read()
	v2state.close()
	if v2statestr == '':
		v2statestr = 0
        ui.label_19.setText("V2:"+cars_state[int(v2statestr)])
        ui.label_19.setGeometry(QtCore.QRect(posex2-15,posey2-20,86,21))
	   #V2读取故障文件
	v2bd = open('/home/tan/ROBOTS/robot2/BREAKDOWN.txt','r+')
	v2bdstr = v2bd.read()
	v2bd.close()
	if v2bdstr == '2':
		ui.label_17.setPixmap(QPixmap("e2.png"))
		ui.label_17.setScaledContents(True)
		ui.label_17.setGeometry(QtCore.QRect(posex2,posey2,21,21))
        #设置动态小车V3
        ui.label_11.setGeometry(QtCore.QRect(posex3,posey3,46,36))
	v3state = open('/home/tan/ROBOTS/robot3/STATE.txt','r+')
	v3statestr = v3state.read()
	v3state.close()
	if v3statestr == '':
		v3statestr = 0
        ui.label_20.setText("V3:"+cars_state[int(v3statestr)])
        ui.label_20.setGeometry(QtCore.QRect(posex3-15,posey3-20,90,21))
        #设置动态小车V4
        ui.label_13.setGeometry(QtCore.QRect(posex4,posey4,46,36))
	v4state = open('/home/tan/ROBOTS/robot4/STATE.txt','r+')
	v4statestr = v4state.read()
	v4state.close()
	if v4statestr == '':
		v4statestr = 0
        ui.label_21.setText("V4:"+cars_state[int(v4statestr)])
        ui.label_21.setGeometry(QtCore.QRect(posex4-15,posey4-20,86,21))
	   #V4读取故障文件
	v4bd = open('/home/tan/ROBOTS/robot4/BREAKDOWN.txt','r+')
	v4bdstr = v4bd.read()
	v4bd.close()
	if v4bdstr == '1':
		ui.label_16.setPixmap(QPixmap("e1.png"))
		ui.label_16.setScaledContents(True)
		ui.label_16.setGeometry(QtCore.QRect(posex4,posey4,21,21))

	#V1任务列表
	task1 = open('/home/tan/ROBOTS/robot1/TASK_NOW.txt','r+')
	list1 = task1.read()
	task1.close()
	if list1 != '':
		list1 = list1.split()
		V1P1 = list1[3];V1P2 = list1[4];V1P3 = list1[5]
		#输出V1的运输路线
		ui.textBrowser.setText('     '+list1[1]+'-'+list1[2])
		#输出V1的货物
		ui.textBrowser_24.setText('   '+V1P1);ui.textBrowser_30.setText('   '+V1P2)
		ui.textBrowser_36.setText('   '+V1P3)
		#输出V1的任务
		if list1[0] == 'TRANS':
			ui.textBrowser_16.setText('  '+list1[0])
		else: ui.textBrowser_16.setText(list1[0])
	else:
		#输出V1的运输路线
		ui.textBrowser.setText('     ')
		#输出V1的货物
		ui.textBrowser_24.setText('   ');ui.textBrowser_30.setText('   ')
		ui.textBrowser_36.setText('   ')
		#输出V1的任务
		ui.textBrowser_16.setText('  ')

	#V2任务列表
        task2 = open('/home/tan/ROBOTS/robot2/TASK_NOW.txt','r+')
	list2 = task2.read()
	task2.close()
	if list2 != '':
		list2 = list2.split()
		V2P1 = list2[3];V2P2 = list2[4];V2P3 = list2[5]
		#输出V2的运输路线
        	ui.textBrowser_2.setText('     '+list2[1]+'-'+list2[2])
		#输出V2的货物
        	ui.textBrowser_25.setText('   '+V2P1)
        	ui.textBrowser_31.setText('   '+V2P2);ui.textBrowser_37.setText('   '+V2P3)
		#输出V2的任务
		if list2[0] == 'TRANS':
			ui.textBrowser_13.setText('  '+list2[0])
		if list2[0] == 'BREAKDOWN2':
        		ui.textBrowser_13.setText('  '+'TRANS')
		if list2[0] == 'RETURN':		
			ui.textBrowser_13.setText(list2[0])
	else:
		#输出V2的运输路线
        	ui.textBrowser_2.setText('     ')
		#输出V2的货物
        	ui.textBrowser_25.setText('   ')
        	ui.textBrowser_26.setText('   ');ui.textBrowser_27.setText('   ')
		#输出V2的任务
        	ui.textBrowser_13.setText('  ')
		
	#V3任务列表
	task3 = open('/home/tan/ROBOTS/robot3/TASK_NOW.txt','r+')
	list3 = task3.read()
	task3.close()
	if list3 != '':
		list3 = list3.split()
        	V3P1 = list3[3];V3P2 = list3[4];V3P3 = list3[5]
		#输出V3的运输路线
		ui.textBrowser_4.setText('     '+list3[1]+'-'+list3[2]);
		#输出V3的货物
		ui.textBrowser_26.setText('   '+V3P1)
		ui.textBrowser_32.setText('   '+V3P2);ui.textBrowser_38.setText('   '+V3P3)
		#输出V3的任务
		if list3[0] == 'TRANS':	
			ui.textBrowser_14.setText('  '+list3[0])
		else: ui.textBrowser_14.setText(list3[0])
	else:
		#输出V3的运输路线
		ui.textBrowser_4.setText('   ')
		#输出V3的货物
		ui.textBrowser_26.setText('   ')
		ui.textBrowser_32.setText('   ');ui.textBrowser_38.setText('   ')
		#输出V3的任务
		ui.textBrowser_14.setText('  ')
		
	#V4任务列表
	task4 = open('/home/tan/ROBOTS/robot4/TASK_NOW.txt','r+')
	list4 = task4.read()
	task4.close()
	if list4 != '':
		list4 = list4.split()
		# V4的配送结果
		V4P1 = list4[3];V4P2 = list4[4];V4P3 = list4[5]
        	# 输出V4的运输路线
		if list4[2] == 'X1':
        		ui.textBrowser_3.setText('     '+list4[1]+'-'+'T3')
		else:
			ui.textBrowser_3.setText('     '+list4[1]+'-'+list4[2])
        	# 输出V4运输的货物
		ui.textBrowser_27.setText('   '+V4P1)
        	ui.textBrowser_33.setText('   '+V4P2);ui.textBrowser_39.setText('   '+V4P3)
        	# 输出V4的任务
        	if list4[0] == 'BREAKDOWN1':
        		ui.textBrowser_15.setText('  '+'TRANS')
		if list4[0] == 'TRANS':
			ui.textBrowser_15.setText('  '+list4[0])
		if list4[0] == 'RETURN':
			ui.textBrowser_15.setText(list4[0])
	else:
        	# 输出V4的运输路线
        	ui.textBrowser_3.setText('     ')
        	# 输出V4运输的货物
		ui.textBrowser_27.setText('   ')
        	ui.textBrowser_33.setText('   ');ui.textBrowser_39.setText('   ')
        	# 输出V4的任务
        	ui.textBrowser_15.setText('  ')

        # 设置
    	ui.lineEdit_23.setStyleSheet("background-color:white;border-width:1")   
    	ui.lineEdit_24.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_25.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_26.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_27.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_28.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_29.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_30.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_31.setStyleSheet("background-color:white;border-width:1")
    	ui.lineEdit_32.setStyleSheet("background:transparent;border-width:1")
    	ui.lineEdit_33.setStyleSheet("background:transparent;border-width:1")
    	ui.lineEdit_34.setStyleSheet("background:transparent;border-width:1")
    	ui.lineEdit_35.setStyleSheet("background:transparent;border-width:1")
    	ui.lineEdit_36.setStyleSheet("background:transparent;border-width:1")
    	ui.lineEdit_37.setStyleSheet("background:transparent;border-width:1")
	# 读取A1A2A3剩余物资情况
	container1 = open('/home/tan/MATERIAL/CONTAINER/CONTAINER1','r+')
	conlist1 = container1.read()
	conlist1 = conlist1.split()
	container1.close()
	container2 = open('/home/tan/MATERIAL/CONTAINER/CONTAINER2','r+')
	conlist2 = container2.read()
	conlist2 = conlist2.split()
	container2.close()
	container3 = open('/home/tan/MATERIAL/CONTAINER/CONTAINER3','r+')
	conlist3 = container3.read()
	conlist3 = conlist3.split()
	container3.close()
	# 输出A1A2A3剩余物资情况
	if conlist1 !='':
		ui.lineEdit_23.setText(conlist1[0])
		ui.lineEdit_25.setText(conlist1[1])
		ui.lineEdit_24.setText(conlist1[2])

	if conlist2 !='': 
		ui.lineEdit_26.setText(conlist2[0])
		ui.lineEdit_27.setText(conlist2[1])
		ui.lineEdit_28.setText(conlist2[2])

	if conlist3 !='':
        	ui.lineEdit_29.setText(conlist3[0])
		ui.lineEdit_31.setText(conlist3[1])
		ui.lineEdit_30.setText(conlist3[2])

	# 读取T1T2剩余物资情况
	taskpoint1 = open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','r+')
	tasklist1 = taskpoint1.read()
	tasklist1 = tasklist1.split()
	taskpoint1.close()
	taskpoint2 = open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','r+')
	tasklist2 = taskpoint2.read()
	tasklist2 = tasklist2.split()
	taskpoint2.close()
	# 输出T1T2剩余物资情况
	if tasklist1 != '':
		ui.lineEdit_33.setText(tasklist1[0])
		ui.lineEdit_34.setText(tasklist1[1])
		ui.lineEdit_32.setText(tasklist1[2])
		if (tasklist1[0]=='3')&(tasklist1[1]=='1')&(tasklist1[2]=='1'):
			flag1 = 1
	if tasklist2 != '':
		ui.lineEdit_36.setText(tasklist2[0])
		ui.lineEdit_35.setText(tasklist2[1])
		ui.lineEdit_37.setText(tasklist2[2])
		if (tasklist2[0]=='5')&(tasklist2[1]=='1')&(tasklist2[2]=='5'):
			flag2 = 1
	# 判断任务点T3是否开启若开启，则开始读取显示T3的物资量
	ui.pushButton_2.clicked.connect(show_T3)
	taskpoint3 = open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','r+')
	tasklist3 = taskpoint3.read()
	tasklist3 = tasklist3.split()
	taskpoint3.close()
	if (tasklist3[0]!='0')|(tasklist3[1]!='0')|(tasklist3[2]!='0'):
        	ui.lineEdit_39.setText(tasklist3[0])
		ui.lineEdit_38.setText(tasklist3[1])
		ui.lineEdit_40.setText(tasklist3[2])
	if (tasklist3[0]=='0')&(tasklist3[1]=='2')&(tasklist3[2]=='2'):
		flag3 = 1
	print(str(flag1)+' '+str(flag2)+' '+str(flag3))
	#判断3个标志是否均为1，若均为1，则执行任务结束命令
	if (flag1 == 1)&(flag2 == 1)&(flag3 == 1):
		ui.label_12.setText("任务完成！")

        QtWidgets.QApplication.processEvents()  #使UI界面图片可以连续变化
        time.sleep(0.1)   #延迟0.1秒
        #可以自由的调整时钟的时间：以s的为基准，只显示数倍于s的时间即可。如下，控制second0为10倍的s
        s += 1
        if s == 10:
            second0 += 1
            s = 0
	if second0 == 10:
	    second1 += 1
	    second0 = 0
        if second1 == 6:
            minute0 += 1
            second1 =0

#给四个小车写入初始任务
def write_cars123():
    tasklist1 = ["TRANS A1 T2 1 1 1\n"
                 "RETURN T2 A1 0 0 0\n"
                 "TRANS A1 T1 1 1 1\n"]
    TASK1=open('/home/tan/ROBOTS/robot1/TASKCAR.txt','w+')
    TASK1.writelines(tasklist1)
    TASK1.close()
    #写入小车2
    tasklist2 = ["TRANS A2 T1 2 0 0\n"
                 "RETURN T1 A2 0 0 0\n"
                 "BREAKDOWN2 A2 T2 2 0 0\n"]
    TASK2=open('/home/tan/ROBOTS/robot2/TASKCAR.txt','w+')
    TASK2.writelines(tasklist2)
    TASK2.close()
    #写入小车3
    tasklist3 = ["TRANS A3 T2 1 0 2\n"
                 "RETURN T2 A2 0 0 0\n"
                 "TRANS A2 T2 1 0 2\n"]
    TASK3=open('/home/tan/ROBOTS/robot3/TASKCAR.txt','w+')
    TASK3.writelines(tasklist3)
    TASK3.close()

def write_car4():
    #写入小车4
    tasklist4 = ["TRANS A3 T3 0 1 1\n"
                 "RETURN T3 A1 0 0 0\n"
                 "BREAKDOWN1 A1 X1 0 1 1\n"]
    TASK4=open('/home/tan/ROBOTS/robot4/TASKCAR.txt','w+')
    TASK4.writelines(tasklist4)
    TASK4.close()

def init_task():#初始化任务列表
    init_taskpoint = ["0 0 0\n"]
    taskpit1 = open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT1','w+')
    taskpit1.writelines(init_taskpoint)
    taskpit1.close()
    taskpit2 = open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT2','w+')
    taskpit2.writelines(init_taskpoint)
    taskpit2.close()
    taskpit3 = open('/home/tan/MATERIAL/TASKPOINT/TASKPOINT3','w+')
    taskpit3.writelines(init_taskpoint)
    taskpit3.close()

    init_taskcar1 = open('/home/tan/ROBOTS/robot1/TASKCAR.txt','w+')
    init_taskcar1.writelines('')
    init_taskcar1.close()
    init_taskcar2 = open('/home/tan/ROBOTS/robot2/TASKCAR.txt','w+')
    init_taskcar2.writelines('')
    init_taskcar2.close()
    init_taskcar3 = open('/home/tan/ROBOTS/robot3/TASKCAR.txt','w+')
    init_taskcar3.writelines('')
    init_taskcar3.close()
    init_taskcar4 = open('/home/tan/ROBOTS/robot4/TASKCAR.txt','w+')
    init_taskcar4.writelines('')
    init_taskcar4.close()

def reset():
    ui.label_12.setText("任务完成！")

def combo():
    index = ui.comboBox.currentIndex()
    index = (index + 1)*100
    tim = open('/home/tan/ROBOTS/time.txt','w+')
    tim.writelines(str(index))
    tim.close()

def bandwidth():

    pub1 = rospy.Publisher('/robot1/bandwidth_command', String, queue_size=10)
    pub2 = rospy.Publisher('/robot2/bandwidth_command', String, queue_size=10)
    pub3 = rospy.Publisher('/robot3/bandwidth_command', String, queue_size=10)
    pub4 = rospy.Publisher('/robot4/bandwidth_command', String, queue_size=10)

    bandwidth_str = "bandwidth"
    rospy.loginfo("bw_success")
    pub1.publish(bandwidth_str)
    pub2.publish(bandwidth_str)
    pub3.publish(bandwidth_str)
    pub4.publish(bandwidth_str)
    stime = rospy.get_time()
    sendtime = open('/home/tan/TIME/BW/send','w+')
    sendtime.write(str(stime))
    sendtime.close()

def response():

    pub1 = rospy.Publisher('/robot1/response_command', String, queue_size=10)
    pub2 = rospy.Publisher('/robot2/response_command', String, queue_size=10)
    pub3 = rospy.Publisher('/robot3/response_command', String, queue_size=10)
    pub4 = rospy.Publisher('/robot4/response_command', String, queue_size=10)
    response_str = "response"
    pub1.publish(response_str)
    pub2.publish(response_str)
    pub3.publish(response_str)
    pub4.publish(response_str)
    rospy.loginfo("re_success")
    stime = rospy.get_time()
    sendtime = open('/home/tan/TIME/RE/send','w+')
    sendtime.write(str(stime))
    sendtime.close()

def show_res():
    time.sleep(0.5)
#读取sub1
    sub1 = open('/home/tan/TIME/RE/sub1','r+')
    sub1str = sub1.read(5)
    if sub1str != '':
	sub1float = float(sub1str)
    sub1.close()
#读取sub2
    sub2 = open('/home/tan/TIME/RE/sub2','r+')
    sub2str = sub2.read(5)
    if sub2str != '':
	sub2float = float(sub2str)
    sub2.close()
#读取sub3
    sub3 = open('/home/tan/TIME/RE/sub3','r+')
    sub3str = sub3.read(5)
    if sub3str != '':
	sub3float = float(sub3str)
    sub3.close()
#读取sub4
    sub4 = open('/home/tan/TIME/RE/sub4','r+')
    sub4str = sub4.read(5)
    if sub4str != '':
	sub4float = float(sub4str)
    sub4.close()
#如果是空，则文本框不显示
    if (sub1str=='')|(sub2str=='')|(sub3str=='')|(sub4str==''):
	ui.lineEdit_4.setText('0')
#比较四个时间的大小
    else:
	submin = min(sub1float,sub2float,sub3float,sub4float)
	submin = int(1000 * submin)
	if submin<=0:
	    submin = submin * (-1)
	ui.lineEdit_4.setText(str(submin) + ' ' + 'ms')


def show_bw():
    time.sleep(1)
#读取sub1
    sub1 = open('/home/tan/TIME/BW/sub1','r+')
    sub1str = sub1.read(5)
    if sub1str != '':
	sub1float = float(sub1str)
    sub1.close()
#读取sub2
    sub2 = open('/home/tan/TIME/BW/sub2','r+')
    sub2str = sub2.read(5)
    if sub2str != '':
	sub2float = float(sub2str)
    sub2.close()
#读取sub3
    sub3 = open('/home/tan/TIME/BW/sub3','r+')
    sub3str = sub3.read(5)
    if sub3str != '':
	sub3float = float(sub3str)
    sub3.close()
#读取sub4
    sub4 = open('/home/tan/TIME/BW/sub4','r+')
    sub4str = sub4.read(5)
    if sub4str != '':
	sub4float = float(sub4str)
    sub4.close()
#如果是空，则文本框不显示
    if (sub1str=='')|(sub2str=='')|(sub3str=='')|(sub4str==''):
	ui.lineEdit_41.setText('0')
#比较四个时间的大小
    else:
	submax = max(sub1float,sub2float,sub3float,sub4float)
	submax = int(1000 * submax)
	if submax<=0:
	    submax = submax * (-1)
	ui.lineEdit_41.setText(str(submax) + ' ' + 'ms')

'''
#error1是机械故障，车辆时静止的；error2是通信故障，车辆时运动的
def show_error1():
    #创建机械故障提示图形
    ui.label_16.setPixmap(QPixmap("e1.png"));ui.label_16.setScaledContents(True)
    #如果得到错误提示，即使机械故障图获取故障车辆的位置
    #ui.label_16.setGeometry(QtCore.QRect())  #括号中填入故障车辆的位置信息
def show_error2():
    #创建通信故障提升图形
    ui.label_17.setPixmap(QPixmap("e2.png"));ui.label_17.setScaledContents(True)
    #如果得到错误提示，即使通信故障图与故障车辆一起运动
    # ui.label_17.setGeometry(QtCore.QRect())  #括号中填入故障车辆的位置信息,同时将show_error2函数放在获取故障车位置的循环中，达成共同运动'''

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建QAppication类的实例
    MainWindow = QMainWindow()
    #设置背景图片
    window_pale = QPalette()
    window_pale.setBrush(QPalette.Background, QBrush(QPixmap("2.jpg")))
    MainWindow.setPalette(window_pale)
    ui = pra0911.Ui_Conversion()
    ui.setupUi(MainWindow)
    rospy.init_node('bandwidth_response_talker', anonymous=True)  #初始化talker结点

    MainWindow.show()
    ui.textBrowser_23.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_23.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_24.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_25.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_26.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_27.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_28.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_29.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_30.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_31.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_32.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_33.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_34.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_35.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_36.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_37.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_38.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_39.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.lineEdit_40.setStyleSheet("background:transparent;border-width:0;border-style:outset")

    init_task()#初始化车辆任务列表
    response()
    bandwidth()
    ui.pushButton.clicked.connect(write_cars123)
    ui.pushButton.clicked.connect(partial(convert, ui))
    ui.pushButton.clicked.connect(show_map)
    ui.pushButton.clicked.connect(response)
    ui.pushButton.clicked.connect(show_movingcars)

    ui.pushButton_2.clicked.connect(add_T3)
    ui.pushButton_2.clicked.connect(write_car4)
    ui.pushButton_3.clicked.connect(reset)

    ui.pushButton_4.clicked.connect(bandwidth)
    ui.pushButton_4.clicked.connect(combo)
    ui.pushButton_5.clicked.connect(show_res)
    ui.pushButton_6.clicked.connect(show_bw)
    sys.exit(app.exec_())



