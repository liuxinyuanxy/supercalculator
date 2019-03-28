import math
import os
def clear():os.system('cls')
def fac(x):
	s = 1
	for i in range(x):
		s = s * (i + 1)
	return s
os.system("color F0")
os.system("title supercalculator        --code by liuxinyuan")
print("这是一个超级计算器，克服了传统计算器拥有范围限制的弊端，但如果计算量过大(如1e10000以上的运算)仍会使计算出错甚至导致程序崩溃")
print("每次计算完成后，请输入exit退出程序，或按回车键继续计算")
print("请注意一定要按要求输入，否则可能导致程序崩溃")
print("请确认是否每次计算完成后清屏：(yes/no)")
str = input()
p = str[0]
while str != 'exit':
	if p != 'n':
		clear()
	print("请输入字母以选择运算类型并按回车键确认:(由于技术原因，目前仅支持整数与小数运算)")
	print("a.整数 b.小数")
	k = input()
	if p != 'n':
		clear()
	print("请输入数字以选择功能并按回车键确认：")
#	print("注意：如果输入并按回车后程序无反应，请再按一次回车，此bug正修复中") 此bug已修复qwq
	print("普通运算部分")
	print("1.普通加法(x+y) 2.普通减法(x-y) 3.普通乘法(x*y) 4.普通除法(x/y)")
	print("5.取整除法(x/y) 6.模除(x mod y) 7.x的y次方(x^y) 8.平方(x^2) 9.开根(sqrt(x))")
	print("10.e的x次幂(exp(x)) 11.以e为底的对数(ln(x)) 12.以y为底的对数(logy(x))")
	print()
	print("弧度制运算部分")
	print("13.sin(x) 14.cos(x) 15.tan(x) 16.asin(x) 17.acos(x) 18.atan(x)")
	print("19.弧度转角度 20.角度转弧度")
	print()
	if k == 'a':
		print("组合计数部分")
		print("21.阶乘(x!)")
		print("22.组合数(从x个元素中无序地选取y个元素的方案数)")
		print("23.排列数(从x个元素中有序地选取y个元素的方案数)")
	opt = int(input())
	if k == 'a':
		print("请输入x")
		x = int(input())
		if opt in [1, 2, 3, 4, 5, 6, 7, 12, 22, 23]:
			print("请输入y")
			y = int(input())
			if opt == 1:
				print(x + y)
			elif opt == 2:
				print(x - y)
			elif opt == 3:
				print(x * y)
			elif opt == 4:
				print(x / y)
			elif opt == 5:
				print(x // y)
			elif opt == 6:
				print(x % y)
			elif opt == 7:
				print(x**y)
			elif opt == 22:
				print(fac(x) // (fac(y) * fac(x - y)))
			elif opt == 23:
				print(fac(x) // fac(x - y))
			else:
				print(math.log(x) / math.log(y))
		else:
			if opt == 8:
				print(x**2)
			elif opt == 9:
				print(math.sqrt(x))
			elif opt == 10:
				print(math.exp(x))
			elif opt == 11:
				print(math.log(x))
			elif opt == 13:
				print(math.sin(x))
			elif opt == 14:
				print(math.cos(x))
			elif opt == 15:
				print(math.tan(x))
			elif opt == 16:
				print(math.asin(x))
			elif opt == 17:
				print(math.acos(x))
			elif opt == 21:
				print(fac(x))
			elif opt == 18:
				print(math.atan(x))
			elif opt == 19:
				print(math.degrees(x))
			elif opt == 20:
				print(math.radians(x))
	else:
		print("请输入x")
		x = eval(input())
		if opt in [1, 2, 3, 4, 5, 6, 7, 12]:
			print("请输入y")
			y = eval(input())
			if opt == 1:
				print(x + y)
			elif opt == 2:
				print(x - y)
			elif opt == 3:
				print(x * y)
			elif opt == 4:
				print(x / y)
			elif opt == 5:
				print(x // y)
			elif opt == 6:
				print(x % y)
			elif opt == 7:
				print(x**y)
			else:
				print(math.log(x) / math.log(y))
		else:
			if opt == 8:
				print(x**2)
			elif opt == 9:
				print(math.sqrt(x))
			elif opt == 10:
				print(math.exp(x))
			elif opt == 11:
				print(math.log(x))
			elif opt == 13:
				print(math.sin(x))
			elif opt == 14:
				print(math.cos(x))
			elif opt == 15:
				print(math.tan(x))
			elif opt == 16:
				print(math.asin(x))
			elif opt == 17:
				print(math.acos(x))
			elif opt == 18:
				print(math.atan(x))
			elif opt == 19:
				print(math.degrees(x))
			elif opt == 20:
				print(math.radians(x))
	str = input()
