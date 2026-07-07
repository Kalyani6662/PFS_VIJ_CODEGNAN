#conditions
#if-condition by using comparison operator
'''a=10
b=20
if a<b:
    print("True")'''
'''a=10
b=20
if a>b:
    print("True")'''
'''a=20
b=10
if a>b:
    print("True")'''
'''a=10
b=20
if a>=b:
    print("True")'''
'''a=20
b=10
if a>=b:
    print("True")'''
'''a=5
b=7
if a<=b:
    print("less")'''
'''a=12
b=15
if a>=b:
    print("true")'''
'''a=15
b=12
if a>=b:
    print("True")'''
'''a=30
b=40
if a!=b:
    print("true")'''
'''a=10
b=10
if a==b:
    print("equal")'''
'''a="python"
if a=="python":
    print("same")'''
'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("True")'''
'''a=int(input("a value"))
if a>50:
    print("true")'''
'''a=3
b=6
if a<b and b>a:
    print("true")'''
'''a=4
b=7
if a<=b and b>=a:
    print("true")'''
'''a=9
b=12
if a!=b and a==b:
    print("true")'''
'''a=9
b=12
if a!=b or a==b:
    print("true")'''
'''a=2
b=4
if a>b and b<a:
    print("true")'''
'''a=2
b=4
if a>b or b<a:
    print("true")'''
'''a=14
b=16
if a<=b or b>=a:
    print("true")'''
'''a=14
b=16
if not a>b:
    print("true")'''
'''a=16
b=14
if not a<b:
    print("true")'''
'''a=16
b=14
if not a>=b:
    print("True")'''
'''a=16
b=14
if not a<=b:
    print("true")'''
'''a=16
b=16
if not a==b:
    print("true")'''
'''a=13
b=14
if not a>b and a<b:
    print("true")'''
'''a=13
b=14
if not a<b or a<b:
    print("true")'''
#if using identify operator
#is,is not
'''a=4
if type(a) is int:
    print("it is int")'''
'''a=4
if type(a) is not int:
    print("it is int")'''
'''a=4.5
if type(a) is float:
    print("It is float")'''
'''a=4.5
if type(a) is not float:
    print("It is float")'''
'''a="python"
if type(a) is str:
    print("It is string")'''
'''a="python"
if type(a) is not str:
    print("It is string")'''
'''a=True
if type(a) is bool:
    print("It is bool")'''
'''a=True
if type(a) is not bool:
    print("It is bool")'''
'''a=5+9j
if type(a) is complex:
    print("It is complex")'''
'''a=5+9j
if type(a) is not complex:
    print("It is complex")'''
#if using membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("True")'''
'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("True")'''
'''a=2,3,4,5,6,7
if 20 not in a:
    print("True")'''
'''a=int(input("a value"))
if 30 in a:
      print("True")'''#error
'''a=2,3,4,5,6,7,8,9
b=int(input("b value"))
if b in a:
    print("true")'''
#if-else using comparison operators
'''a=4
b=8
if a<b:
    print("True")
else:
    print("False")'''
'''a=5
b=8
if a>b:
    print("True")
else:
    print("False")'''
'''a=4
b=8
if a<=b:
    print("True")
else:
    print("False")'''
'''a=4
b=8
if a>=b:
    print("True")
else:
    print("False")'''
'''a=4
b=8
if a!=b:
    print("True")
else:
    print("False")'''
'''a=4
b=8
if a==b:
    print("True")
else:
    print("False")'''
#if-else using identify operators
'''a=4
if type(a) is int:
    print("it is int")
else:
    print("it is not int")'''
'''a=4.0
if type(a) is float:
    print("it is float")
else:
    print("it is not float")'''
'''a="python"
if type(a) is str:
    print("it is str")
else:
    print("it is not str")'''
'''a=True
if type(a) is bool:
    print("It is bool")
else:
    print("It is not bool")'''
'''a=5+9j
if type(a) is not complex:
    print("It is complex")
else:
    print("It is not complex")'''
#if-else using membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("True")
else:
    print("flase")'''
'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("True")
else:
    print("flase")'''
'''a=2,3,4,5,6,7
if 20 not in a:
    print("True")
else:
    print("False")'''
#if-else using logical operator
'''a=3
b=6
if a<b and b>a:
    print("true")
else:
    print("false")'''
'''a=3
b=4
if a<b and b>a:
    print("true")
else:
    print("false")'''
'''a=4
b=7
if a<=b and b>=a:
    print("true")
else:
    print("false")'''
'''a=9
b=12
if a!=b and a==b:
    print("true")'''
'''a=9
b=12
if a!=b or a==b:
    print("true")'''
'''a=2
b=4
if a>b and b<a:
    print("true")
else:
    print("false")'''
'''a=2
b=4
if a>b or b<a:
    print("true")
else:
    print("false")'''
'''a=14
b=16
if a<=b or b>=a:
    print("true")
else:
    print("false")'''
'''a=14
b=16
if not a>b:
    print("true")
else:
    print("false")'''
'''a=16
b=14
if not a<b:
    print("true")
else:
    print("false")'''
'''a=16
b=14
if not a>=b:
    print("True")
else:
    print("false")'''
'''a=16
b=14
if not a<=b:
    print("true")
else:
    print("false")'''
'''a=16
b=16
if not a==b:
    print("true")
else:
    print("false")'''
'''a=13
b=14
if not a>b and a<b:
    print("true")
else:
    print("false")'''




    
    
    
