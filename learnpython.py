#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello,world')
print(100+200+300)
#name=input('please enter your name:')
#print('hello',name)
print('I\'m \"ok\"!')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
...line2
...line3''')

print(u'中文测试正常')
print('Age: %s. Gender: %s' % (25,True))
print('growth rate: %d %%' % 7)

#使用list和tuple
classmates = ['Michael','Bob','Tracy']
print(classmates,'length=',len(classmates),'classmates[2]=',classmates[-1])
classmates.append('Adam')
print(classmates)
classmates.insert(1,'Jack')
print(classmates)
classmates.pop(1)
print(classmates)
s=['python','java',['asp','php'],True]
print(len(s),s[2][1])

#tuple一旦初始化就不能修改
classmates2=('Michael','Bob','Tracy')
#一个元素的tuple
t=(1,)
#可变tuple
t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)


#条件判断
age=20
if age>=18:
	print('your age is',age)
	print('adult')
else:
	print('your age is',age)
	print('teenager')

age=3
print('your age is',age)
if age>=18:
	print('adult')
elif age>=6:
	print('teenager')
else:
	print('kid')

#s=input('birth:')
s=2000
birth=int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')


#循环
names=['Michael','Bob','Tracy']
for name in names:
	print(name)

print(list(range(5)))

sum=0
for x in range(101):
	sum=sum+x
print(sum)

sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print(sum)

#使用dict和set
d={'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
d['Adam']=67
print(d['Adam'])
print('Thomas' in d,d.get('yeshiyuan'),d.get('Thomas',-1))
d.pop('Bob')
print(d)
#set
s=set([1,2,3])
print(s)
s.add(4)
s.add(4)
print(s)
s.remove(4)
print(s)
s2=set([2,3,4])
print(s & s2)
print(s | s2)

a='abc'
print(a.replace('a','A'))
print(a)
a='abc'
b=a.replace('a','A')
print(a)
print(b)
#homework
x=(1,2,3)
y=(1,[2,3])
z=set(x)
print(z)
#z=set(y)
print(z)

#数据类型转换
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(''))

#函数	
a=abs #变量a指向abs函数	
print(a(-1))

#定义函数
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type1')
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-3))
#print(my_abs('x'))

#空函数
def nop():
	pass

#返回多个值
import math
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny

x,y=move(100,100,60,math.pi/6)
z=move(100,100,60,math.pi/6)
print(x,y)
print(z)

#函数的参数
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print(power(5),power(5,3))

#默认参数
def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:,',city)

enroll('Sarah','F')
enroll('Bob','M',7)
enroll('Adam','M',city='Tianjin')

#可变参数
def cale(*numbers):
	sum = 0
	for n in numbers:
		sum=sum+n*n
	return sum

print(cale(1,2))
print(cale(1,2,3))
print(cale())
nums=[1,2,3]
print(cale(*nums))

#切片
L=['Michael','Sarah','Tracy','Bob','Jack']
print(L[0:3])
print(L[:2])
print(L[1:3])
print(L[-2:])

L=list(range(100))
print(L)
print(L[:10:2])
print(L[::5])  #所有数，每5个取一个
print(L[:])    #什么都不写，只写[:]就可以原样复制一个list
#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0,1,2,3,4,5)[:3])
print('ABCDEFG'[:3])

#迭代
print('迭代.......')
d={'a':1,'b':2,'c':3}
for key in d:
	print(key)
	
for value in d.values():
	print(value)

#同时迭代key和value
for k,y in d.items():
	print(k,y)

for ch in 'ABC':
	print(ch)

from collections import Iterable
print(isinstance('abc',Iterable)) # str是否可迭代
print(isinstance(123, Iterable)) # 整数是否可迭代

#把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
	print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
	print(x,y)


#列表生成式
print('列表生成式......')
print(list(range(1,11)))

L=[]
for x in range(1,11):
	L.append(x*x)

print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x % 2== 0])
print([m+n for m in 'ABC' for n in 'XYZ'])

import os #导入os模块
print([d for d in os.listdir('.')]) #os.listdir可以列出文件和目录

d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])
#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#生成器
print('生成器......')
L=[x*x for x in range(10)]
print(L)
g=(x*x for x in range(10))
print(g)
print(next(g))
for n in g:
	print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f=fib(6)
print(f)

def odd():
	print('step1')
	yield 1
	print('step2')
	yield 3
	print('step3')
	yield 5
o=odd()
next(o)
next(o)
next(o)

g=fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:   #想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
		print('Generator return value:',e.value)
		break

#函数式编程
#高阶函数
#传入参数
def add(x,y,f):
	return f(x)+f(y)

print(add(-5,6,abs))

#map/reduce
def f(x):
	return x*x

r=map(f,[1,2,3,4,5,6,7,8,9,])
print(list(r))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

from functools import reduce
def add(x,y):
	return x+y

print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
	return x*10+y

print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print(reduce(fn,map(char2num,'13579')))

#整合
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))
print(str2int('12345'))

#简化
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))

print(str2int('67890'))

#练习3
def str2float(s):
    def del_dot(s):
        return s.replace('.', '')

    def str2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    _result = reduce(lambda x, y: x * 10 + y, map(str2num, del_dot(s)))

    if s.find('.') == -1:
        return _result
    else:
        return _result / (10 ** (len(s) - s.find('.') - 1))


print('str2float(\'123.456\') =', str2float('123.456'))

#filter
def is_odd(n):
	return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10,15])))

#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'C',' '])))

#sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

#返回函数
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum
#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f=lazy_sum(1,3,5,7,9)
print(f)
#调用函数f时，才真正计算求和的结果：
print(f())
#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f2=lazy_sum(1,3,5,7,9);
print(f==f2)

#闭包
def count():
	fs=[]
	for i in range(1,4):
		def f():
		    return i*i
		fs.append(f)
	return fs
f1,f2,f3=count()
print(f1(),f2(),f3())
#返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i)) #f(i)被立即执行，因此i的当前值被传入f（）
	return fs
f1,f2,f3=count()
print(f1(),f2(),f3())


#关键字lambad表示匿名函数，冒号前面的x表示函数参数

#装饰器
print('装饰器')
def now():
	print('2016-02-19')
f=now
f();
print(now.__name__)
print(f.__name__)

def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2016-02-19')
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
now()

def log(text):
	def dectorator(func):
		def wrapper(*args,**kw):
			print('%s %s()' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return dectorator

@log('execute')
def now():
	print('2015-02-19')

now()

#和两层嵌套的decorator相比，3层嵌套的效果是这样的 
#now = log('execute')(now)
print('now.name=',now.__name__)

import functools

def log(func):
    @functools.wraps(func)  #wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int,base=2)
print(int2('1010101'))


#模块
#使用模块
