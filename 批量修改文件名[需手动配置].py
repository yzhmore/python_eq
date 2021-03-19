#!/usr/bin/python3

import os,sys

#视频文件后缀
extName = ".mp4"
extName2 = ".mkv"
extName3 = ".avi"

#被修改文件的目录地址
path = "E:/VideoList/TVPlay/" + input("please input your file path:")
filelist = os.listdir(path)
n = 1
#想修改成的文件名
wantName = "30枚银币第一季"

for i in filelist:
    #分离文件名称与后缀
    splitName = os.path.splitext(i)
    #如有符合后缀名的文件则替换文件名称
    if splitName[1] == extName or splitName[1] == extName2 or splitName[1] == extName3:
        newname = wantName + str(n) + splitName[1]
        os.chdir(path)
        os.rename(i,newname)
        print(os.path.basename(i)+' -> '+ os.path.basename(newname))
        n+=1