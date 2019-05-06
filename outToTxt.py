#-*- coding: utf-8 -*-
import time
def outTxt(str,fileName='C:\SPIDER\out.txt'):
    with open(fileName, "a",encoding='utf-8') as f:
        f.writelines(str)
        f.write("\n")

f=open('C:\SPIDER\out.txt', "w+",encoding='utf-8')
f.write("爬虫test 知乎话题热门数据---by zw \n")
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
f.write(str(time)+"\n")
f.close()