Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arithmatic operators
>>> a=2
>>> b=4
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a//b)
0
>>> print(a/b)
0.5
>>> print(a**b)
16
>>> print(a%b)
2
>>> #assignment Operators
>>> n=4
>>> m=5
>>> n+=m
>>> n
9
>>> n-=4
>>> 
>>> n
5
>>> n*=m
>>> n
25
>>> n//=m
>>> n
5
>>> m
5
>>> n/=m
>>> n
1.0
>>> n%m
1.0
>>> n
1.0
>>> m
5
>>> 
#comparison Operators
g=6
h=8
a>m
False
g<h
True
g<=h
True
g>=
SyntaxError: invalid syntax
g>=h
False
g!=h
True
g==h
False
#logical Operators
r=4
g=7
r and g
7
r or g
4
r not g
SyntaxError: invalid syntax
k=3
l=5
k<l and l>k
True
k>l and l>k
False
k!=l and l>k
True
k!=l and l!=k
True
k<l or l>k
True
k!=l or k==l
True
k<=l or l<=k
True
not True
False
not False
True
#Identify Operators
o=9
type(o) is int
True
type(o) is not int
False
n=4.5
type(n) is float
True
type(n) is not float
False
#Membership Operators
f=3,4,5,6,7,8
6 in f
True
10 in f
False
3 not in f
False
23 not in f
True
