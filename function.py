
# def sum(x,y):
#     return x+y
#     print(sum(4,5))

# def sub(x,y):
#     return x-y
#     print(sub(4,5))

# def mul(x,y):
#     return x*y
#     print(mul(4,5))
# def div(x,y):
#     return x/y
#     print(sum(4,5))








#Write a Python function to sum all the numbers in a list
# def sum_of_list2 (list1):
#   _lis=0
#   for i in range(len(list1)):
#     _lis=_lis+(list1[i])
#     print(_lis)
#   return _lis
# list1=[3,4,56,7,8]
# (sum_of_list2(list1))

 


# list=[4,4,5,4,34,5]
# def add(list):
#     count=0
#     for i in range(len(list)) :
#         count=count+list[i]
#     return count
# print(add(list))        


#Write a Python function to multiply all the numbers in a list

# def mul_list2(list1):
#   mul=1
#   for i in list1:
#     mul=mul*i
#   return mul  
# list1=[2,3,4,5]
# print(mul_list2(list1))













# list=[4,4,5,4,34,5]
# def mul(list):
#    total=1
#    for i in list:
#      total=total*i
#    return total
# print(mul(list))    



#Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument 
# 










# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return  n*fact(n-1) 
# n=15        
# print(fact(n))           






#Write a Python program to reverse a string.

# str1='rammurat'
# def pappu(str1):
#     result1=''
#     for i in str1:
#       result1=result1+insert(i,-i)
#     return result1    
# print(pappu(str1))    


# Write a Python function to check whether a number falls in a given range.

# def number_falls(n):
#   if n in range(1,9):
#     print(n,'is in this range')
#   else:
#     print(n,'not is in this range')
# number_falls(5)  

# Write a Python function that accepts a string and calculate the number of upper case letters
#  and lower case letters.

# str2='eucFEJKD'
# def str1(str2):
#  for i in str2:
#   count=0
#   count1=0
#   if i in range(65,90):
#     count=count+i
#   else:
#     count1=count1+i
#  print(count) 
#  print(count1)
# str1('eucFEJKD')   


#Write a Python function that takes a list and returns a new list with unique elements of the first list.


# list1=[2,4,6,7,3,5,75,5,3,2,4,75,5]
# def unique_element(list1):
#   d=[]
#   for i in list1:
#    if  i not in d:
#     d.append(i)
#   return d
# print(unique_element(list1))  


# prime number


# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))




#Write a Python program to print the even numbers from a given list.

# list1=[2,3,45,8,6,9,12,24,56,76,45,]
# def even_numbers(list1):
#   even=[]
#   for i in list1:
#     if  i%2==0:
#       even.append(i)
#   return even   
# print(even_numbers(list1))   


#Write a Python function that checks whether a passed string is palindrome or not.





# Write a Python function to check whether a number is "Perfect" or not.

# def is_perpect(n):
#   sum=0
#   for i in range(1,n):
#     if n%i==0:
#       sum=sum+i
#   if n==sum:
#       print(n,'is perfect number')  
#   else:
#       print(n,'is not perfect number') 
      
# n=27
# (is_perpect(n))


#Write a Python function that checks whether a passed string is a palindrome or not


# def is_palindromw(str1):
#   a=str1
#   str2=''
#   for i in str1:
#     sum=i+sum
#   if a==sum:
#     print('yes')  
#   else:
#     print('no')


# str1='rammar'
# is_palindromw(str1)


#Write a Python function to check whether a string is a pangram or not

# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 
# (both included).

# n= int(input('enter the number :'))
# list1=[]
# for i  in range(1,n+1):
#   list1.append(i**2)
# print(list1)  



#Write a Python program to create a chain of function decorators (bold, italic, underline etc.).

# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello world"
# print(hello()) ## returns "<b><i><u>hello world</u></i></b>"


#Write a Python program to execute a string containing Python code.
