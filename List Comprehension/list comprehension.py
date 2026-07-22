#List Comprehension
'''a=["codegnan","python","course"]'''
#1st process
'''b=str(a)
print(b.upper())'''
#2nd process but wrong 
'''for i in a:
    print(i.upper(),end=",")'''
#3rd process
'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''
#Idhi List Comprehension
#syntax
#a=[expr for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

#Taskss--1
'''b=["vij","hyd","viz"]
b=[i.capitalize() for i in b]
print(b)'''

#Taskss--2
'''a=[1,2,3,5,6,8,12,13]
#[1,4,9,25,36,64,144,169]
a=[i*i for i in a]
print(a)'''

#2nd method
'''a=[i**2 for i in a]
print(a)
#3rd method
a=[pow(i,2) for i in a]'''

#if-usage in list comprehension
#even
'''a=[i for i in range(16) if i%2==0]
print(a)'''
#odd
'''a=[i for i in range(16) if i%2!=0]
print(a)'''
#squares of even numbers
'''a=[i*i for i in range(21) if i%2==0]
print(a)'''
#print given letter fruits names are printed
'''a=["apple","banana","grapes","mango","kiwi","dragon","berry"]
a=[i for i in a if "a" in i]
print(a)'''

'''a=[i for i in a if "a" not in i]
print(a)'''
#no-elif usage in list comprehension
#if-else
'''a = [i*i if i % 2 == 0 else i*5 for i in range(31)]
print(a)'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
'''a=[a[i]+b[i] for i in range(len(a))]
print(a)'''
'''a=[a[i]+b[i] for i in range(5)]
print(a)'''
'''a=[i+j for i,j in zip(a,b)]
print(a)'''








