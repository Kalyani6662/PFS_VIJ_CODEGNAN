#loops()
#for,while,range,break,continue,pass
#for loop()

'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={5,6,7,8,9}
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''b={"year":2026,"month":"july","date":9}
for i in b:
    print(i)
    print(type(b))
    print(type(i))
for i in b.keys():
    print(i)
for i in b.values():
    print(i)
    print(type(b))
    print(type(i))
for i in b.items():
    print(i)
    print(type(b))
    print(type(i))'''

'''a="codegnan"
for i in a:
    print(i)'''

'''b=[4.5,5.6,7.8]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''
'''c=[True,False]
for i in c:
    print(i)
    print(type(c))
    print(type(i))'''

'''d=[2+5j,7+8j]
for i in d:
    print(i)
    print(type(d))
    print(type(i))'''

#Tasksssssssssssssssssssssss
'''a=["apple","banana","mango"]
b=str(a)
print(b.upper())'''

'''a=["apple","banana","mango"]
for i in a:
    print(i.upper(),end=" ")'''

'''fruits=["apple","banana","mango"]
b=[]
for i in fruits:
    b.append(i.upper())
print(b)'''

#2nd task
'''a=[1,3,5,7,9,"code"]
a.extend("code")
print(a)'''

#While loop()
'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=20
while a>3:
    a=a-1
    print(a)'''

'''a=20
while a>3:
    a=a-1
print(a)'''

'''a=40
while a>5:
    a=a-1
print(a)'''

'''a=30
while a>1:
    print(a)
    a+=1'''
'''a=10
while a>2:
    print(a)
    a-=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=1
while a<25:
    print(a)
    a+=1'''

'''#Bakery
while True:
    a=int(input("enter"))
    if a==1200:
        print("redvelvet cake")
    elif a==1000:
        print("almond cake")
    elif a==800:
        print("chocolate cake")
    elif a==600:
        print("butter scotch cake")
    else:
        print("cake is not available")'''

#range()- The range function returns a sequence of numbers,starting from zero by default and increaments by one by one and stops before a specified number.
#start-stop-step
#stop
'''for i in range(20):
    print(i)'''
#start,stop
'''for i in range(13,35):
    print(i)'''
#start-stop-step tasks
'''for i in range(0,30,3):
    print(i)'''

'''for i in range(5,50,5):
    print(i)'''

'''for i in range(2,20,2):
    print(i)'''

#Tasksssssssssss
'''while True:
    marks=int(input())
    if marks>=91 and marks<101:
        print("Grade A")
    elif marks>=81 and marks<91:
        print("Grade B")
    if marks>=70 and marks<81:
        print("Grade C")
    if marks>=50 and marks<71:
        print("Grade D")
    else:
        print("Fail")'''

while True:
    marks=int(input())
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    if marks in range(71,81):
        print("Grade C")
    if marks in range(50,71):
        print("Grade D")
    else:
        print("Fail.............")



    


    




    
    
    

    


    


    




    
    
    

    
