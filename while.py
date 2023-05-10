
# n=int(input('Enter the num :'))
# i=1
# even=0
# odd=0
# while i<=n:
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd +i
#     i=i+1
# print(even)  
# print(odd)  

# length = 0
# list1 = [1,2,4,6,7]
# i=0
# while list1[i]:
#     print(list[i])
#     length=length+1
#     i=i+1
# print(length)

# num = 121
# new_num = 0
# temp=num
# while num > 0:
#     digit = num%10
#     print(digit)
#     new_num = new_num*10 + digit
#     num=num//10    
# print(temp)
# if temp==new_num:     
#     print(new_num)

# n=5
# i=1
# while n>i:
#     print(i*i)
#     i=i+1

# write a program to print the following using while loop
# a first 10 even numbers
# b  first 10 odds numbers
# c first 10 natural numbers
# d first 10 whole numbers


# i=2
# while i<=20:
#     print(i)
#     i=i+2

# i=1
# while i<=20:
#     print(i)
#     i=i+2

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# i=0
# while i<=10:
#     print(i)
#     i=i+1

#Q.. first 10 integers and thiers squares.
# i=1
# while i<=10:
#     print(i**2)
#     i=i+1


#Q.  10, 20, 30, 40,.....,300
# i=10
# while i<=300: 
#     print(i)
#     i=i+10



#Q. 105,98,91,7


# i=105
# while i>=7:
#     print(i)
#     i=i-7

# first 10 natural number reverse
# i=10
# while i>=1:
#     print(i)
#     i=i-1

# sum of first 10 natural number

# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)   

#Q. print table
# n= int(input('Enter the number :'))
# i=1
# while i<=10:
#      r=n*i
#      print(r)
#      i=i+1

# check number are prime or not

# n= int(input('Enter the number :'))
# i=1
# while i<=n:
#     if n%i==0:
#          print(i ,'is prime number')    
#     else:
#         print(i,'not prime number') 
#     i=i+1   


# sum of the digits numbers

# n =int(input('Enter the number :')) 
# sum=0
# while n!=0:
#      r=n%10
#      sum=sum+r
#      n=n//10
# print(sum)  
# 
# 
#Q. reves num
# n= int(input('Enter the number :'))
# sum=0
# while n!=0:
#     p =n%10
#     sum=sum+p
#     n=n//10
# print(sum)


# n=int(input('Enter the number :'))
# for i in range(n+1):
#     for j in range(i):
#         print('*',end="")
#     print()    
# for i in range(n):
#     for j in range((n-1)-i):
#         print('*',end="")  
#     print()         



# for i in range(1,10):
#     for j in range(3+i):
#         for k in (str(i)):
#             print('@'*i,end='')
#     print('#'*(5-i),end='')
# print()   


# n =int(input('num :'))
# sum=0
# for i in range(1,n+1):
#     sum=sum+1/i
# print(sum)



#Q.. Write a program in Python to display the Factorial of a number.

# num=5
# fact=1
# while num>=1:
#     fact=fact*num
#     num=num-1
# print(fact)

#Write a program in Python to reverse a word.


# str = input("Input a word to reverse: ")
# for i in range(len(str) - 1, -1, -1):
#   print(str[i], end="")
# print("")



#Q..Write a program that appends the type of elements from a list.

# x = [23,'ram', 23.98]
# y=[]
# for i in range(len(x)):
#      y.append(x[i])
# print(y)



#Q.. Write a program to filter even and odd number from a list.

# x = [10, 23, 24, 35, 65, 78, 90]
# for i in range(len(x)):
#      if [i]%2==0:
#        print('even',x[i])
#      else:
#       print('odd',x[i])     
     


#Q.. Write a program to fetch only even values from a dictionary.



# x = [10, 23, 24, 35, 65, 78, 90]
# for i in range(len(x)):
#      if i%2==0:
#        print('even',x[i])

#Q.. Write a program to reverse a string in python.
# a= 'ram'
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end='')


# a= 'ram'
# i=1
# while len(a)>=i:
#     i=i+1
#     print(a[i],end='')

#Write a program to count vowels and consonants in a string.


# n='ram'
# i=1
# count1=0
# count2=0
# while len(n)>=i:
#     if n[i] in 'aeiou':
#         count1=count1+1
#     else:
#         count2=count2+1
#     i=i+1
# print(count1)    
# print(count2)  



#Q... Write a program to remove duplicates in a string

# n='rammurat'
# r=[]
# for i in range(len(n)):
#     if [i] not in r:
#       r.append(n[i])
# print(r)

  
# n = input("Enter a Word ")
# x = []
# for i in range(len(n)):
#     if n[i] not in x:
#         x.append(n[i])
# for i in range(len(x)):
#     print(x[i], end=" ")


# Write a program to count the number of letters in a word.



# n='rammurat'
# count=0
# for i in range(len(n)):
#     count=count+1
# print(count)    


#Python program to count the occurrence of each character in a word.

