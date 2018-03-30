def gcd(x,y):
	return x if y==0 else gcd(y,x%y)
print ("gcd方法:",(gcd(12,8)))





def gcd1(x,y):
	while y!=0:
		x,y=y,x%y
	return x
print ("gcd1方法结果：",(gcd1(8,12)))
