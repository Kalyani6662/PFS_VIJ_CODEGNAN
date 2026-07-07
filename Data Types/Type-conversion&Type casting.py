Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=10
type(a)
<class 'int'>
b=4.5
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
d="code"
type(d)
<class 'str'>
e="'code'"
type(e)
<class 'str'>
f=True
type(f)
<class 'bool'>
g=False
type(g)
<class 'bool'>
h=3+2j
type(h)
<class 'complex'>
i=2j
type(i)
<class 'complex'>
#this is called as Type Casting
#Now DataType Conversions
int(3)
3
int(3.4)
3
int("python")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(2+3j)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(2+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(1)
1.0
float(1.0)
1.0
float("string")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float("string")
ValueError: could not convert string to float: 'string'
float(2+3j)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(2+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
string(1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    string(1)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string(1.0)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    string(1.0)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string(True)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    string(True)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> string(False)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    string(False)
NameError: name 'string' is not defined. Did you forget to import 'string'?
s
>>> string(2+3j)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    string(2+3j)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> complex(1)
(1+0j)
>>> complex(1.0)
(1+0j)
>>> complex(True)
(1+0j)
>>> complex("pooja")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex("pooja")
ValueError: complex() arg is a malformed string
>>> complex(False)
0j
>>> bool(1)
True
>>> bool(0)
False
>>> bool("string")
True
>>> bool(True)
True
>>> bool(2+3j)
True
>>> str(1)
'1'
>>> str(True)
'True'
>>> str("google")
'google'
>>> str(2+3j)
'(2+3j)'
