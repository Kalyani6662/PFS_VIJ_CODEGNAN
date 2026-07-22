#Functions - A function is a block of organized, reusable code and that is used to perform a single or multiple tasks.
#python gives inbuilt functions like print,you can make your own function also and these are called user defined functions.
#python blocks begin with the keyword def followed by the function name and paranthesis-(()).
'''a=10
b=20
print(a+b)
print(a-b)
print(a*b)
a=100
b=200
print(a+b)
print(a-b)
print(a*b)
a=1000
b=2000
print(a+b)
print(a-b)
print(a*b)'''

#functions
'''def calculate(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''a=int(input())
b=int(input())
def calculate(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
calculate(a,b)'''

'''a=int(input())
b=int(input())
def calculate(a,b):
    print(a/b)
    print(a%b)
    print(a**b)
calculate(a,b)'''

'''def add(a,b):
    print(a+b)
add(1,2)'''
#calling function
'''def cal():
    a=int(input())
    b=int(input())
    print(a+b)
cal()'''
#Using While loop
'''while True:
    def cal():
        a=int(input())
        b=int(input())
        print(a+b)
    cal()'''
#Recurrsion
'''def cal():
    a=int(input())
    b=int(input())
    print(a+b)
    cal()
cal()'''

'''def fullname():
    fname=input()
    lname=input()
    print((fname+" "+lname).title())
fullname()'''

#Difference between print and return - print just shows the human user input in a console - return will terminate the function and gives back a value from the function
'''def mul(a,b):
    print(a*b)
mul(3,5)'''
'''def mul(a,b):
    return a*b
print(mul(2,3))'''
#print v/s return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(3,2)'''

#return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(add(2,3))'''
#only one return 
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(add(2,3))'''
#splitbill
'''def bill():
    count_mem=int(input())
    bill_amount=int(input())
    c=bill_amount/count_mem
    return c
print(f"{bill():.2f}")'''
'''def bill():
    count_mem=int(input())
    bill_amount=int(input())
    c=bill_amount//count_mem
    return c
print("{:.2f}".format(bill()))'''
'''def bill():
    count_mem=int(input())
    bill_amount=int(input())
    c=bill_amount//count_mem
    return c
print(bill())'''

'''def bill():
    count_mem=int(input())
    bill_amount=int(input())
    c=bill_amount//count_mem
    print("bill is {}".format(c))
    print(f"bill is {c}")
