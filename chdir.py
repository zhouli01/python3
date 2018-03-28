#！usr/bin/python3
import os,sys

path = "D:/python3/venv"

ret =os.getcwd()
print ("当前工作目录为%s" %ret)

os.chdir(path)

ret=os.getcwd()
print ("变更后的工作目录为%s" %ret)
