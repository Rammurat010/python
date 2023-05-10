#Python program to reverse a number


# def reverse_num(n):     
#  sum=0
#  while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10
#  return (sum) 
# n=int(input('Enter the num :'))
# print(reverse_num(n))    


#Write a program in Python to print the Fibonacci series using iterative method.


# n=int(input('Enter the number :'))
# first=0
# second=1
# for i in range(0,n):
#     if i<=1:
#       fib=i
#     else:
#      fib =first+second
#      first=second
#      second=fib
#      print(fib)   


#Fibonacci series program in python using recursive method
# def Fibonacci_series(n):
#     fist=0
#     second=1
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#      return Fibonacci_series(n-1) + Fibonacci_series(n-2)  
# n=int(input('Enter the number :'))
# for i in range(0,n):
#     print(Fibonacci_series(i))




#Write a program in Python to check whether a number is palindrome or
# not using iterative method.

# n=int(input('Enter the number :'))
# r=n
# sum=0
# while n>0:
#     p=n%10
#     sum=sum*10+p
#     n=n//10
# print(sum) 
# if r==sum:
#     print('palindrome' )
# else:
#     print('not palindrome ')    

#Write a program in Python to find greatest among three integers.


# n1 = int(input(" first number n1: "))
# n2 = int(input("second number n2: "))
# n3 = int(input("third number n3: "))
# if n1>=n2 and n1>=n3: 
# 	print(" n1 is greatest")
# if n2>=n1 and n2>=n3:
# 	print(" n2 is greatest")
# if n3>=n1 and n3>=n2:
# 	print("n3 is greatest")


#Program to check given number representation is in binary or not

# num = int(input("please give a number : "))
# while(num>0):
#     j=num%10
#     if j!=0 and j!=1:
#         print("num is not binary")
#         break
#     num=num//10
#     if num==0:
#         print("num is binary") 


#Write a program in Python to find sum of digits of a number using recursion?



# def recurtion(n):
#     if n==0:
#       return 0
  
#     return (n%10 +recurtion(n//10))
# n=int(input('enter the number :'))
# print(recurtion(n))


#Write a program in Python to swap two numbers without using third variable?


# a = int(input("please give first number a: "))
# b = int(input("please give second number b: "))
# a=a-b
# print(a)
# b=a+b
# print(b)
# a=b-a
# print(a)
# print("After swapping")
# print("value of a is : ", a)
# print("value of b is : ", b) 


#Write a program in Python to swap two numbers using third variable?


# a=int(input('enter the number'))
# b=int(input('enter the number'))
# x=a
# a=b
# b=x
# print(a)
# print(b)


#Write a program in Python to find prime factors of a given integer.

# def primeFactors(n):
 
#     c = 2
#     while(n > 1):
 
#         if(n % c == 0):
#             print(c, end=" ")
#             n = n / c
#         else:
#             c = c + 1
# n = 315
# primeFactors(n)
 


#Write a program in Python to add two integer without using arithmetic operator?
# def add(a,b):
#     for i in range(b,0,-b):
#         a=a+i
#     return a    
# a=int(input('enter the number :'))
# b=int(input('enter the number :'))
# x=(add(a,b))
# print('sum of two num',x)


#Write a program in Python to find given number is perfect or not?



#Python Program to find the Average of numbers with explanations


# n = int(input("Enter the total number you want to enter:"))

# sum = 0
# for i in range(n):
#     x = int(input("Enter the number:"))
#     sum = sum + x
# avg = sum / n
# print("Average=", avg)


#Python Program to calculate factorial using iterative method.


# a=int(input('enter the nub :'))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
#     print(fact)




#Python Program to calculate factorial using recursion.

# def fact(a):
#     fact1=1
#     if a<0:
#         return 'no factorial'
#     elif a==1:
#         return 1
#     else:
#         fact1=a*fact(a-1)
#     return fact1    
        
