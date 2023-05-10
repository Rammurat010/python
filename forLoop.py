# a=range(-1, -10, -2)
# for i in a:
#  print(i)

# a=range(10, 0, -2)
# for i in a:
#  print(i)

# st ="nitish"
# n=len(st)
# for i in range(n):
#     print(i ,"=",st[i])
#     print("rest of the code")   

# st ="nitish"
# for i in st:
#     print(i)
# else:
#     print("enter the part")
# print("Rest of the code")


# nested for loop
# for i in range(2):
#     print("outer loop", i)
#     for j in range(3):
#         print("inner loop", j)

# for i in range(5):
#     print(i)
#     for j in range(i):
#         print(i, end=' ')
# print("A"*4)
# limit=int(input("Enter the number"))
# for i in range(1,limit):
#     print("*"*i)



#Number Pattern
# row=5
# for i in range(1,row +1,1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print("")    


# n=int(input("Enter the value :" ))
# if n%2==0:
#     print("even")
# elif n%2!=0:   
#   print("odd") 
# elif n==0:
#     print("0 is not even or odd ")  


# print('Rammurat',end='@')
# print('Vishal',end=' ')
# print('Ambresh')

# s='Ram Ji'
# print(s[2:])

# a =['ram',10]
# for i in range():

# emp1 = { "name": "Amit", "basic salary": 4567, "allowance": 890}
# emp2 = { "name": "Manoj", "basic salary": 7890, "allowance": 99}

# totalEmp=[emp1,emp2]

# for emp in totalEmp:
#     print(emp)


# a=['Ram',10]

# for i in range(len(a)):
#     print(a[i], end='')



# num=[{"pappu" :"A"}, {"rahul" , "B"}, {"Rakesh" , "C"}, {"Mohit" ,"D"}, {"Rohan" , "E"}]
# for i in num:
#     if 
#     print('name',"has a grade"'A')

# rrr=int
# for i in range(5):
#     if rrr>15:
#         print("larger nub")
#     elif rrr<4 : 
#         print("small")
#     elif rrr==5:
#         print('equal')  
#     elif rrr!=0:
#         print('equal to zero') 
#     elif rrr==7:
#         print("mid nub")
#         Break:

# for 10 employees take input from user to create a list like
# [{"Name":"Atul", "Basic Salary":10000,"Allowance":2000},{"Name":"Alkesh", "Basic Salary":12000,
# "Allowance":1000},
# {"Name":"Rammurat", "Basic Salary":20000,"Allowance":2000}]
# emp1 = { "name": "atul", "basic salary": 10000, "allowance": 2000}
# emp2 = { "name": "alkesh", "basic salary": 12000, "allowance": 1000}
# emp3 = { "name": "rammurat", "basic salary": 20000, "allowance": 2000}
# totalEmp=[emp1,emp2,emp3]
# for i in totalEmp:
#     print(i)



# emps=int(input("enter the emp"))
# basic_salary=int(input("enter the basic salary"))
# allowances = int(input("enter the basic allowances"))
# a=[{}]



# statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
 
# print('List Of given states and their capitals:\n')
 
# # Iterating over values
# for state, capital in statesAndCapitals.items():
#     print(state, ":", capital)


# isGuess=True
# number=10
# while isGuess:
#     guess=int(input('Enter a guess: '))
#     if guess>number:
#         print('Guess number is greater than correct number')
#     elif guess<number:
#         print('Guess number is smaller than correct number')
#     elif number==guess:
#         print('Guess number is equal to correct number')
#         isGuess=False


# Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
# between 1500 and 2700 (both included).


# for i in range(1500,2700,1):
#     if i&7==0 and i%5==0:
#         print(i)


''' Write a Python program to guess a number between 1 and 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess


* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.'''



# for i in range(5):
#     for j in range(i):
#         print('*',end='')
#     print()    
        
        
#Write a Python program that accepts a word from the user and reverses it


