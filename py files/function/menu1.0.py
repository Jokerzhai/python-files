#-*- coding: utf-8 -*-

import sys
import os
import yaml
import re
import time

reload(sys)
sys.setdefaultencoding('utf-8')


##############对raw_input输入字符类型判断并转化################
def input_handle(s):
    if str.isdigit(s):              ##对输入是否是数字进行判断
        s = int(s)                  ##如果输出的是数字，则转化为整数类型
    else:
        s = s.decode('utf-8')       ##如果是字符串或汉字，则转化为unicode类型（主要是针对汉字转化，汉字默认是str）
    return s

##############框架函数################################
def framework(task_mgr='',device_mgr=''):
    os.system('cls')                ##清屏
    print('''   
    **************欢迎使用快捷打开系统******************
    
    
    +-----------------------------------------------
    |      1、任务管理器
    |      2、设备管理器
    +-----------------------------------------------
    '''%(task_mgr,device_mgr)
    )

##############输出展示函数#####################
def show(task_mgr='',device_mgr=''):

    global  T_NAME                                                    ##任务管理器全局变量##
    global  D_NAME                                                    ##设备管理器全局变量##
cmd_index = raw_input('请输入编号或者文字 ： ')
if   cmd_index == 'q':                                          ##如果输入为q，则退出程序
   sys.exit(0)
elif cmd_index == '1':                                        #############任务管理器输出函数#######################
    T_NAME = os.system('Taskmgr')
elif cmd_index == '2':
    D_NAME =os.system('devmgmt')                              #############设备管理器输出函数#######################
else:
    T_NAME = ''
    D_NAME = ''
while T_NAME:                                                 ##全局变量不为空进行循环##
    framework(T_NAME,D_NAME)
    show(T_NAME,D_NAME)
    time.sleep(5)
    T_NAME = ''
    D_NAME = ''
###############主函数##################################


###############定义全局变量############################
M_NAME = ''             ##任务管理器全局变量##
D_NAME = ''             ##设备管理器全局变量##
###############主循环开始##############################
while True:
    framework(T_NAME, D_NAME)        ##调用框架，显示初始状态