# a=int(input('enter the nub :'))
# print(fact(a))


#Python Program to check a given number is even or odd.
# n =int(input('enter the number :'))
# if n%2==0:
#     print(n,'is even number')
# else:
#      print(n,'is odd number')    

#Python program to print first n Prime Number with explanation.

# n= int(input('enter the number :'))
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#          print(i)
         
         
         
 #Python Program to find Smallest number among three.


# a=int(input('enter the number :'))        
# b=int(input('enter the number :'))  
# c=int(input('enter the number :')) 
# if a>=b and c>=b:
#     print(b,'is smallest number') 
# elif a>=c and b>=c:
#     print(c,'is samllest number')  
# elif b>=a and c>=a:  
#     print(a,'is samllest number')      



#Python program to calculate the power using the POW method.

# a=int(input('enter the number :'))
# b=int(input('enter the number :'))
# x=pow(a,b)
# print(x)



#Python Program to calculate the power without using POW function.(using for loop)
# a=int(input('enter the number :'))
# b=int(input('enter the number :'))
# for i in range(1,b+1):
#     x=a*




#Python Program to calculate the square of a given number.

# n=int(input('enter the number :'))
# x=n**2
# print(x)


#Python Program to calculate the cube of a given number.

# n=int(input('enter the number :'))
# x=n**3
# print(x)


#Python Program to calculate the square root of a given number.
# import math
# n=int(input('enter the number :'))
# x=math.sqrt(n)
# print(x)

# Python program to calculate LCM of given two numbers.
# a=int(input('enter the number'))
# b=int(input('enter the number'))


#check leap year
# year=int(input("Please Enter a year: "))
 
# if (year % 400 == 0): 
#    print("Given year %d is a leap year.", year)
# elif (year % 100 == 0): 
#     print("Given year %d is not a leap year.", year)
# elif (year % 4 == 0): 
#       print("Given year %d is a leap year.", year)
# else: 
#       print("Given year %d is not a leap year.", year)
   
   
   
# # Python Program to convert temperature in celsius to fahrenheit

# # change this value for a different result
# celsius = 37.5

# # calculate fahrenheit
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
   
   
   


# Python code to convert fahrenheit into celsius
# #taking input from the user
# fahrenheit = float(input("Please give the Hahrenheit Temperature : "))  
# #converting Celsius into Fahrenheit 
# celsius = ((fahrenheit-32)*5)/9
# print("Celcius= ",celsius)   



# Fahrenheit to Celsius formula
# °C =(°F - 32)/1.8000




#Python program to calculate Simple Interest with explanation.




# Python code to calculate simple interest
# #taking the values of principal, rate of interest and time from the user
# principal = int(input("Enter the principal amount: "))  
# rate = int(input("Enter the rate of interest: "))  
# time = int(input("Enter the time of interest in year: "))  
# #using the input values calculate simple interest
# simpleInterest = (principal*rate*time)/100
# print("Simple Interest = ",simpleInterest)



#Python program to remove given character from String.



# str1='rammurat'
# n=input('enter the character :')
# x=str1.replace(n,'')
# print(x)




# str1='rammUHFuratR'

# x=str1.index('u')
# print(x)

#Python Program to count occurrence of a given characters in string.


# str1='rammurat'
# n=input('enter the charecter :')
# x=str1.count(n)
# print(x)

# Python Program to check if two Strings are Anagram.

#Python program to check a String is palindrome or not.


# str1=input('enter the string :')
# b=str1
# str2=''
# for i in range(len(str1)-1,-1,-1):
#     str2=str2+str1[i]   
# if b==str2:
#     print('palindrome')
# else:
#     print('not palindrome')        


#Python program to check given character is vowel or consonant.

# n= input('enter the words :')
# if n in 'aeiouAEIOU':
#     print(n,'is vowel')
# else:
#     print(n,'is consonant')    


#Python program to check given character is digit or not.

