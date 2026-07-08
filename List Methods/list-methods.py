Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[2,5.6,"python"]
>>> print(type(a))
<class 'list'>
>>> a=[True,False]
>>> print(type(a))
<class 'list'>
>>> a=["python","java","c","c++"]
>>> a.append("DSA")
>>> a
['python', 'java', 'c', 'c++', 'DSA']
>>> a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ml","ai"])
>>> a
['python', 'java', 'c', 'c++', 'DSA', ['ml', 'ai']]
>>> #extend
>>> a=["ml","ai","ds"]
>>> a.extend(["c","c++","pyton"})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a.extend(["c","c++","pyton"])
>>> a
['ml', 'ai', 'ds', 'c', 'c++', 'pyton']
>>> #insert()
>>> b=["viz","hyd"]
>>> b.insert(1,"vzg")
>>> b
['viz', 'vzg', 'hyd']
>>> a=["black","red","white"]
>>> a.index("white")
2
>>> a.copy()
['black', 'red', 'white']
>>> b.copy()
['viz', 'vzg', 'hyd']
b=a.copy()
b
['black', 'red', 'white']
b.count("pink")
0
b.count("red")
1
a.sort()
a
['black', 'red', 'white']
b=[3,4,2,5,8,5,7]
b.sort()
b
[2, 3, 4, 5, 5, 7, 8]
a=[7,8,9,10,12,40,60]
a.reverse()
a
[60, 40, 12, 10, 9, 8, 7]
b["pink","red","white"]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b["pink","red","white"]
TypeError: list indices must be integers or slices, not tuple
b=["pink","red","white"]
b.reverse()
b
['white', 'red', 'pink']
a.pop()
7
b.pop()
'pink'
b
['white', 'red']
b.pop("red")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b.pop("red")
TypeError: 'str' object cannot be interpreted as an integer
b.pop(1)
'red'
b
['white']
b.remove("white")
b
[]
b=["pooja","sweety","cherry","kalyani"]
len(b)
4
a.clear()
a
[]
