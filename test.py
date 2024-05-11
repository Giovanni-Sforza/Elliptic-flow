import matplotlib.pyplot as plt
import numpy as np

def openfile(filename,size,biginrow):
    file = open(filename, "r")  # 以只读模式打开文件
    lines = file.readlines()  # 获取所有行并保存到lines列表中
    data = []
    # 指定开始读取的行
    for line in lines[int(biginrow) - 1:]:  # 读取指定的所有行
        line = line.strip('\n')  # 去掉换行符
        line = line.split()
        data = np.hstack((data,line)) # 去掉空格

    file.close()  # 关闭文件
    data = np.array(data,dtype=float)
    data = np.reshape(data,size)
    return data

dataproton = openfile("proton\dNptdpt_PbPb276_proton_c25  c.txt",(40,8),2)

plt.yscale('log')
plt.plot(dataproton[10:40,0],dataproton[10:40,1])
plt.plot(dataproton[10:40,0],dataproton[10:40,2])
plt.show()
