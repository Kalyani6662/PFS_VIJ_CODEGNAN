Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#length - no of characters in a string is called length ->len()
a="python"
len(a)
6
b="pooja"
len(b)
5
c=""
len(c)
0
#count - no of repeated characters or words in a letter
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("a")
1
a.count(" ")
3
#method mundhu variable . vundali pakkaga
#find a string
a="code"
a.find(d)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.find(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
a.find("d")
2
KeyboardInterrupt
#2 letters vunte 1st letter position vastundhi
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobile number\tmailid\nclg"
print(a)
name
mobile number	mailid
clg
b="name:kalyani\nmobile number:9391256662\tmailid:kalyanikondapalli0@gmail.com\nclg:vignan's university"
print(b)
name:kalyani
mobile number:9391256662	mailid:kalyanikondapalli0@gmail.com
clg:vignan's university
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#upper case
a=hello
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a=hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
a="hello"
a.upper()
'HELLO'
#Lower Case
b="pooja"
b="POOJA"
b.lower()
'pooja'
#only p capital avali ante
#capitalize
c="python"
c[0].upper()
'P'
>>> c.capitalize()
'Python'
>>> # All words lo first letter capital avvali appudu title()
>>> a="python course"
>>> a.title()
'Python Course'
>>> b="i am in class"
>>> b.title()
'I Am In Class'
>>> #True or Flase conditions
>>> a="java"
>>> a.isupper()
False
>>> a.islower()
True
>>> a.isdigit()
False
>>> a.isalpha()
True
>>> b="python course"
>>> b.isalpha()
False
>>> #isalpha means alphabets
>>> c="pythoncourse"
>>> c.isalpha
<built-in method isalpha of str object at 0x000001FE94D0BEB0>
>>> c.isalpha()
True
>>> d=1234
>>> d.isdigit()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> d="1234"
>>> d.isdigit()
True
>>> #isdigit() ante anni digits ee vundali
>>> d.isalnum()
True
>>> #isalnum() ante alphabets or numbers vundali
>>> e="pooja1234"
>>> e.isalnum()
True
>>> f="pooja@1234"
>>> f.isalnum()
False
a="hello python"
a.startswith("h")
True
a.endswith("n")
True
#strip() -> it is used to remove the white spaces
#lstrip() -> it will remove the left spaces
#rstrip() -> it will remove the right spaces
a="                 python             "
a.strip()
'python'
a.lstrip()
'python             '
a.rstrip()
'                 python'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
a="a b c d"
a.split()
['a', 'b', 'c', 'd']
#join
a="vijhydviz"
"".join(a)
'vijhydviz'
a="vij","hyd","viz"
"".join(a)
'vijhydviz'
" ".join(a)
'vij hyd viz'
"k".join(a)
'vijkhydkviz'
#Concatination
a="hello"
b="word"
print(a+b)
helloword
print(a+" "+b)
hello word
fname="kalyani"
lname="kondapalli"
print(fname+" "+lname)
kalyani kondapalli
print(fname.title()+" "+lname.title())
Kalyani Kondapalli
print((fname+" "+lname).title())
Kalyani Kondapalli
print(fname.capitalize()+" "+lname.capitalize())
Kalyani Kondapalli
print(fname.capitalize()+" "+lname)
Kalyani kondapalli
#formatting
a=4
b=8
print("the sum is",a+b)
the sum is 12
x="kalyani"
print("my name is",x)
my name is kalyani
#.format method
a="motu"
b="pathulu"
print("hello {}{}).format(a,b)
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello" {}{}).format(a,b)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("hello", {}{}).format(a,b)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("hello {}{}".format(a,b))
      
hello motupathulu
print("hello {} {}".format(a,b))
      
hello motu pathulu
print("hello {} hello{}".format(a,b))
      
hello motu hellopathulu
print("hello {} hello {}".format(a,b))
      
hello motu hello pathulu
#fstring
      
a="sita"
      
b="rama"
      
print(f"hello {a}{b}")
      
hello sitarama
print(f"hello {a} {b}")
      
hello sita rama
print(f"hello {a} hello {b}")
      
hello sita hello rama
a=4
      
b=5
      
print(f"The Product is {a*b}")
      
The Product is 20
print("The product is".format(a*b))
      
The product is