# str1=input('enetr tha string :')
# reverse_str=''
# for i in str1:
#     reverse_str=i+reverse_str
# print(reverse_str)    

# Write a Python program to count the number of even and odd numbers in a series of numbers



# Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# list1 = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# for i in list1:
#     print(i,'is type ',type(i))
    
    
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5    
# n=6
# for i in range(n+1):
#     if i==3 or i==6:
#         continue
#     print(i,end=' ')
    
      
      
#Write a Python program to get the Fibonacci series between 0 and 50. Go to the editor
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34            
            
# n=50
# a=0
# b=1
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     if b>50:
#         print(b) 
#         break   
                
#  Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" 
#  instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and 
#  five, print "FizzBuzz".                
# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)



#  Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
#  The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints
# the lines as output (all characters in lower case).

#  Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. 
#  The program will print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

# n=(input('enter the number :'))
# list1=n.split(',')
# for i in list1:
#     p=int(i,2)	
#     print(p)
 
 
 
# items = []
# num = [x for x in input().split(',')]
# for p in num:
#     x = int(p, 2)
#     if not x%5:
#         items.append(p)
# print(','.join(items))


# Write a Python program that accepts a string and calculates the number of digits and letters. Go to the editor
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

# str1= 'Python 3.2'
# count=0
# count1=0
# for i in str1:
#     if i.isalpha():
#         count=count+1
#     elif i.isdigit():
#         count1=count1+1
# print(count1)   
# print(count)     
        
        


# Write a Python program to check the validity of passwords input by users. Go to the editor
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.        


# str1='Rammurat@123'
# count=0
# str2=(input('enter the passwords :'))
# for i in str2:
#     if i in str1:
#         count=count+1
# print(count)        
# if count==len(str1): 
#     print('find the passwords') 
# else:
#     print('wrong passwords')          


# l, u, p, d = 5, 7, 8, 0
# print(l)


#Write a Python program to find numbers between 100 and 400 (both included) 
# where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
    

# list1=[]
# for i in range(100,401):
#     if i%2==0:
#         list1.append(i,)
# print(list1)        


# for i in range(7):
#     for j in range(5):
#         if   (j==0 or j==4) and i!=0 or (i ==0 or i==3) and (j>0 and j<4):
#             print('*',end='')
#         else:
#             print(' ',end='')
    
#     print()        


# for i in range(7):
#     for j in range(5):
#         if j==0 or j==4 and (i!=0 and i!=6) or (i==0 or i==6) and (j>0 and j<4):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()        

# Write a Python program to calculate a dog's age in dog years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73



#Write a Python program to check whether an alphabet is a vowel or consonant.
# n='a'
# if n in 'a,e,i,o,u,A,E,I,O,U':
#     print('vowel')
# else:
#     print('consonant')
    
    
#  Write a Python program to convert a month name to a number of days. Go to the editor
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days     


#Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.

# a=9
# b=9
# c=a+b
# if c>=15 and c<=20:
#     print('20')
# else:
#     print(c)
    
    
#Write a Python program that checks whether a string represents an integer or not. Go to the editor
# Expected Output:

# Input a string: Python                                                  
# The string is not an integer.      


# Write a Python program that checks whether a string represents an integer or not. Go to the editor
# Expected Output:

# Input a string: Python                                                  
# The string is not an integer.  

# str1='murat'
# for i in str1:
#     if type(i) in str:
#         print('this string is not a integer')\
    
    
# 36. Write a Python program to check if a triangle is equilateral, isosceles or scalene. Go to the editor
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:

# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle     

# x=6                                                                    
# y= 8                                                                    
# z= 12 
# if x==y==z:
#     print('equilateral')
# elif x==y or x==z or y==x:
#     print('isosceles')    
# else:
#     print('scalene')    
    
    
# Write a Python program that reads two integers representing a month and day and prints the season for 
# that month and day. Go to the editor
# Expected Output:

