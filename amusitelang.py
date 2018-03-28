#!user/bin/python
#coding:UTF-8
lower=int(input("请输入比较小的数字："))
upper=int(input("请输入比较打的数字："))

sum =0
for num in range(lower,upper):
	L=len(str(num))
	for n in  str(num):
		sum+=int(n)**L
	if num==sum:
		print (num)
	sum =0