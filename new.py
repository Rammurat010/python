

# n=int(input('enter the number :'))
# if n<=0:
  
#     print('quit')
# else:
#     for i in range(100):
#         if n>=9:
#             print('too big')
#             break
#         elif n<=7:
#             print('to small')
#             break  
#         elif n==8: 
#             print('correct')
#             break      





# 1: Write a program to take a input of student mark and print Grade
# Mark Range	Grade
# 100-91    A+
# 90-81     A
# 80-71     B+
# 70-61     B
# 60-51     C+
# 50-41     C
# 40-0      Fail


# n= int(input('enter the mark :'))
# if n<=100 and 90<n:
#     print('A+')
# elif n<=90 and 80<n:
#     print('A')
# elif n<=80 and 70<n:
#     print('B+')        
# elif n<=70 and 60<n:
#     print('B')
# elif n<=60 and 50<n:
#     print('C+')
# elif n<=50 and 40<n:
#     print('C')
# else:
#     print('Fail')              


# 2:Take 2 int values from user and print greatest among them

# a=int(input('enter the first number :'))
# b=int(input('enter the second number :'))
# if a>b:
#     print(a,'is largest')
# elif a<b:
#     print(b,'is largest')
# else:
#     print(a,'and',b,'are both same')    
    



# 3: Take values of length and breadth of a rectangle from user and check if it is square or not.

# a=int(input('enter the length  of a rectangle :'))
# b=int(input('enter the breadth of a rectangle :'))
# if a==b:
#     print('square')
# else:
#     print('not square')    
    





# 4: Take input of age of 3 people by user and determine oldest and youngest among them.

# a=int(input('enter the age of first man :'))
# b=int(input('enter the age of second man :'))
# c=int(input('enter the age of third man :'))
# if a>b and b>c:
#     print(a,'oldest',c,'youngest')
# elif a>c and c>b:
#     print(a,'oldest',b,'youngest')     
# elif b>c and c>a:
#     print(b,'oldest',a,'youngest')  
# elif b>a and a>c:
#     print(b,'oldest',c,'youngest')       
# elif c>a and a>b:
#     print(c,'oldest',b,'youngest')    
# elif c>b and b>a:
#     print(c,'oldest',a,'youngest')      
    


# 5:Take 3 sides triangle as string via comma separated ('3,4,5'). Check type triangle right angle triangle,
# isosceles triangle etc


# a=(input('enter the 3 sides triangle :'))
# list1=a.split(',')
# list1=[2,3,4]
# if list1[0]*list1[0]+list1[1]*list1[1]==list1[2]*list1[2] or list1[0]*list1[0]+list1[2]*list1[2]==list1[1]*list1[1]or list1[1]*list1[1]+list1[2]*list1[2]==list1[0]*list1[0]
#     print('right angle triangle')
# elif list1[0]==list1[1] or list1[0]==list1[2] or list1[2] ==list1[1]:
#     print('isosceles triangle') 
# else:
#     print('other triangle')    




# 1: Calculate the sum of all numbers from 1 to a given number
# n=int(input('enter the number :'))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)    



# 2: Reverse a given integer number
# n=int(input('enter the nuber :'))
# r_n=''
# str1=str(n)
# for i in str1:
#     r_n=i+r_n
# print(r_n)    
    


# 3: Write a program to check prime number or not

# n=int(input('enter the number :'))
# count=0
# if n==1:
#     print(n,'is prime number')
# elif n<=0:
#     print('not defind')   
# else:     
#     for i in range(2,n+1):
#         if n%i==0:
#             count=count+1            
# if count==1:    
#     print(n,'is prime number')  
# else:
#     print(n,'is not prime number') 
          



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

# n=int(input('enter the number :'))
# for i in range(1,n+2):
#     for j in range(1,i):
#         print('*',end=' ')
#     print()    
# for k in range(1,n+1):
#     for L in range(1,(6-k)):
#         print('*',end=' ')
#     print()    






'''5:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #'''


# n=int(input('enter the number :'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('#',end=' ')
#     print() 
    



