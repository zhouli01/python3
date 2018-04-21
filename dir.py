import os,time

currentdir = os.getcwd()
filenum, filesize, dirnum = 0, 0, 0
for name in os.listdir(currentdir):
    if os.path.isfile(name):
        print('%s\t\t%d\t%s' % (time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getmtime(name))), os.path.getsize(name), name))
        filenum += 1
        filesize += os.path.getsize(name)
    elif os.path.isdir(name):
        print('%s\t<DIR>\t\t%s' % (time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getmtime(name))), name))
        dirnum += 1

print('\t\t%d个文件\t\t%d 字节' % (filenum, filesize))
print('\t\t%d个目录' % dirnum)