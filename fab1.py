#1use/bin/python


num= int(input('please input a num:'))
f1=1
f2=1


if num<=0:
	print ("请输入一个整数:")
elif num==1:
	print ("数列为: %d" %f1)
else:
	print("数列为：",end=" ")
	print (f1,f2,end=" ")
	for i in 	range(1,num-1):
		f = f1+f2
		f1,f2=f2,f
		print (f,end=" ")
