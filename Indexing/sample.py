Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="kalyani"
a[0]
'k'
a[0]+a[1]
'ka'
a[0]+a[1]+a[2]+a[3]
'kaly'
>>> b="I am in class"
>>> b[8]+b[9]+b[10]+b[11]+b[12]
'class'
>>> b[5]+b[6]
'in'
>>> b[1]
' '
>>> b[1]+b[4]+b[7]
'   '
>>> c="I am learning python course"
>>> c[5]+c[6]+c[7]+c[8]+c[9]+c[10]+c[11]+c[12]
'learning'
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'python'
>>> c[21]+c[22]+c[23]+c[24]+c[25]+c[26]
'course'
>>> d="Time is very precious"
>>> d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]+d[21]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]+d[21]
IndexError: string index out of range
>>> d="Time is very precious"
>>> d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]
'precious'
>>> d[8]+d[9]+d[10]+d[11]
'very'
>>> d[0]+d[1]+d[2]+d[3]
'Time'
>>> e="Simple is better than complex"
>>> e[-29]+e[-28]+e[-27]+e[-26]+e[-25]+e[-24]
'Simple'
>>> e[-22]+e[-21]
'is'
>>> e[-12]+e[-11]+e[-10]+e[-9]
'than'
>>> e[-7]+e[-6]+e[-5]+e[-4]+e[-3]+e[-2]+e[-1]
'complex'
>>> e[-19]+e[-18]+e[-17]+e[-16]+e[-15]+e[-14]
'better'
>>> e="I love Python"
>>> e[-11]+e[-10]+e[-9]+e[-8]
'love'
>>> e[-6]+e[-5]+e[-4]+e[-3]+e[-2]+e[-1]
'Python'
