Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=4;b=9
print(a+b)
13
a,b=2,3
print(a+b)
5
a,b,c=2,3,4
print(a,b,c)
2 3 4
>>> a,b,c=2,3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 7)
>>> a,b,c=(3,4,5)
>>> print(a,b,c)
3 4 5
>>> #above is called as unpack
>>> first name="pooja"
SyntaxError: invalid syntax
>>> first_name="kalyani"
>>> print(first_name)
kalyani
>>> firstname="pooja"
>>> print(firstname)
pooja
>>> fname="pooja"
>>> lname="ch"
>>> print(fname+lname)
poojach
>>> print(fname+" "+lname)
pooja ch
>>> print(fname,lname)
pooja ch
>>> #above is called concatination
>>> name="pooja"
>>> print(name)
pooja
>>> NAME="pooja"
>>> print("NAME")
NAME
>>> Name="pooja"
>>> print(Name)
pooja
>>> #above is called as case sensitive
>>> a=4
>>> print(a)
4
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> # above is called as delete keyword
