#This is a recursive function to find the factorial of an integer

# def fect(n):
#     if n==0:
#       return 1
#     else:
#      return (n*fect(n-1))  
# print(fect(8))




#Program to print the fibonacci series upto n_terms

# def fib(m):
#     if m==0:
#      return 0
#     if m==1:
#      return 1
#     else:
#      return (fib(m-1))+fib(m-2)
# n=8 
# for i in range(n+1):
#     x=fib(i)
#     print(x)




# sum of n natural numbers in python
# def sum(m):
#     if m<=1:
#      return 1
#     else: 
#      return m+sum(m-1) 
# n=9
# print(sum(9))



#Reverse a string

# def res (str1):
#     if len(str1)>=0:
#         return str1[0]
#     else:
#        x= str1[len(str1)]+res(str1[(len(str1)-1)])
#        print(x)
#        return x 
# str1='rammurt'
# print(res('rammurt'))
# sum=0
# def sum_num(i):
#     global sum
#     sum=sum+i
#     return sum

# for i in range(1,5):
#     sum_num(i)
# print(sum)






# def sum_num(i):
#     sum=0
#     while i>0:
#       d=i%10  
#       sum=sum+d  #0+2+4
#       i=i//10  #0
#     return sum

# num=420
# x=sum_num(num)
# print(x)
#The Fibonacci sequence begins with the following 14 integers:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 


# def fib(n):
#   a=0
#   b=1
#   sum=0
#   if n==1:
#    print(a)
#   elif n==2:  
#    print(a)
#    print(b)
#   else:
#    print(a)
#    print(b)  
#    for i in range(n-2):
#     sum=a+b
#     a=b
#     b=sum
#     print(sum)     
# fib(5)

# n='6365'
# r=n[::-1]
# print(r)
# if n==r:
#     print('yes')
# else: 
#     print('no')
    
    
# sub1=int(input('enter the number :'))  
# sub2=int(input('enter the number :'))    
# sub3=int(input('enter the number :'))    
# sub4=int(input('enter the number :'))    
# sub5=int(input('enter the number :')) 

# per=(sub1+sub2+sub3+sub4+sub5)/5*(100)  
# if per<=100 and per >=90:
#     print('murat subject1=',sub1,'subject2=',sub2,'subject3=',sub3,'subject4=',sub4,'subject5=',sub5,'A+')
# elif per<90 and per >80:
#     print('murat subject1=',sub1,'subject2=',sub2,'subject3=',sub3,'subject4=',sub4,'subject5=',sub5,'A')     
# elif per<80 and per >70:
#     print('murat subject1=',sub1,'subject2=',sub2,'subject3=',sub3,'subject4=',sub4,'subject5=',sub5,'B+')    
# elif per<60 and per >50:
#     print('murat subject1=',sub1,'subject2=',sub2,'subject3=',sub3,'subject4=',sub4,'subject5=',sub5,'B')   
# elif per<40 and per >30:
#     print('murat subject1=',sub1,'subject2=',sub2,'subject3=',sub3,'subject4=',sub4,'subject5=',sub5,'C')   
# else:
#     print('f')


# n=int(input('enter the number :'))
# r=n**(1/2)
# print(r)
# if type(r)==int:
#    print(n,'yes ')
# else:
#     print('no')   



n=input('enter the email:')
b=input('enter the password :')
str1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str2="abcdefghijklmnopqrstuvwxyz"

sc='@!#$'

num="0123456789"
count=0
if b in str1:
   count=count+1
elif b in str2:
   count=count+1
elif b in sc:   
   count=count+1
elif b in num:   
   count=count+1   