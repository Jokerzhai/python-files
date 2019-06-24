#-*- coding: utf-8 -*-

import os

class ImageRename():
    def _init_(self):
        self.path = 'C:/ZZY/test'           ##等下试试在前面加个r试试能不能转义

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 0

        for item in filelist:
            if item.endswitch('.txt '):
                src = os.path.join(os.path.abspath(self.path),item)
                dst = os.path.join(os.path.abspath(self.path),'0000' + format(str(i),'0>3s')+'.txt')
                os.rename(src,dst)
                print 'converting %s to %s ...' %(src,dst)
                i = i+1
        print 'total %d to rename & converted %d txts'      %(total_num,i)
    if _name_ == '_main_':
        newname = ImageRename()
        newname.rename()