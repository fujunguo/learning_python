from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print()

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
print(c.x, c.y, c.r)
print()

# deque是为了高效实现插入和删除操作的双向列表，适用于队列和栈
# list插入和删除效率很低
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
print()

# defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
print()

# OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)])
print(d)
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))
print()

# Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
