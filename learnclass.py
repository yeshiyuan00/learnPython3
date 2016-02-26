#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def print_score(self):
		print('%s: %s' % (self.__name,self.__score))

	def get_grade(self):
		if self.__score>=90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self,score):
		if 0<=score <= 100:
			self.__score=score
		else:
			raise ValueError('bad score')


bart = Student("Bart Simpon",59)
lisa = Student('Lisa Simpon',87)
bart.print_score()
print(bart.get_grade())
lisa.print_score()
print(lisa.get_grade())
bart.age=8
print(bart.age)
#print(lisa.age)
#print(lisa.__name)
print(bart._Student__name)  #强烈不建议


#继承和多态
print('继承和多态')
class Animal(object):
	def run(self):
		print("Animal is running...")

class Dog(Animal):
	def run(self):
		print('Dog is running...')

	def eat(self):
		print('Eating meat...')
class Cat(Animal):
	def run(self):
		print('Cat is running...')

dog=Dog()
dog.run()
cat=Cat()
cat.run()

print(isinstance(cat,Animal))

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())
run_twice(Dog())

#获取对象信息
print('获取对象信息')
print(type(123))
print(type(abs))
print(type(123)==type(456))
print(type('abc')==str)

import types
def fn():
	pass
print(type(fn)==types.FunctionType)
print(type(lambda x:x)==types.BuiltinFunctionType)
print(type((x for x in range(10)))==types.GeneratorType)


class Husky(Dog):
	pass
a=Animal()
d=Dog()
h=Husky()

print(isinstance(h,Husky))
print(isinstance(h,Dog))

print(isinstance([1,2,3],(list,tuple)))

print('使用dir获得一个对象的所有属性和方法')
print(dir('abc'))
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
	def __len__(self):
		return 100
dog=MyDog()
print(len(dog))


class MyObject(object):
    def __init__(self):
         self.x = 9
    def power(self):
       return self.x * self.x

obj = MyObject()

print(hasattr(obj,'x'))  #有属性'x'吗？
print(hasattr(obj,'y'))  #有属性'y'吗？
setattr(obj,'y',90) #设置一个属性'y'
print(getattr(obj,'y')) # 获取属性'y'
#getattr(obj, 'z') 报错
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

def readImage(fp):
	if hasattr(fp,'read'):
		return readData(fp)
	return None

#使用__slots__
print('使用__slots__')

class Student(object):
	pass

s=Student()
s.name='Michael' #给实例绑定一个属性
print(s.name)

def set_age(self,age):  # 定义一个函数做为实例方法
	self.age =age

from types import MethodType
s.set_age=MethodType(set_age,s) #给实例绑定一个方法
s.set_age(25)
print(s.age)

s2=Student()
#s2.set_age(25) 方法对另一个实例不起作用

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
	self.score=score

Student.set_score=MethodType(set_score,Student)

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

class Student(object):
	__slots__=('name','age') #用tuple定义允许绑定的属性名称

s=Student() # 创建新的实例
s.name='Michael'
s.age=25
# s.score=99

class Student(object):
	
	def get_score(self):
		return self._score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value<0 or value>100:
			raise ValueError('score must between 0~100!')
		self._score=value

s=Student()
s.set_score(60)
print(s.get_score())

class Student(object):

	@property
	def score(self):
	    return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value 

s=Student()
s.score=60  # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()

# 定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):

	@property
	def birth(self):
	    return self._birth

	@birth.setter
	def birth(self,value):
		self._birth=value

	@property
	def age(self):
	    return 2015-self.birth
	


#多重继承
print('多重继承')

class Animal(object):
	pass

#大类
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

#各种动物
class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

#######
class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')


class Dog(Mammal,Runnable):
	pass

class Bat(Mammal,Flyable):
	pass

#定制类
print('定制类')
class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__=__str__

print(Student('Michael'))

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1

	def __iter__(self):
		return self  # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值
		if self.a > 100000: # 退出循环的条件
			raise StopIteration()
		return self.a # 返回下一个值

for n in Fib():
	print(n)


class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int): # n是索引
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n, slice): # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

f=Fib()
print(f[0],f[1])
print(f[0:5])

class Student(object):

	def __init__(self):
		self.name = 'Michael'

	def __getattr__(self, attr):
		if attr=='score':
			return 99

	def __getattr__(self, attr):
		if attr=='age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s=Student()
print(s.name)
#print(s.score)

class Chain(object):

	def __init__(self,path=''):
		self.__path=path
	def __getattr__(self,path):
		return Chain('%s%s' % (self._path,path))

	def __str__(self):
		return self._path

	__repr__=__str__

#Chain().status.user.timeline.list


class Student(object):
	def __init__(self,name):
		self.name=name

	def __call__(self):
		 print('My name is %s.' % self.name)

s=Student('Michael')
s()
print(callable(Student('Michael')))

#枚举
print('枚举')
from enum import Enum

Month=Enum('Month',('JAN', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)

from enum import Enum,unique

@unique
class Weekday(Enum):
	sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6