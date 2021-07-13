# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QPalette,QBrush
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import time
import pra0911

cars_task = ["trans","return","rescue"]
cars_state = ["空闲","运输","装货","卸货","返回","救援"]
posex0 = 0; posey0 = 0

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
# 通过checkbox判断是否有新增任务，若有，则读入任务点T3
    T3P1 = 0; T3P2 = 0; T3P3 = 0  #初始化三个变量
    if ui.checkBox.isChecked() == True :  #判断checkbox是否勾选，若勾选了，则读入T3的数据
        T3P1 = ui.lineEdit_17.text();T3P2 = ui.lineEdit_18.text();T3P3 = ui.lineEdit_19.text()
   #if ui.checkBox.isChecked() == False :  #即如果没有选择添加任务点T3，则清空该项任务(也可能不需要这项，应该只点击一次确定)


# 5个小车的配送结果
    roadv1 = 'A1-T1';roadv2 = 'A1-T1';roadv3 = 'A1-T1'
    roadv4 = 'A1-T1';roadv5 = T3P1
    V1P1 = 0;V1P2 = 0;V1P3 = 0; V2P1 = 0;V2P2 = 0;V2P3 = 0; V3P1 = 0;V3P2 = 0;V3P3 = 0;
    V4P1 = 0;V4P2 = 0;V4P3 = 0; V5P1 = 0;V5P2 = 0;V5P3 = 0

# 输出5个小车的配送结果
    ui.textBrowser.setText(str(roadv1));ui.textBrowser_2.setText(str(roadv2));ui.textBrowser_3.setText(str(roadv3))
    ui.textBrowser_4.setText(str(roadv4));ui.textBrowser_5.setText(str(roadv5))
    #输出各个小车运输的货物
    ui.textBrowser_24.setText(str(V1P1));ui.textBrowser_25.setText(str(V2P1));ui.textBrowser_26.setText(str(V3P1))
    ui.textBrowser_27.setText(str(V4P1));ui.textBrowser_28.setText(str(V5P1))
    ui.textBrowser_30.setText(str(V1P2));ui.textBrowser_31.setText(str(V2P2));ui.textBrowser_32.setText(str(V3P2))
    ui.textBrowser_33.setText(str(V4P2));ui.textBrowser_34.setText(str(V5P2))
    ui.textBrowser_36.setText(str(V1P3));ui.textBrowser_37.setText(str(V2P3));ui.textBrowser_38.setText(str(V3P3))
    ui.textBrowser_39.setText(str(V4P3));ui.textBrowser_40.setText(str(V5P3))
    #输出各个小车的任务
    ui.textBrowser_12.setText(cars_task[0]);ui.textBrowser_13.setText(cars_task[0]);ui.textBrowser_14.setText(cars_task[0])
    ui.textBrowser_15.setText(cars_task[0]);ui.textBrowser_16.setText(cars_task[0]);
# 输出物资点剩余物资情况
    ui.textBrowser_6.setText("1-2-3");ui.textBrowser_7.setText("1-2-3");ui.textBrowser_8.setText("1-2-3")

def show_map():  #显示地图和小车的位置
    map = QPixmap("map5.jpg")  #使用QPixmap获取图像
    ui.label_6.setPixmap(map)   #将图像放在label里，这里用ui.label_6即可，不需要使用pra0911.Ui_Conversion
    ui.label_6.setScaledContents(True) #自动调整图像大小以适应label
    ui.label_9.setPixmap(QPixmap("v1.png"));ui.label_9.setScaledContents(True)
    ui.label_10.setPixmap(QPixmap("v2.png"));ui.label_10.setScaledContents(True)
    ui.label_11.setPixmap(QPixmap("v3.png"));ui.label_11.setScaledContents(True)
    ui.label_13.setPixmap(QPixmap("v4.png"));ui.label_13.setScaledContents(True)

def show_movingcars():
    n = 100
    minute = 00; second = 0; s = 0
    #设置图片标签的左、上边缘，以及宽度和高度
    while 1:
        #设置计时器
        ui.textBrowser_9.setText("计时：" + str(minute) + ':' + str(second))
	lo= open('/home/tan/ROBOTS/robot1/location.txt','r+')
	posex0 = lo.read(6)
        posey0=lo.readline()
        posey0=lo.read(6)
	posex1 = int(round((125.5*float(posex0))-293))
	posey1 = int(round((-101.2*float(posey0))+1432))
        #设置动态小车V1
        ui.label_9.setGeometry(QtCore.QRect(posex1,posey1,46,36))
        ui.label_18.setText(cars_state[1])
        ui.label_18.setGeometry(QtCore.QRect(posex1,posey1,41,21))
        #设置动态小车V2
        ui.label_10.setGeometry(QtCore.QRect(820,420,46,36))
        ui.label_19.setText(cars_state[1])
        ui.label_19.setGeometry(QtCore.QRect(820,400+n,41,21))
        #设置动态小车V3
        ui.label_11.setGeometry(QtCore.QRect(1050,420,46,36))
        ui.label_20.setText(cars_state[1])
        ui.label_20.setGeometry(QtCore.QRect(1050,400+n,41,21))
        #设置动态小车V4
        ui.label_13.setGeometry(QtCore.QRect(1100,420,46,36))
        ui.label_21.setText(cars_state[1])
        ui.label_21.setGeometry(QtCore.QRect(1100,410+n,41,21))
        
        #可以在此插入show_error1()
        QtWidgets.QApplication.processEvents()  #使UI界面图片可以连续变化
        time.sleep(0.1)   #延迟0.1秒
        #可以自由的调整时钟的时间：以s的为基准，只显示数倍于s的时间即可。如下，控制second为10倍的s
        s += 1
        if s == 20:
            second += 1
            s = 0
        if second == 60:
            minute += 1
            second =0
        n-=1

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
    # ui.label_17.setGeometry(QtCore.QRect())  #括号中填入故障车辆的位置信息,同时将show_error2函数放在获取故障车位置的循环中，达成共同运动

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建QAppication类的实例
    MainWindow = QMainWindow()
    #设置背景图片
    window_pale = QPalette()
    window_pale.setBrush(QPalette.Background, QBrush(QPixmap("pic.jpg")))
    MainWindow.setPalette(window_pale)
    ui = pra0911.Ui_Conversion()
    ui.setupUi(MainWindow)

    MainWindow.show()
    ui.textBrowser_23.setStyleSheet("background:transparent;border-width:0;border-style:outset")
    ui.pushButton.clicked.connect(partial(convert, ui))
    ui.pushButton.clicked.connect(show_map)
    ui.pushButton.clicked.connect(show_movingcars)

    sys.exit(app.exec_())



