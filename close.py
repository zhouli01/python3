#！usr/bin/python3



fo=open("1.txt","r+")
print("文件名：",fo.name)

seq=["菜鸟网络 1\n","菜鸟网络 2"]
fo.writelines(seq)
# fid=fo.fileno()
# print ("文件描述符:",fid)
#fo.flush()
#
# ret=fo.isatty()
# print ("返回值:",ret)

# line =fo.readline()
# print("读取的数据为：%s" %(line) )
#
# position=fo.tell()
# print("当前文件位置为：%d" %(position))

fo.close()