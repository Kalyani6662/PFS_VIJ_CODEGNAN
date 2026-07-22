'''a = input().split()
for i in a:
    print(len(i))'''

'''a = input().split()
for i in a:
    print(i.capitalize())'''

'''a=input()
for i in a:
    c=a[5]
    e=a[3]
    f=a[1]
print(c,e,f)'''

'''a = input()
i = 0
while i < len(a):
    c=a[5]
    e=a[3]
    f=a[1]
    print(c,e,f)
    break'''

'''n=int(input())
for i in range(11):
    print(n,"*",i,"=",i*5)'''

'''n=int(input())
for i in range(10,-1,-1):
    print(n,"*",i,"=",i*5)'''

'''n=int(input())
m=int(input())
for i in range(11):
    for j in range(n):
        print(n,"*",i,"=",i*n)'''

'''a=int(input())
b=int(input())
for j in range(a):
    for i in range(b):
        print("*",end="")
    print()'''

'''a=int(input())
b=int(input())
for i in range(a):
    for j in range(b):
        print(i,end="")
    print()'''

'''a=int(input())
b=int(input())
for i in range(a):
    for j in range(b):
        print(i+1,end="")
    print()'''

'''a=int(input())
b=int(input())
for i in range(a):
    for j in range(b):
        print(b-i,end="")
    print()'''

'''a=int(input())
b=int(input())
for i in range(a):
    for j in range(b):
        print(j,end="")
    print()'''

'''a=int(input())
b=int(input())
for i in range(a):
    for j in range(b):
        print(b-1-j,end="")
    print()'''

'''n=5
for i in range(n):
    print("*"*n)'''

'''a=int(input())
b=int(input())
for i in range(5,0,-1):
    for j in range(b):
        print(i,end="")
    print()'''

'''a=int(input())
b=int(input())
for i in range(a):
    for j in range(0,4):
        print(j,end="")
    print()'''

'''a=int(input())
b=int(input())
for i in range(a):
    for j in range(1,6):
        print(j*2,end="")
    print()'''

'''for i in range(4,0,-1):
    for j in range(-5,-10,1):
        print(j,end="")
    print()'''

'''for i in range(3):
    for j in range(1,1,1):
        print(i)'''

'''for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i,j,k)
        print()'''

'''a=int(input())
if a&1==0:
    print("even")
else:
    print("odd")'''

'''for i in range(3):
    for j in range(1):
        for k in range(2):
            print(i,j,k)'''

'''for i in range(3):
    for j in range(3,0,-1):
        for k in range(2):
            print(i,j,k)'''

'''for i in range(1):
    for j in range(3,0,-1):
        for k in range(2):
            print(i+j+k)'''
'''a=[]
for i in range(3):
    for j in range(3):
        for k in range(3):
           a.append((i,j,k))
print(a)'''
'''n=5
for row in range(0,n+1):
    for col in range(n):
        b=(row+1)
    print(b*"*")'''
'''n=5
for i in range(1,n+1):
    for j in range(i):
        print(j,end="")
    print()'''

#value constant ga vunte ----> i
#value change avuthundhi ante ---->j
'''n=5
for i in range(1,n+2):
    for j in range(i):
        print("*",end="")
    print()'''
'''n=4
for i in range(n,0,-1):
    for j in range((n-i)+1):
        print("*",end="")
    print()'''
'''n=4
for i in range(n+1):
    for j in range((n-i)+1):
        print("*",end="")
    print()'''
'''n=4
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()'''
'''n=4
for i in range(n+1):
    for j in range(((n-i)+1)-1):
        print("*",end="")
    print()'''
'''n=4
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()'''
'''n=5
for i in range(n):
    for j in range(i+1):
        print(j+2,end="")
    print()'''
#Taskssssssssss
#Right Angle
'''n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()'''

#Reversed Right Angle
'''n=5
for i in range(n+1):
    for j in range((n+1)-i):
        print("*",end="")
    print()'''
#square
'''n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()'''
#pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print("*",end=" ")
    print()
        
               
            









