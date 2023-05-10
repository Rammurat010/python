#Write a Python program to calculate the sum of a list of numbers.

# def sum_list(list1):
#     if len(list1)==1:
#         return list1[0]
#     else:
#         return list1[0]+sum_list(list1[1:])

# list1=[3,4,5,6,]
# print(sum_list(list1))


#Write a Python program to convert an integer to a string in any base.
# def int_to_str(str1):
#     if str1[0]:
#         return ''
#     else: str(str[:1])+str(str1[1:])
        
    
# str1=1234
# print(int_to_str(str1))


# def get_index(n,list1):
#     if n not in list1:
#         return -1
#     list12=[]
#     for i in range(len(list1)):
#         if n==list1[i]:
#             list12.append(i)
#     return list12


# list1=[3,4,5,6,6,7,8,7]
# n=int(input('enter the number :')) 
# print(get_index(n,list1))       


#Counting the White Spaces in a String
# n='ram is good boy'
# count=0
# for i in n:
#     if i==' ':
#         count=count+1
# print(count)        
        
#Counting Digits, Letters, and Spaces in a String       
# n='ram    12345'
# count1=0
# count2=0
# count3=0
# for i in n:
#     if i==' ':
#        count1=count1+1 
#     if i.isalpha:
#         count2=count2+1
#     if i.isdigit:
#         count3=count3+1
# print(count3,count2,count1)   

#Counting Special Characters in a String              

# spChar = "!@#$%^&*()"
# count=0
# for i in spChar:
#     if i in spChar:
#         count=count+1
# print(count)        


#Removing All Whitespace in a String
        
# n='ram m m m'
# str1=''
# for i in n:
#     if i==' ':        
#         pass
#     else:
#        str1=str1+i 
# print(str1)       

#Building a Pyramid in Python
# n=3
# k=1
# for i in range(1,n):
#     for j in range(i):
#         print(' '*(3-i)+'*'*k)
#         k=k+2
        
        
#Write a Python program to sum recursion lists. Go to the editor
# def  sum_list(list1):
#     sum=0
#     for i in list1:
#        if type(i)==type([]):
#            sum=sum+sum_list(i)
#        else:
#            sum=sum+i   
#     return sum
    
      
# list1=[1, 2, [3,4], [5,6]]         
# print(sum_list(list1))          


#Write a Python program to get the factorial of a non-negative integer
# def fact(n):
#  if n==1:
#     return 1
#  else:
#      return n*fact(n-1)

# n=5
# print(fact(n))    

#Write a Python program to solve the Fibonacci sequence using recursion.

# def fib(n):
#     if n==0 or n==1:
#         return 1
#     else:
    
#      return fib(n-1)+fib(n-2)

# n=6
# print('0')
# for i in range(n+1):
#     print(fib(i))

#Write a Python program to get the sum of a non-negative integer.
# def sum_n_n(n):
#     if n<1:
#         return 1
#     else:
#         return n+sum_n_n(n-1)
    
# n=14
# print(sum_n_n(n))


# Write a Python program to calculate the harmonic sum of n-1. Go to the editor
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# harmonic series

def sum_har(n):
    if n==1:
        return 1
    else:
        return 1/n+sum_har(n-1)

n=7
print(sum_har(n))