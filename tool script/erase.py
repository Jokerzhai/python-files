#-*- coding:utf-8 -*-

import sys
import os
import signal
import logging
import time

#jlink_path="C:/Program Files (x86)/SEGGER/JLink_V632a"
jlink_path="C:/Program Files (x86)/SEGGER/JLink_V634c"
gdb_path="C:\gnu\\gcc_arm_5.4\\bin"
bin_path='E:\standalone\IMXRT1050\SDK_2.0_EVK-MIMXRT1050_20170915_v5\\boards\evkmimxrt1050\demo_apps\lwip\lwip_ping\\bm\\armgcc\sdram_debug'
result_file_name = 'result.txt'

# print os.system("route print > t.txt")
# output = os.popen("ipconfig")


 # Class subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, 

 #                                  stderr=None, preexec_fn=None,  close_fds=True, shell=False, 

 #                                 cwd=None, env=None, universal_newlines=False, startupinfo=None, 

 #                              creationflags=0, restore_signals=True, start_new_session=False, pass_fds=())
import subprocess
'''
cortex-m7 MKW41Z512xxx4
600101615
'''
jlink_cmd_list = [
    # jlink_path + '\jlinkgdbserver.exe',
    jlink_path + '\JLinkGDBServerCL.exe',
    # '-device','cortex-m7',
    '-device','MIMXRT1052XXXXB',
    # '-scriptfile', 'evkbimxrt1050_sdram_init.jlinkscript',
    '-speed', 'auto',
    '-if', 'swd',
    '-port', '2331'
]

def reserveResult(file_name, result_str):
    str_set = ()
    with open(file_name, 'r') as fd:
        str_set = set(fd.read().split('\n'))
        str_set.add(result_str)
        str_set.remove('')


    with open(file_name, 'w') as fd:
        for i in str_set:
            fd.write(i+'\n')

def patten_realtime_output(child_pid, str):
    while True:
        r = child_pid.stdout.readline().strip()
        if r:
            print r
        if str in r:
            return True
        if subprocess.Popen.poll(child_pid) != None and not r:
            return 0

erase_cmd_list = [
    # jlink_path + '\jlinkgdbserver.exe',
    jlink_path + '\JLink.exe',
    # '-device','cortex-m7',
    '-SelectEmuBySN','600101615',
    #'-CommanderScript', 'evkbimxrt1050_flash_erase.jlink',
    '-CommanderScript', 'erase.jlink'
]

def erase_flash():
    erase_pid = subprocess.Popen(erase_cmd_list, stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    if patten_realtime_output(erase_pid, 'done'):
        subprocess.call(['taskkill', '/F', '/T', '/PID',  str(erase_pid.pid)])

def main():
    # if len(sys.argv)<2:
    #     print 'params error'
    #     exit()



    subprocess.call(erase_cmd_list, shell=True)
    print '-'*20 + ' erase done ' + '-'*20

    # erase_flash()
    # os.system('C:/\"Program Files (x86)\"/SEGGER/JLink_V631d\JLink.exe -SelectEmuBySN 600101615 -CommanderScript evkbimxrt1050_flash_erase.jlink')
    # erase_pid = subprocess.Popen(['ping', 'localhost'], stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # if patten_realtime_output(erase_pid, 'statistics'):
    #     subprocess.call(['taskkill', '/F', '/T', '/PID',  str(erase_pid.pid)])

    # cmd_bin_path =sys.argv[1]
    # print os.path.isfile(cmd_bin_path)
    # cmd_bin_path.replace('\\','\\\\')

    # gdb_cmd_list = [
    #     gdb_path + '\\arm-none-eabi-gdb.exe',
    #     cmd_bin_path,
    #     # bin_path + '\lwip_ping_bm.elf',
    #     '-x', 'gdb.init'
    # ]

    # jlink_pid = subprocess.Popen(jlink_cmd_list, stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # logging.info("jlink-gdbserver pid = %s"%jlink_pid)
    # if patten_realtime_output(jlink_pid, 'Connected to target'):
    #     child_gdb = subprocess.Popen(gdb_cmd_list, stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #     logging.info("arm gdb pid = %s"%child_gdb)    
    #     if patten_realtime_output(child_gdb, 'Transfer rate:'):
    #         time.sleep(1)
    #         subprocess.call(['taskkill', '/F', '/T', '/PID',  str(jlink_pid.pid)])
    #         subprocess.call(['taskkill', '/F', '/T', '/PID',  str(child_gdb.pid)])
    
    #         reserveResult(result_file_name, cmd_bin_path.split('\\')[-1])
main()

# jlink_pid = subprocess.Popen(jlink_cmd_list, shell=True)
# child_gdb = subprocess.call(gdb_cmd_list, 0, None, None, None, None, shell=True)
# jlink_pid.kill()
# # a = os.kill(pid, signal.9) #　与上等效
# reserveResult(result_file_name, cmd_bin_path.split('\\')[-1])
# print 'finished!!!'
# child_gdb.stdin.write('target remote localhost:2331')
# child_gdb.stdin.write('load')


# os.system("echo " + jlink_path + '> result.txt')

# (set(open().read().split('\n')))