#!/usr/bin/python
# -*- coding: UTF-8 -*-

def lcm(x, y): # very fast
    s = x*y
    while y: x, y = y, x%y
    return s//x
print(lcm(12, 8)) #result: 24

def lcm1(x,y):
	s=x*y
	while y!=0:
		x,y=y,x%y
	return s//x
print ("lcm1方法结果：",(lcm1(8,12)))