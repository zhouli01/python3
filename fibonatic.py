# a=0
# b=1
# while b < 1000:
#     print(b)
#     a, b = b, a+b


n=int(input("please input n:"))
n=str(n)
m=n[::-1]
if(m==n):
	print("%s is 回文数" %n)
