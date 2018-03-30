


lower =int (input("please input a lower num:"))
upper =int (input("please input a upper num:"))

sum =0
for num in range(lower,upper):
	l=len(str(num))
	for n in str(num):
		sum+=int (n)**l
	if num==sum:
		print (num ,end=",")
	sum=0
	

