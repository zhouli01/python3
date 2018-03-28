# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print('a:',a)
print('b:',b)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素