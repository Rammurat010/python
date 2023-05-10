#Write a Python Code to Check if a Number is Odd or Even.

# n=7
# if n%2==0:
#     print('yes')
# elif n%2!=0:
#     print('no')

#Write a Python code to find the maximum of two numbers.

# n=4
# m=5
# if n>m:
#     print(n,'is')        
# else:
#     print(m,'is')


#Write a Python code to check prime numbers.

# n=6
# count=0
# for i in range(2,n+1):
#     if n%i==0:
#         count=count+1
# if count==1:
#     print('yes')
# else:
#     print('no')    


#Write a Python factorial program without using if-else, for, and ternary operators.
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
    
# n=5
# print(fact(n))


#Write a Python code to calculate the square root of a given number.
# import math
# n=9
# r=math.sqrt(9)
# print(r)



#Write a Python code to calculate the area of a triangle.
 
# a=4
# b=7
# c=8
# s=(a+b+c)/2
# r=((s-a)*(s-b)*(s-c))**.5
# print(s)        
        
#Write a Python code to check the armstrong number. 

# n=371
# a=n
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum+rem*rem*rem
#     n=n//10
# print(sum)    
# if a==sum:
#     print('yes')
# else:
#     print('no')    
    
    
#Write a Python code to swap two variables.


# a=6
# b=5
# x=b
# b=a
# a=x
# print(a)
# print(b)    



# Write a Python program to create a list by concatenating a given list with a range from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# n=5       
# list =[]   
# for i in range(1,n+1):  
#     x='p'*i,'q'*i
#     list.append(x)
# print(list)    


#Write a Python program to get a variable with an identification number or string. 
#Write a Python program to find common items in two lists.

# list1=[2,3,4,5,6,5,4,3,]
# list2=[2,4,5,5,6,4,4,5,6,4,5]
# list3=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             list3.append(j)
# print(list3)            


# Writ Write a Python program to convert a list of multiple integers into a single integer. Go to the editor


#  Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
# Sample list: [11, 33, 50]
# Expected Output: 113350

# list= [11, 33, 50]
# str1=''
# for i in list:
#     str1=str1+str(i)
# print(str1)    

#Write a Python program to split a list based on the first character of a word. 

# str1='rammurat'
# x=str1.split()
# print(x)

#Write a Python program to create multiple lists.
# list1=[]
# for i in range(2,21,2):
#     list1.append(i)
# print(list1)    
    
#Write a Python program to find missing and additional values in two lists.

# list1 = ['a','b','c','d','e','f']
# list2 = ['d','e','f','g','h'] 
# list3=[]
# for i in list1:
#     for j in list1:
#         if i==j:
#             pass
#         else:
#             list3.append(j)
# print(list3)            
               
#Write a Python program to split a list into different variables.

# Write a Python program to generate groups of five consecutive numbers in a list.   


# list1=[]
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         list1.append(j)
# print(j)                    



# for i in range(7):
#     for j in range(5):
#         if j==0 or (i==0 or i==3) and (j>=0 and j<4) or j==4 and i>0 and i<3:
#             print('*',end ='')
#         else:
#             print(end=' ')   
#     print()        


# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6, -5))

# Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# List1= (8, 2, 3, 0, 7)
# sum=0
# for i in List1:
#     sum=sum+i
# print(sum)    

# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


#  Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# str1="1234abcd"
# str2=''
# for i in str1:
#     str2=i+str2
# print(str2)    


# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number
# as an argument. 

# def fact(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fact(n-1)+fact(n-2)
    

# n=int(input('enter the positvie number :'))
# for i in range(n+1):
#     r=fact(i)
   
#     print(r)

#  Write a Python function that accepts a string and counts the number of upper and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# def count2(str1):
#     count=0
#     count1=0
#     for i in str1:
#         if i.isupper():
#             count=count+1
#         elif i.islower():
#          count1=count1+1
       
#     print(count)
#     print(count1)      
# str1='The quick Brow Fox'
# count2(str1)        

     

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]  


# def unique_list(List1):
#     list2=[]
#     for i in List1:
#         if i not in list2:
#             list2.append(i)
#     return list2        


# List1= [1,2,3,3,3,3,4,5]
# print(unique_list(List1))



#  Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
#  Go to the editor
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors 
# other than 1 and itself.