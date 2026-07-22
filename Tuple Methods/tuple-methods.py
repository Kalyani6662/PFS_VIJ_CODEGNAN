Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #TUPLE()
>>> a=(4,5.6,"python",5+9j,True)
>>> print(a)
(4, 5.6, 'python', (5+9j), True)
>>> type(a)
<class 'tuple'>
>>> a.count(5+9j)
1
>>> a.index(True)
4
>>> len(a)
5
>>> #sets
>>> #set is a semi mutable
>>> #set is a unorder connection
>>> #it doesnt consider any repaeted order
>>> a={"python",3,5+9j,True)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a={"python",3,5+9j,True}
>>> print(a)
{(5+9j), True, 3, 'python'}
>>> #like above set is an unorder
>>> type(a)
<class 'set'>
>>> #methods of sets
>>> a={3,4,5,6,7,8}
>>> b={5,6,7,2,4,9}
>>> a.issubset(b)
False
>>> b.issubset(a)
False
>>> b=(5,6,7}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> b={5,6,7}
>>> b.issubset(a)
True
>>> a.issuperset(b)
True
a.union(b)
{3, 4, 5, 6, 7, 8}
c={1,2,3,4,5}
d={6,7,8,9,2}
c.union(d)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#intersection()
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
#update
a={10,20,30,40,50}
b={40,50,60,70,80}
a
{50, 20, 40, 10, 30}
a.update(b)
a
{70, 40, 10, 80, 50, 20, 60, 30}
a.difference(b)
{10, 20, 30}
a.symmetric_difference(b)
{20, 10, 30}
b.symmetric_difference(a)
{10, 20, 30}
a.intersection_update(b)
a
{70, 40, 80, 50, 60}
b
{80, 50, 70, 40, 60}
e={1,3,5,7,9}
f={5,3,2,6,8}
e.intersection_update(f)
e
{3, 5}
f
{2, 3, 5, 6, 8}
f.intersection_update(e)
f
{3, 5}
s={3,4,5,6,7}
r={1,2,3,4,5}
s.difference_update(r)
s
{6, 7}
r
{1, 2, 3, 4, 5}
a={11,12,13,14,15,16,17,18}
b={21,22,23,24,15,16,17,28}
a.symmetric_difference_update(b)
a
{11, 12, 13, 14, 18, 21, 22, 23, 24, 28}
b
{15, 16, 17, 21, 22, 23, 24, 28}
a.discard(28)
a
{11, 12, 13, 14, 18, 21, 22, 23, 24}
a.copy()
{11, 12, 13, 14, 18, 21, 22, 23, 24}
a.clear()
a.isdisjoint(b)
True