bill()'''
'''def bill():
    count_mem=int(input())
    bill_amount=int(input())
    print("bill is {}".format(bill_amount//count_mem))
    print(f"bill is {bill_amount//count_mem}")
bill()'''

#Taskssss
#add,sub,mul-options
'''def options(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return add,sub,mul
def choose():
    a=int(input("Enter the number))
    b=int(input("Enter the number))
    option=int(input("Enter the option"))
    add,sub,mul=options(a,b)
    if option==1:
        return add
    elif option==2:
        return sub
    else:
        return mul
print(choose())'''
#Using Multiple def 
'''def add1(a,b):
    add=a+b
    return add
def sub1(a,b):
    sub=a-b
    return sub
def mul1(a,b):
    mul=a*b
    return mul
def choose():
    a=int(input("Enter the number1))
    b=int(input("Enter the number2"))
    option=int(input("Enter the option))
    add=add1(a,b)
    sub=sub1(a,b)
    mul=mul1(a,b)
    if option==1:
        return add
    elif option==2:
        return sub
    elif option==3:
        return mul
print(choose())'''
#Multiple def
'''def sub():
    print(a-b)
def add():
    print(a+b)
def mul():
    print(a*b)
while True:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    option = int(input(Enter your choice
                       1.add
                       2.sub
                       3.mul))
    if option==1:
        sub()
    elif option==2:
        add()
    elif option==3:
       mul()'''
#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="kalyani"
    mailid="k@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
#Output--- 10 kalyani k@gmail.com'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="kalyani",mailid="kalyani@gmail.com")
Details(id=30,name="pooja",mailid="p@gmail.com")
Details(40,"nikitha","n@gmail.com")
Details("nikitha",50,"p@gmail.com")
Details(mailid="p@gmail.com",name="pooja",id=30)'''
#Outputs---
'''id name mailid
20 kalyani kalyani@gmail.com
30 pooja p@gmail.com
40 nikitha n@gmail.com
nikitha 50 p@gmail.com
30 pooja p@gmail.com'''

#Default arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %f" %price)
Grocery()'''

'''def Grocery(item,price=250):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''
#it shows error because never gives first argument value and next one empty.gives only first one empty after that empty or value.(non def argument follows def arg)
'''def Grocery(item="rice",price):
    print("item is %s" %item)
    print("price is %f" %price)
Grocery(1000)'''

#Tasksssssssssss
#cake_name,price,qty
'''def Bakery(cake_name,price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %f" %price)
    print("qty is %d" %qty)
Bakery("blackforest",500,1)'''

'''def Bakery(cake_name="redvelvet",price=600,qty=1):
    print("cake_name is %s" %cake_name)
    print("price is %f" %price)
    print("qty is %d" %qty)
Bakery()'''

'''def Bakery(cake_name,price=1590,qty=1):
    print("cake_name is %s" %cake_name)
    print("price is %f" %price)
    print("qty is %d" %qty)
Bakery("vennela")'''

'''def Bakery(cake_name="butterscotch",price,qty=1):
    print("cake_name is %s" %cake_name)
    print("price is %f" %price)
    print("qty is %d" %qty)
Bakery(1500)#--------It shows error non def argument follows def arg'''

#* arguments(* is used to unpack the elements)
'''a=[1,2,3,4,5]
print(a)
print(*a)'''

'''a=(1,4,5,6)
print(*a)'''

'''a={1,4,6,7,8}
print(*a)'''

'''b={"name":"pooja","city":"vij"}
print(*b)------>only keys will unpack in dict'''

'''c="python"
print(*c)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)->errorrr'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''

'''*a,b,*c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(*c)--->error-multiple stars not allowed'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)---->error-more values than limit to unpack'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,*b,c="codegnan"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

#variable length aruments are automatically stores in tuple and we use star arguments.
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6)
b=[1,2,4,5,6]
check(*b)
c={1,2,3,4,5,6}
check(*c)
d={"name":"pooja","age":28,"place":"vij"}
check(*d)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i)==int or type(i)==float:  
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"python")'''

#**(kwargs)(*---tuple)(**-----dictionary)
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)
def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''
#both * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
final()
data=(2,3,4,5,6,2.0,4.5)
final(*data)
details={"year":[2024,2025,2026],
         "month":["june","july","august"]}
final(**details)
final(*data,**details)'''

#tasksss
'''while True:
    def railway():
        ticket=int(input("Enter the ticket price"))
        option=int(input(Enter the option
                         1.female
                         2.male))
        age=int(input("Enter the age"))
        if option==1:
            if age>=60:
                print(ticket*30/100)
            else:
                print(ticket)
        elif option==2:
            if age>=60:
                print(ticket*50/100)
            else:
                print(ticket*30/100)
    railway()'''

#global and local variables --- variables inside and outside the function is called global and local variables.
#A variable is defined above the fuction and is accessible to the entire global space is called global variable.
#Variable is inside the fuction is called local variable.

#first case of global variable
'''a=4
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)

output-->
inside value is 4
outside value is 4'''

#second case of global variable
'''a=2
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)
#output ---->
inside value is 25
outside value is 2'''
#third case of global variable
'''a=6
def check3():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=13#local variable bcoz outside the function b is not initialized so it is a local variable and it cannot print in the outside function. 
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)--> not display 
#output ---
#inside value is 8
#updated value is 15
#value of b is 23
#a value is 6'''

'''a=6
b=9
def check3():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=13
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)
# output-->inside value is 8
updated value is 15
value of b is 23
a value is 6
b value is 9'''

#usage of global keyword --- DEFINITION
#when user wants to access the global variable inside the function directly and carry forward the updated value even outside the function then we need to use gloabl keyword
#the another name of global and local variables are scope of the variables.
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("updated values is",a)
    b=20
    b=b+a
    print("the value of b is",b)
final()
print("a value is",a)
print("b value is",b)
#output --->
inside value is 4
updated values is 15
the value of b is 35
a value is 15
b value is 35'''


#Taskssssss
#Attendance Tracker
'''student=int(input("Enter the Strength of class"))
present=0
absent=0
for i in range(1,student+1):
    attendance=input(f"student {i} present/absent")
    if attendance=="p":
        present+=1
    else:
        absent+=1
print("............Attendance Report.............")
print("......Total strength of class.............",student)
print("............Total presenties..............",present)
print("...........Total absenties................",absent)'''

#Tasksssss
#patterns
'''1)right angle
2)reverse right angle
3)square
4)pyramid'''

#generators
#no tuple comprehension in above cases if we remove those braces and keep paranthesis then the outcome is generated----definition
#(exp for var in collection/range)
a=(i for i in range(16))
'''print(*a)
print(type(a))'''

'''b=list(a)
print(b)
print(type(b))'''

'''b=tuple(a)
print(b)
print(type(b))'''

'''b=set(a)
print(b)
print(type(b))'''

#definition -----(generators)-----> A generator is also a function which can be used as an iterator (loop) by producing group of values, where we can used yield keyword.
#yield vs return ------> Return will terminate the function where as yield can pause the function and go on with every successive iteration.
'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
    return a
print(check(a,b))'''
#yield v/s return
'''def mygen():
    return "vij"
    return "hyd"
    return "vzg"
print(*mygen())'''

'''def mygen():
    #return "vij"
    #return "hyd"
    #return "vzg"
    return "vij","hyd","vzg"
print(*mygen())'''

def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())

#next
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#here the iteration stopped so outcomes comes error on this line

     
     
     
     
            
        
        



    
        
        
        





