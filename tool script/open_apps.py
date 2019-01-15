import os
import subprocess
import sys
import time
#os.startfile("C:\Program Files (x86)\SEGGER\JLink_V634c\JLink.exe")

jlink_path="C:/Program Files (x86)/SEGGER/JLink_V634c"

#JLink_connect_cmd = ["C:\Program Files (x86)\SEGGER\JLink_V634c\JLink.exe"]
JLink_connect_cmd = [jlink_path + '/JLink.exe','-scriptfile', 'erase.jlinkscript']
#Jlink_cmd_list = ['s','erase','exec EnableEraseAllFlashBank','erase']


p = subprocess.Popen(JLink_connect_cmd,stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
p.wait()

#p.stdin.write('connect')


#p.stdin.write('?')
#print p.stdout.read()

#Jlink_pid.kill()







