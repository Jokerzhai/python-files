import os, shutil
#import time


def MoveFile(src_path,target_path):
#    src_path = 'C:/ZZY/TEST/'
#    target_path = 'C:/New folder/'
    while True:
#        time.sleep(1)
        file_list =  os.listdir(src_path)
        if len(file_list) > 0:
            for file in file_list:
                shutil.move(src_path+file,target_path+file)

MoveFile('C:/ZZY/TEST/','C:/New folder/')