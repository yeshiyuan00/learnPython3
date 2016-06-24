from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p=Point(1,2)
print('p.x=%s' % p.x)
print('p.y=%d' % p.y)

print(isinstance(p,Point))
print(isinstance(p,tuple))

from collections import deque
q=deque(['a','b','c',])
q.append('x')
q.appendleft('y')
print('q=',q)


from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])



# from collections import OrdereDict
# d=dict([('a',1),('b',2),('c',3)])
# print('d=',d)
# od=OrdereDict([('a',1),('b',2),('c',3)])
# print('od=',od)

from collections import Counter
c=Counter()
for ch in 'programming':
	c[ch]=c[ch]+1

print(c)