# n= input('enter the words :')
# if  n>'0' and n<'9':
#     print(n,'is digit')
# else:
#     print(n,'is not digit')    




#Python program to check given character is digit or not using isdigit() method.

#Python program to replace the string space with a given character.

# n= input('enter the words :')
# str1='ram murat'
# if str1.

#Python program to convert lowercase char to uppercase of string.


# str1=input('enter the string :')
# str2=''
# for i in str1:
#     if i.isalpha:
#         str2=str2+i.upper()
#     else:
#         pass
# print(str2)     



#Python program to convert lowercase vowel to uppercase in string.   

# str1=input('enter the string :')
# str2=''
# for i in str1:
#     if i in 'aeiou':
#         str2=str2+i.upper()
#     else:
#        str2=str2+i
# print(str2)     


#Python program to delete vowels in a given string.


# str1=input('enter the string :')
# str2=''
# for i in str1:
#    if i in 'AEIOUaeiou':
#     i=''
#     str2=str2+i
#    else:
#        str2=str2+i
# print(str2)   
    



#Python program to count Occurrence Of Vowels & Consonants in a String.


# str1=input('enter the string :')
# count1=0
# count2=0
# for i in str1:
#     if i in 'aeiouAEIOU':
#         count1=count1+1
#     else:
#         count2=count2+1
# print(count1)
# print(count2)            



#Python program to print the highest frequency character in a String. 


#Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.



        
# str1=input('enter the string :')
# str2=''
# for i in str1:
#     if i in 'aeiouAEIOU':
#         i='-'
#         str2=str2+i  
#     else:
#         str2=str2+i    
# print(str2)        


#Python program to Count alphabets, digits, special char in string
    

# str1=input('enter the charecter :')
# count1=0
# count2=0
# count3=0
# for i in str1:
#     if i.isalpha():
#         count1=count1+1
#     elif i.isdigit():
#         count2=count2+1
#     else:
#         count3=count3+1
# print(count1)  
# print(count2)   
# print(count3)     



#Python program to separate characters in a given string.



#Python program to remove blank space from string.


# str1=(input('enter the string :'))
# str2=''
# for i in str1:
#     if i=='_':
#         i=''
#         str2=str2+i
#     else:
#         str2=str2+i 
# print(str2)                   




#Python program to concatenate two strings using join() method.

# str1=input('enter the first string :')
# str2=input('enter the second string :')

# print(''.join([str1,str2]))


#Python program to concatenate two strings without using join() method.


# str1=input('enter the first string :')
# str2=input('enter the second string :')

# str3=str1+str2
# print(str3)




#Python program to remove repeated character from string.

# str1=input('enter the number :')
# str2=''
# for i in str1:
#     if i not in str2:
#         str2=str2+i
#     else:
#         pass    
# print(str2)    



#Python program to calculate sum of integers in string

# str1=input('enter the string :')
# sum=0
# for i in str1:
#     sum=sum+int(i)
# print(sum)    


#Python program to print all non repeating character in string.

# str1=input('enter the string :')
# str2=''
# for i in str1:
#     if str1.count(i)<2:
#         str2=str2+i
# print(str2)        



#Python program to copy one string to another string.

# str1=input('enter the :')
# str2=''
# for i in str1:
#     str2=str2+i
# print(str2)    


#Python Program to sort characters of string in ascending order.

# str1=input('enter the string :')
# y=sorted(str1)
# str2=''
# for i in y:
#     str2=str2+i
# print(str2)    

#Python Program to sort character of string in descending order.
# str1=input('enter the string :')
# str2=''
# y=sorted(str1)
# print(y)
# for i in range(len(y)-1,-1,-1):
#     str2=str2+y[i]
# print(str2)    


# number=10
# table_list1=[]
# for i in range(1,11):
#     table_list1.append(number*i)
# print(table_list1)    