# 1: Given a two list of numbers, write a program to create a new list such that the new list should 
# contain odd numbers from the first list and even numbers from the second list.
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]



# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# list3=[]

# for i in list1:
#      if i%2!=0:
#         list3.append(i)
# for j in list1:
#      if j%2==0:
#         list3.append(j)          
# print(list3)                





# 2: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included).

# list1=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         list1.append(i)
# print(list1)

# 3: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is 
# an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the
# following input is supplied to the program: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# n=int(input('enter the number :'))
# dict1={}
# for i in range(1,n+1):
#     dict1[i]=i**2
# print(dict1)    
    

# 4:WAP that display all leap year from 1900-2101?

# list1=[]
# for i in range(1900,2102):
#     if i%400==0 or i%100!=0 and i%4==0:
#         list1.append(i)
# print(list1)  

      
# 5:WAP to print index at which a particular value exits.if value exist at multiple locations in the list tyhen 
# print all the index.Also count the number of times that value is repeated in the list?

# n=int(input('enter the number :'))
# list1=[2,3,4,8,5,4,5,6,7,5,3,5,6,4,6,2]
# list2=[]
# count=0
# for i in range(0,len(list1)):
#     if list1[i] ==n:
#         print(i)
#         count=count+1
#         list2.append(i)
# print('index of',n,'in list1', list2) 
# print(count) 
      
        
    


# 6:WAP that has list of both positive and as well as negative .Make a new tuple that has only positive value 
# from the list?    

# list1=[4,5,6,-8,-9,53,6]
# list2=[]
# for i in list1:
#     if i<0:
#         list2.append(i)
# tuple1=tuple(list2)
# print(tuple1)        









# 1:WAP that creates a list of 10 random integers .then create two list odd list and even list that has all odd even
# value in the list respectively?

# list1=[44,6,7,89,6,4,45,36,9,65]
# list2=[]
# list13=[]
# for i in list1:
#     if i%2!=0:
#         list2.append(i)
#     else:
#         list13.append(i)
# print('odd list',list2)
# print('even list',list13)            





# 2:WAP that define a list of countries thar are member of BRICS .Check whether a country is member of BRICS or not?

# list1=['Brazil', 'Russia', 'India', 'China', 'South Africa']
# countries=input('enter the countries name :')
# if countries in list1:
#     print(countries,'is member of BRICS ')
# else:
#     print(countries,'is not member of BRICS') 

   

# 3:WAP that inverts a dictionary .That is it makes key of one dictionary value of another and vice versa?

# dic1={'name': 'Amit', 'salary': '100', 'city': 'Greater Noida'}
# dict2={}
# for i,j in dic1.items():
#     dict2[j]=i
# print(dict2)    

# 4:WAP that combines the list to a dictionary?
# Keys=[‘name’,’Age’,’Marital status’]
# Values=[‘yash’,’23’,’married’]


# Keys=['name','Age','Marital status']
# Values=['yash',23,'married']
# dict={}
# for i in range(len(Keys)):
#     dict[(Keys[i])]=Values[i]
# print(dict)    




# 5: Write a program to check if the given number is a palindrome number.
# num=(input('enter the number :'))
# sum=''
# for i in num:
#     sum=i+sum   
# if num==sum:
#     print(num,'is a palindrome number')  
# else:
#      print(num,'is not a palindrome number')       





# 6: emp = [{'name': 'Amit', 'salary': '100', 'city': 'Greater Noida'}, {'name': 'Ambresh', 'salary': '150', 'city': 'Greater Noida'},{'name': 'Aman', 'salary': '100', 'city': 'Dheradun'}]
# Remarks: all questions done via loop in generic format assume that this is very large list of dict
# a: Take a name and find salary
# b: Calculate avg salary
# c: Calculate whose max salary
# d: Take a city name and list down all emp who is beloging to that city
# e: List down all emp whose name start with 'Am'

# emp = [{'name': 'Amit', 'salary': '100', 'city': 'Greater Noida'}, {'name': 'Ambresh', 'salary': '150', 'city': 'Greater Noida'},{'name': 'Aman', 'salary': '100', 'city': 'Dheradun'}]

