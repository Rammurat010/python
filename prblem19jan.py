#1: Write a program to use the loop to find the factorial of a given number.


n=3
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact) 



#2: Write a program to separate positive and negative number from a list. Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]





x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
P = []
N = []
for i in x:
    print(i)
    if i >= 0:
        P.append(i)
    else:
        N.append(i)
print(P)   
print(N)     



# 3:Write a program to fetch only even number salary from a dictionary. x = [{'name':'C', 'salary':100}, {'name':'B', 'salary':150}, 
# {'name':'A', 'salary':101}]


x = [{'name':'C', 'salary':100}, {'name':'B', 'salary':150},  {'name':'A', 'salary':101}]
for i in x:
    if i['salary']%2==0:
        print('even salary',i['salary'])
    else:
       pass



# 4: 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


n=int(input('Enter the number :'))
for i in range(n+1):
    for j in range(i):
        print('*',end="")
    print()    
for i in range(n):
    for j in range((n-1)-i):
        print('*',end="")  
    print() 