# table_dictionery={}
# for i in range(1,11):
#     table_dictionery[i]=9*i
# print(table_dictionery)    
# dict={'odd':[1,3,5],'even':[2,4]}    
# #200
# input_number=int(input('enter the number :'))
# even_odd_dictionry={}
# even_list1=[]
# odd_list2=[]
# for i in range(1,input_number+1):
#     if i%2==0:
#         even_list1.append(i)
#     else:
#          odd_list2.append(i)
# even_odd_dictionry['even']=even_list1
# even_odd_dictionry['odd']=odd_list2
            
# print(even_odd_dictionry)        
        
# def number_sum(n1,n2,n3=0,n4=0):
#     sum=n1+n2+n3+n4
#     return sum
    
    
# n1=2    
# n2=5
# n3=5   
# n4=7
# print(number_sum(n1,n2,n3,n4))    
# print(number_sum(n1,n2,n3))
# print(number_sum(n1,n2))



#decimal to binary
# sum=0
# n=int(input('enter the number :'))
# while n>0:
#     rem=n%2
#     sum=sum*10+rem
#     n=n//2
# print(sum)  


#binary  to decimal


# n=1111
# sum=0
# i=0
# while n>0:
#     rem=n%10
#     sum=sum+ rem*pow(2,i)
#     n=n//10
#     i=i+1
# print(sum)    

  
  


# n=int(input('enter the number :'))
# for i in range(1,n+1):
#         print('*'*i)

# n=int(input('enter the number :'))
# for i in range(n+1):
#         print('*'*(n-i))


# n=int(input('enter the number :'))
# for i in range(n+1):
#     print(' '*(n-i)+'*'*i)


# n=int(input('enter the number :'))
# for i in range(n+1):
#     print(' '*i+'*'*(n-i))


# n=int(input('enter the num :'))
# for i in range(n):
#     print(' '*(n-i)+'*'*(1+2*i)+' '*(n-i))


# n=int(input('enter the number :'))
# for i in range(n):
#     print(' '*(i)+'*'*(9-2*i)+' '*i)



# n=int(input('enter the number :'))
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j,end='')
#     print()    
    
    
# n=7
# for i in range(1,n+1):
#     for j in range(1,n-i):
#         print(j,end='')    
#     print()



# n=6
# for i in range(1,n+1):
#     for j in range(1+i*2):
#         print('*'*i)


# list1=[10,51,3,4,5,6,7,8,9,30,45]
# x=sorted(list1)
# print(x)
# y=len(x)
# print(y)
# p=x[(y-3)]
# print(p)


#Write a program to print the given number is odd or even.

# n=int(input('enter the number :'))
# if n%2==0:
#         print('even')
# else:
#         print('odd')
    


#Write a program to find the given number is positive or negative.


# n=int(input('enter the number :'))    
# if n>0:
#     print('positive')
# elif n<0:
#     print('negative')  
# elif n==0:
#     print('zero')    
    
    

#Write a program to find the sum of two numbers.

# n=int(input('enter the number :')) 
# m=int(input('enter the number :'))
# sum=n+m
# print(sum)    


#Write a program to find if the given number is prime or not

# n=int(input('enter the number :'))
# count1=0
# if n==1:
#     print('prime')
# for i in range(2,n+1):
#     if n%i==0:
#         count1=count1+1
# if count1==1:
#     print('prime') 
# else:
#     print('not prime')           
        
        
#Write a program to check if the given number is palindrome or not.

# n=int(input('enter the number :'))        
# a=n
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum*10+rem
#     n=n//10
# if a==sum:
#     print('palindrome')
# else:
#     print('not palindrome')    
    
    
#Write a program to check if the given number is Armstrong or not.


# n=int(input('enter the number :'))
# a=n
# sum=0    #154
# while n>0:
#     r=n%10
#     sum=sum+r*r*r
#     n=n//10
# print(sum)   
# if a==sum:
#     print(a,'is Armstrong') 
# else:
#       print(a,'is not Armstrong')      



