#-*- coding:utf-8 -*-

import sys
import os
import signal
import logging
import time

jlink_path="C:/Program Files (x86)/SEGGER/JLink_V634b"
gdb_path="C:/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin"
bin_path='‪C:\manual_test_case\allcases'
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
'''
jlink_cmd_list = [
    # jlink_path + '\jlinkgdbserver.exe',
    jlink_path + '\JLinkGDBServerCL.exe',
    # '-device','cortex-m7',
    '-device','MIMXRT1062xxx6A',
     '-scriptfile', 'evkmimxrt1060_sdram_init.jlinkscript',
    '-speed', 'auto',
    '-if', 'swd',
    '-port', '2331'
]

if __name__ == '__main__':
    if 2 != len(sys.argv):
        print 'Params should be 2. If params doesnot exit, please use None instead and the first params should not be empty'
        os._exit(1)
cmd_bin_path =sys.argv[1]
print os.path.isfile(cmd_bin_path)
cmd_bin_path.replace('\\','\\\\')

gdb_cmd_list = [
    gdb_path + '\\arm-none-eabi-gdb.exe',
    cmd_bin_path,
    # bin_path + '\lwip_ping_bm.elf',
    '-x', 'gdb.init'
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
    

def main():
    if len(sys.argv)<2:
        print 'params error'
        exit()
    jlink_pid = subprocess.Popen(jlink_cmd_list, stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    logging.info("jlink-gdbserver pid = %s"%jlink_pid)
    if patten_realtime_output(jlink_pid, 'Connected to target'):
        child_gdb = subprocess.Popen(gdb_cmd_list, stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        logging.info("arm gdb pid = %s"%child_gdb)    
        if patten_realtime_output(child_gdb, 'Transfer rate'):
            time.sleep(1)
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(jlink_pid.pid)])
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(child_gdb.pid)])
    
            reserveResult(result_file_name, cmd_bin_path.split('\\')[-1])
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