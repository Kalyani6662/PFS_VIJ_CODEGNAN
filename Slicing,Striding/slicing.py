Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
#The updated version of this concept is Slicing
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[:8]
'codegnan'
a[4:]
'gnan'
b="work until you succeed
SyntaxError: unterminated string literal (detected at line 1)
b="work until you succeed"
b[7:12]
'til y'
b[5:10]
'until'
b[12:15]
'ou '
b[11:15]
'you '
b[11:14]
'you'
b[:4]
'work'
c="codegnan it solutions"
c=[9:11]
SyntaxError: invalid syntax
c[9:11]
'it'
>>> c[:8]
'codegnan'
>>> c[12:20]
'solution'
>>> c[12:21]
'solutions'
>>> #Negative Slicing
>>> d="Vijayawada is a royal city"
>>> d[-10:-5]
'royal'
>>> d[:-16]
'Vijayawada'
>>> d[-5:]
' city'
>>> d[-4:]
'city'
>>> f="Vizag is city of destiny"
>>> f[-14:-19]
''
>>> f[-15:-11]
'city'
>>> f[:-20]
'Viza'
>>> f[:-19]
'Vizag'
>>> f[-8:]
' destiny'
>>> f[-7:]
'destiny'
>>> #Striding
>>> a="Data Science"
>>> a[::]
'Data Science'
>>> a[::1]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a[::3]
'Dacn'
>>> a="cloud computing"
>>> a[::5]
'c u'
>>> #negative striding
>>> a="Python Course"
>>> a[-1:-10:-2]
'ero o'