# name=input('Enter the name: ' )
# for i in emp:
#     if i['name']==name:
#         z=i['salary']
#         print('salary of emp',z)
# sumSalary=0
# for i in emp:        
#     r= i["salary"]  
#     sumSalary=sumSalary+int(r)
# print('total salary',sumSalary)   

 
# avgSalary=sumSalary/3
# print('Avg SALAR:',str(avgSalary))


# city=input('Enter the city name: ' )
# for i in emp:
#     if i['city']==city:
#         z=i['name']
#         print(z) 


# list_salary=[]        
# for i in emp:
#     s=(i['salary']) 
#     list_salary.append(s)
# max_salary=max(list_salary)
# print('max_salary',max_salary)  
         

# data=[]
# for i in emp:
#     if i['name'].__contains__('Am'):
#         data.append(i['name'])
# print(data)

# def sum_of_num(a,b,*arg):
#     sum=a+b 
#     for i in arg:
#         sum=sum+i
#     print('sum',sum) 

# def sub_of_num(a,b,*arg):
#     sub=a-b 
#     for i in arg:
#         sub=sub-i
#     print('sub',sub)
     
# def mul_of_num(a,b,*arg):
#     mul=a*b 
#     for i in arg:
#         mul=mul*i
#     print('mul',mul)
    
# def div_of_num(a,b):
#     div=a/b 
#     print('div',div)    
    
  
# a=6
# b=2
# sum_of_num(a,b,4)
# sub_of_num(a,b,4)
# mul_of_num(a,b,4)
# div_of_num(a,b)
    
    
    
# name='Amit'
# email='amit@'
# grade = 'B'
# salary = 0

# A+ =>25
# A  => 15
# B+ => 10
# B  => 5
# function return=> incre

# def parcentage(incre,salary=0):
#     if salary>0:
#         new_salary_of_emp= salary*incre/100
#         return new_salary_of_emp
#     else:
#         return 0


# name =input('enter the name :')
# email =input('enter the email :')
# grade =input('enter the grade :')
# salary=int(input('enter the salary :'))
# incre=int(input('enter the incre :'))

# print('incre salary')
# if grade=='A+':
#     print(parcentage(salary,incre))
# elif grade=='B+':
#     print(parcentage(salary,incre))  
# elif grade=='C+':
#     print(parcentage(salary,incre))     
# elif grade=='D+':
#     print(parcentage(salary,incre))  
# else:
#     print('zero b/c very poor grade')           
    
    

def sum_of_num(a,b,*arg):
    sum=a+b 
    for i in arg:
        sum=sum+i
    print('sum',sum) 

def sub_of_num(a,b,*arg):
    sub=a-b 
    for i in arg:
        sub=sub-i
    print('sub',sub)
     
def mul_of_num(a,b,*arg):
    mul=a*b 
    for i in arg:
        mul=mul*i
    print('mul',mul)
    
def div_of_num(a,b):
    div=a/b 
    print('div',div)      
    
    
a=5
b=10
c=6
d=8    


print('press 1 for add')
print('press 2 for sub')
print('press 3 for mui')
print('press 4 for div')
n=int(input('enter the number :'))
if n==1:
    while n==1:
        k=int(input('select of input argument :' ))
        print('sum of 2 argument, 2 press')
        print('sum of 3 argument, 3 press')
        print('sum of 4 argument, 4 press')
        print('for exixt, 4 press')
        if k==2:
            sum_of_num(a,b)
        elif k==3:
            sum_of_num(a,b,c)
        elif k==4:
            sum_of_num(a,b,c,d)
        elif k==4:
            n==0
        elif k>5:
            print('out of range')  
elif n==2:
    while n==1:
        k=int(input('select of input argument :' ))
        print('sub of 2 argument, 2 press')
        print('sub of 3 argument, 3 press')
        print('sub of 4 argument, 4 press')
        print('for exixt, 4 press')
        if k==2:
            sub_of_num(a,b)
        elif k==3:
            sub_of_num(a,b,c)
        elif k==4:
            sub_of_num(a,b,c,d)
        elif k==4:
            n==0
        elif k>5:
            print('out of range')            
    