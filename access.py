import os,sys


ret =os.access("1.txt",os.F_OK)
print ("F——OK 返回值%s"% ret)

ret =os.access("1.txt",os.R_OK)
print ("R——OK 返回值%s"% ret)

ret =os.access("1.txt",os.W_OK)
print ("W——OK 返回值%s"% ret)


ret =os.access("1.txt",os.X_OK)
print ("X——OK 返回值%s"% ret)