#Write a program to check if the given strings are anagram or not.
# def check(s1,s2):
#     if s1==s2:
#         print('is anagram')
#     else:
#         print('is not anagram')

# str1=input('enter the string :')
# str2=input('enter the string :')
# s1=sorted(str1)
# s2=sorted(str2)
# check(s1,s2)


#Write a program to find a maximum of two numbers.
# def maximum(n1,n2):
#     if n1>n2:
#         print(n1,'is max')
#     else:
#         print(n2,'max')
# n1=8
# n2=4
# maximum(n1,n2)


#Write a program to find a minimum of two numbers.
# def min(n1,n2):
#     if n1>n2:
#         print(n2,'is minimum :')
#     else:
#         print(n1,'min')     
# n1=2
# n2=1
# min(n1,n2)

#Write a program to find a maximum of three numbers.
# def maximum(a, b, c):

#     if (a >= b) and (a >= c):
#         largest = a

#     elif (b >= a) and (b >= c):
#         largest = b
#     else:
#         largest = c
        
#     return largest


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# print(maximum(a, b, c))


# Write a program to find a minimum of three numbers.


# def min(a, b, c):
#     if a>=b and b>=c:
#         min1=c
#     elif b>=c and c>=a:
#         min1=a 
#     elif c>=a and a>=b:
#         min1=b 
#     return min1         
    
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# print(min(a, b, c))


#Write a program to find a factorial of a number.
# def fat(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact    
# n=4
# print(fat(n))


#Write a program to find a fibonacci of a number.

# n=int(input('enter the number'))
# for i in range(n+1):
#     for j in range(i):
#         print('*' ,end='')
#     print()    


# n=7
# for i in range(n):
#     for j in range(5):
#         if j==0 or( (i==0 or i==3 or i==6) and (j!=0)):
#             print('*',end=' ')
#         else:
#             print(' ',end='')
#     print()        





# n=7
# for i in range(7):
#     for j in range(5):
#         if j==0 or ((i==0 or i==3 or i==6) and (j!=0 and j!=4)) or (j==4 and (i!=0 or i!=3 or i!=6)):
#             print('*',end='')
#         else:
#             print('',end='')
#     print()        


# n=7
# for i in range(7):
#     for j in range(5):
#         if j==0 or ((i==0 or i==3) and (j!=0)):
#             print('*', end=' ')
#         else:
#             print('',end='')
#     print()        


# n=7
# for i in range(7):
#     for j in range(5):
#         if j==0 or j==4 or (i==3 and (j>0 and j<4)):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()        
         
         
# n=7
# for i in range(7):
#     for j in range(5):
#         if j==0 or ((i==6) and (j!=0)):
#             print("*",end=' ')
#         else:
#             print('',end='')
#     print()   

# n=7
# for i in range(6):
#     for j in range(6):
#         if j==0 or j==5 or ((i-j==0) and( j>0 and j<5)):
#             print('*',end='')
#         else:
#             print('',end=' ')    
#     print()
             
                     
# n=7
# for i in range (7):
#     for j in range(5):
#         if ((j==0) and (i>0 and i<6)) or ((j==4) and (i>0 and i<6))  or ((i==0 or i==6) and (j>0 and j<4)):
#             print('*',end=' ')
#         else:
#             print(' ', end=' ') 
#     print()                  



# n=5
# k=1
# for i in range(1,n):
#     for j in range(i):
#         print(k,end=' ')
#         k=k+1
#     print()    


# n=5
# for i in range(1,n):
#     for j in range(5-i):
#         print((n-i),end='')
#     print()    


# n=5
# for i in range(1,5):
#     for j in range(1,6-i):
#         print(j,end='')
#     print()   


# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i):
#         print(' ',end='')
#     for j in range(i,1,-1):
#         print(j,end='')
#     for j in range(1,i+1):
#         print(j,end='')    
#     print()        