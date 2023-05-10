# Write a Python function that takes a list of integers as an argument and returns the sum of all the even numbers in the list.



# def sum_even(list1):
#     sum=0
#     for i in list1:
#         if i%2==0:
#             sum=sum+i
#     return sum        
# list1=[3,4,6,7,86,4,3,5,6,7,89,7]
# print(sum_even(list1))


# 2: Write a Python function that takes a string as an argument and returns a new string with all the vowels removed.


# def remove_vowels(str1):
#     str2=''
#     for i in str1:
#         if i not in 'AEIOUaeiou':
#             str2=str2+i
#     return str2        
        
# str1='rammurat'
# print(remove_vowels(str1))

# 3: Write a Python function that takes a dictionary as an argument and returns a list of all the keys in the dictionary.

# def  find_dict_value(dict1):
#     list1=[]
#     for i in dict1.values():
#         list1.append(i)
#     return list1    
        
# dict1={'name': 'murat', 'mobile':2345}
# print(find_dict_value(dict1))


# 4: Write a Python function that takes a list of strings as an argument and returns the longest string in the list.

# def longest_string(list1):
#     list2=[]
#     for i in list1:
#         list2.append(len(i))
#     longest_string1=max(list2)
#     return  longest_string1

# list1=['ram','murawt','tawde','pappu']
# print(longest_string(list1))

# 5: Write a Python function that takes a list of integers as an argument and returns a new list of all the prime numbers in the original list.


# def prime_number(list1):
#     primes_list = []
#     for num in list1:
#         if num==1:
#             primes_list.append(num)
#         elif num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 primes_list.append(num)
#     return primes_list
# list1=[1,2,3,45,61,39,55,78,31]
# print(prime_number(list1))


# 1:wap to find largest number in a list using recursion?

#  (1,largest_number(list1[1:]))    (1,2,3,45,61,39,55,78,31)  78
#  (2,largest_number(list1[1:]))    (2,3,45,61,39,55,78,31)  78
#  (3,largest_number(list1[1:]))    (3,45,61,39,55,78,31)  78
#  (45,largest_number(list1[1:]))   (45,61,39,55,78,31)  78
#  (61,largest_number(list1[1:]))   (61,39,55,78,31)   78
#  (39,largest_number(list1[1:]))   (39,55,78,31)    78
#  (55,largest_number(list1[1:]))   (55,78,31)     78
#  (78,largest_number(list1[1:]))   (78,31)     78
#   (list1[0])                      (31)     31

# def largest_number(list1):
#     if len(list1)==1:
#         return list1[0]
#     else:  
#         return max(list1[0],largest_number(list1[1:]))


# list1=[1,2,3,45,61,39,55,78,31]
# print(largest_number(list1))


# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)     #5*fact(5-1)  4*fact(4-1) 3*(3-1) 2*(2-1) 1*(1-1)   1
     

  
# n=5
# print(fact(n))

# 2:write a function to print fibnocci series?



# def fib(n):
#     list1=[]
#     a=0
#     b=1
#     list1.append(a)
#     list1.append(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         list1.append(c)
#     return list1
# n=int(input('enter the number :'))
# print(fib(n))


# 3:write a function that accept a string from user and display character that are present at even index?


# def string_even_index(str1):
#     str2=''
#     len1=len(str1)
#     for i in range(len1):
#         if i%2==0:
#             str2=str2+str1[i]
#     return str2        

# str1=input('enter the the stringn :')
# print(string_even_index(str1))


# 4:write a function that sort the given list without using predefined function [1,2,4,3,68,9,88,7,6]?


# def sort_list(list1):
#     len1=len(list1)
#     for i in range(len1):
#         for j in range(len1-1):
#             if list1[j]>list1[j+1]:
#                 temp =list1[j]
#                 list1[j]=list1[j+1]
#                 list1[j+1]=temp         
#     return list1       
# list1=[1,2,4,3,68,9,88,7,6]
# print(sort_list(list1))


# 5:write a  function that from a list of first character of every word in another list
# ['Hello','welcome',''To','the','world',''of',python']

# def first_character(list1):
#     list2=[]
#     for i in list1:
#         for j in i:  #hello
#             list2.append(j)
#             break
#     return list2    

# list1=['Hello','welcome','To','the','world','of','python']
# print(first_character(list1))




# 1:write a function that returns the area and circumference of a circle whose radius is passed as an argument?

# def area_circum(r):
#     area_of_circle=3.14*r**2
#     circumference_of_circle=2*3.14*r
#     return area_of_circle, circumference_of_circle


# r=float(input('enter the radious :'))
# area ,circumference =area_circum(r)
# print('area of circle',area)
# print('circumference of circle',circumference)

#  2:wap to generate Abecedarian series?


#  3:write a function to reverse a string?


# def reverse_sting(str1):
#     str2=''
#     for i in str1:
#         str2=i+str2
#     return str2    
        

# str1=input('enter the string :')
# print(reverse_sting(str1))



#  4:write a function that find sum of n natural number using recursion?


# def sum_of_natural_number(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     return sum    

# n=int(input('enter the number :'))
# print(sum_of_natural_number(n))



#  5:wap a function using for loop to calculate the factorial of given number ?


# n=int(input('enter the number :'))
# fact=1
# if n==0:
#     print(1)
# elif n<0:
#     print('factorial does not exict')    
# elif n==1:
#     print(1)
# else:
#     for i in range(2,n+1):
#         fact=fact*i
#     print(fact)    


# a=6
# b=0
# try:
#     print(a/b)
# except Exception as murat:
#     print(murat)
    