# Input the month (e.g. January, February etc.): july                     
# Input the day: 31                                                       
# Season is autumn     


# . Write a Python program to find the median of three values. Go to the editor
# Expected Output:

# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0   

# a=15
# b=26
# c=29
# m=(a+b+c)/3
# print(m)
# n=int(input('enter the number :'))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end='')
#     print()    

# Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

#  Write a Python program to split a given dictionary of lists into lists of dictionaries. Go to the editor
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
    
    
# dic1={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# dict2={}
# listk=[]
# listv=[]
# for i,j in dic1.items():
#     listk.append(i)
#     listv.append(j)
        
# print(dict2)        
        
        
#  Write a Python program to remove a specified dictionary from a given list. Go to the editor
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},
#  {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]        


# dict1= [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},
#  {'id': '#808000', 'color': 'Olive'}]
# print(dict1[1:])



# Write a Python program to convert string values of a given dictionary into integer/float datatypes. Go to the editor
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
# Click me to see the sample solution

# dic1=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# dic2={}
# list=[dic2]
# for i in dic1:
#     for a,b in i.items():
#         dic2[a]=int(b)
# print(list)        


#  A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.
#  Go to the editor
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

# dic1={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# dic2={}
# for i,j in dic1.items():
#     dic2[i]=[]
# print(dic2)    
    
# A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
# Go to the editor
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

# dic1={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# dic2={}
# for k in dic1.items():
#     for i in k:
#         if i=='math':
#             dic2[i]=[j+1]
#         elif i== 'Physics':
#             dic2[i]=[j-2]
#         elif i== 'Chemistry':
#             dic2[i]=[j]    
# print(dic2)            
    
    

# Write a Python program to extract a list of values from a given list of dictionaries. Go to the editor
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]


# dic1=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# list1=[]
# for i in dic1:
#     for j in i.keys():
#         if j=='Math':
#           list1=list1+[(i[j])]
# print(list1)            




# Write a Python program to find the length of a dictionary of values. Go to the editor
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}


# dic1={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'blackiududug'}
# dic2={}
# for val in dic1.values():
#     dic2[val]=len(val)
# print(dic1)  
# print(dic2)    



# Write a Python program to access dictionary key's element by index. Go to the editor
# Expected Output:
# physics
# math
# chemistry

# dic1 = {'physics': 80, 'math': 90, 'chemistry': 86}
# di2=[dic1]
# print(di2[:1])

# Write a Python program to convert a dictionary into a list of lists. Go to the editor
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


# dic1={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dic2={}
# for i,j in dic1.items():
#     dic2[i]=[j]
# print(dic2)    
    
    
# rite a Python program to filter even numbers from a dictionary of values. Go to the editor
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}    
    
    
# dict1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# dict2={}
# for i,j in dict1.items(): 
#     if j>=4:
#         dict2[v]
        
# Write a Python program to find the specified number of maximum values in a given dictionary. Go to the editor
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']        
           
# dic1={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 105, 'g': 57, 'h': 8, 'i': 100}
# for k in range(3):
#     for i in dic1.keys():    
#         max_val='a'
#         if i>max_val:
#             max_val=dic1['a']
#         else:
#             dic1.pop(i)           
# print(max_val)  
# sortedList=sorted(dic1.items(),key=lambda v:v[1])     
#sortedDict=dict()
# print(sortedList[-3])


# Write a Python program to count the frequency of a dictionary. Go to the editor
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

# dic1={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# dic2={}
# list1=[]
# for i,j in dic1.items():
#   list1.append(j)
# print(list1)  
# for i in list1:
#     y=list1.count(i) 
#     print(y)     
    
    
# Write a Python program that creates key-value list pairings within a dictionary. Go to the editor
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
# Click me to see the sample solution    
  
  
# dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}  
# dic1={}
# for i,j in dic.items():
#     dic1[i]= 
# print(dic1)    




