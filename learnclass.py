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