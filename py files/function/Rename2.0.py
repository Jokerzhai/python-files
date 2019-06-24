import os

path_name = 'C:/ZZY/TEST'
i = 0
for item in os.listdir(path_name):
    os.rename(os.path.join(path_name,item),os.path.join(path_name,(str(i)+'.txt')))
    i+=1