# Write a Python program to find a tuple, the smallest second index value from a list of tuples

# list1= [(4, 1), (1, 2), (6, 0)]
# sorted_list1=sorted(list1,key=lambda list1: list1[1])
# print(sorted_list1)

#Write a Python program to create a list of empty dictionaries. 

# n=6
# list2=[]
# for i in range(n):
#     list2.append({})
# print(list2)    

#Write a Python program to print a list of space-separated elements.
# num = [1, 2, 3, 4, 5]
# list1=[]
# for i in num:
#     if i :
#         list1.append(i)
#     else:
#         del(i)    
# print(list1) 

# Write a Python program to insert a given string at the beginning of all items in a list. Go to the editor
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']       


# list1=[1,2,3,4]
# list2=[]
# k=1
# for i in list1:
#     list2.append('emp'+str(i))
#     k=k+1
# print(list2)    

#Write a Python program to iterate over two lists simultaneously.
# num = [1, 2, 3]
# color = ['red', 'white', 'black']
# for i in color:
#     for j in num:
#         print(j,i)
#         break

# Write a Python program to move all zero digits to the end of a given list of numbers. Go to the editor
# Expected output:
# Original list:
# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# list1=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# list2=[]
# for i in list1:
#     if i !=0:
#         list2.append(i)
# print(list2)        

# Write a Python program to find the list in a list of lists whose sum of elements is the highest. Go to the editor
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

# list1=[1,2,3], [4,5,6], [10,11,12], [7,8,9]

# list2=''
# for i in list1:
#     if i==list1[2]:
#         list2=list2+str(i)  
# print(list2)      

# Write a Python program to find all the values in a list that are greater than a specified number. 

# list1 = [220, 330, 500]
# list2 = [12, 17, 21]
# n=14
# for i in list1:
#     for j in list2:
#         if n>i and n>j:
#             print('True')
#         else:
#              print('false')

# Write a Python program to extend a list without appending. Go to the editor
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]




# Write a Python program to find items starting with a specific character from a list. Go to the editor
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:

# list=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# list2=list[:2]
# list3=list[-1]
# list4=str(list2)+str([list3])
# print(list4)

#  Write a Python program to check whether all dictionaries in a list are empty or not. Go to the editor
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

# list1 = [{},{5},{},{}]
# list2={}
# for i in list1:
#     if i=={}:
#         x=True
#     else:
#         x=False
# print(x)            
        
        
# Write a Python program to flatten a given nested list structure. Go to the editor
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]        

# list1= (0, 10,90, 100, 110, 120)
# print(list1.add(1))



# A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary. 
# Go to the editor
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

# dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# dic1={}
# for i,j in dict.items():
#     dic1[i]=[]
# print(dic1)    
    
# A Python Dictionary contains List as a value. Write a Python program to update the list values in 
# the said dictionary. Go to the editor
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}   


# Write a Python program to extract a list of values from a given list of dictionaries. Go to the editor
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]

# dic1=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# list1=[]
# for k in dic1:
#     for i,j in k.items(): 
#         if i=='Science':
#             print(j)
#             list1.append(j)
# print(list1)        




# Write a Python program to find the length of a dictionary of values. Go to the editor
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

# dic1={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dic2={}
# for i,j in dic1.items():
#     dic2[j]=len(j)
# print(dic2)    


# Write a Python program to filter even numbers from a dictionary of values. Go to the editor
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

# dic1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# dic2={}
# for i,j in dic1.items():
#     print(j)
#     dic2[i]=j[1:]
# print(dic2)     

# Write a Python program to find the specified number of maximum values in a given dictionary. Go to the editor
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']   
    
# dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 105}
# for k in range(3):
#     for i,j in dict.items():
#         max_kay='a'
#         if i>max_kay:
#             max_kay=dict[i]
#         else:
#             dict.pop(i)    
# print(max_kay)