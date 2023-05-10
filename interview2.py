# tuple1=(4,6,7,8)
# print(tuple1[::-1])


# Access value 20 from the tuple

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# c=tuple1[2][2]
# print(c)


#Create a tuple with single item 50

# tuple1=(50,)
# print(type(tuple1))


# Unpack the tuple into 4 variables

# tuple1=(4,56,7,8)
# a,c,g,e=tuple1
# print(a)


#Swap two tuples in Python
# t1=(4,5,6)
# t2=(4,6,8)

# p=t1
# t1=t2
# t2=p
# print(t1,t2)


# Copy specific elements from one tuple to a new tuple

# tuple1 = (11, 22, 33, 44, 55, 66)

# Reverse each word of a string

# tuple1=('rammurT')
# w=tuple1[::-1]
# print(w)

#Remove items from a list while iterating 



# dict_1={100:"python",200:"Java",300:"Ruby",400:"C",500:"C++",600:"R"}
# print("Dictionary:",dict_1)
# d_temp={}
# index=0
# for i in dict_1.values():
#     d_temp[i]=list(dict_1.keys())[index]
#     index+=1
# print("Reversed dictionary:",d_temp)


#Display all duplicate items from a list

# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# list1=[]
# list2=[]
# for i in sample_list:
#     if i  not in list1:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list2)        


#Filter dictionary to contain keys present in the given list

# Add a list of elements to a set

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

# sample_set.update(sample_list)
# print(sample_set)

#Return a new set of identical items from two sets

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3=set1+set2
# print(set3)


#create a tuple
# tuplex = ((2, "w"),(3, "r"))
# for x, y in tuplex:
#     print(dict(y, x)) 

# Converting an Integer into Decimals
# n=8
# sum=''
# while n>0:
#     rem=n%2
#     sum=str(rem)+sum
#     n=n//2    
# print(sum)

#Converting an String of Integers into Decimals

# n='98'
# r=int(n)
# sum=''
# while r>0:
#     rem=r%2
#     sum=str(rem)+sum
#     r=r//2
# print(sum)

# Reversing a String using an Extended Slicing Technique

# str1='ram'
# print(str1[::-1])

# Counting Vowels in a Given Word

# str1='rammurat'
# count=0
# for i in str1:
#     if i in 'aeiouAEIUO':
#         count=count+1
# print(count)        


#Counting Consonants in a Given Word

# str1='rammurat'
# count=0
# for i in str1:
#     if i not in 'aeiouAEIUO':
#         count=count+1
# print(count)  

#Counting the Number of Occurances of a Character in a String

#Writing Fibonacci Series
# n=5
# a=0
# b=1
# print(0)
# print(1)
# for i in range(n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)     


#Finding the Maximum Number in a List

# list1=[2,3,4,5,6,88,76,44]
# max_value=list1[0]
# for i in list1:
#     if i>max_value:
#         max_value=i
# print(max_value)        


#Finding the Minimum Number in a List

# list1=[21,37,84,5,6,88,76,44]
# mim_value=list1[0]
# for i in list1:
#     if i< mim_value:
#         mim_value=i
# print(mim_value)        

#Finding the Middle Element in a List
# list1=[21,37,84,5,6,88,76,44]
# mid_element=int(len(list1)/2)
# print(list1[mid_element])

 #Converting a List into a String
 
# list1=[21,37,84,5,6,88,76,44]
# sum=''
# for i in list1:
#     sum=sum+str(i)
# print(sum)    

#Adding Two List Elements Together

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6] 
# list3=[]
# for i in range(len(lst1)):
#     list3.append(lst1[i]+lst2[i])
# print(list3)    

#Comparing Two Strings for Anagrams


# s1 = "listen"
# s2 = "silenz"
# count=0
# for i in s1:
#     for j in s2:
#         if i==j:
#             count=count+1
# if len(s1) ==count:
#     print('yes')
# else:
#     print('no')    

#Checking for Palindrome Using Extended Slicing Technique



#Write a Python program to convert a list of characters into a string.

# list1=[3,4,5,5,66,'j'] 
# sum=''
# for i in list1:
#     sum=sum+str(i)
# print(sum)    
     
     
# Write a Python program to find the index of an item in a specified list. 
   
# list1=[3,4,5,5,66,6,5]
# x=list1.index(5) 
# print(x)     


#Write a Python program to flatten a shallow list

# list1=[[2, 3, 4], [3, 2, 4], [5, 8]]
# list2=[]
# for i in list1:
#     for j in i:
#         list2.append(j)
# print(list2)        


#Write a Python program to append a list to the second list.
# list1=[3,4,5,5,66,6,5]
# list2=[]
# for i in list1:
#     list2.append(i)
# print(list2)    



# Write a Python program to select an item randomly from a list.
# import random
# list1=[3,4,5,5,66,6,5]
# print(random.choice(list1))


# Write a Python program to check whether two lists are circularly identical.

# Write a Python program to get the frequency of elements in a list.

#Write a Python program to find the greatest common divisor (GCD) of two integers.



# n=15
# a=5
# list1=[]
# for i in range(1,6):
#     if n%i==0:
#         list1.append(i)
# x=max(list1)      
# print(x)  

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and prints the result. Go to the editor
# Sample Output:
# 25
# 48

# add=lambda n:15+n
        
# n=10        
# print(add(n))   

# mul=lambda n:15*n
        
# n=10        
# print(mul(n))     

# Write a Python program to create a function that takes one argument, and that argument will be
# multiplied with an unknown given number. Go to the editor
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75  

# def lambda1(n):
#     print('Double the number of',n,'=',n*2)

# n=15
# print(lambda1(n))


# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# list1 =[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print(sorted(list1,key=lambda list1: list1[0]))
# print(sorted(list1,key=lambda list1: list1[0]))


# Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]



#Python program to remove given character from String.
# str1='rammurat'
# str2=''
# n=input('enter the object :')
# for i in str1:
#     if i==n:
#         str2=str2+''
#     else:
#         str2=str2+i    
# print(str2)        


#Python Program to count occurrence of a given characters in string.


# str1='rammurat'
# count=0
# for i in str1:
#     count=count+1
# print(count)    

#Python Program to check if two Strings are Anagram.
# str2='rammurat'
# str1='rammtaru'
# count=0
# for i in str1:
#     if i in str1:
#         count=count+1
# if count==len(str2):
#     print('Anagram')  
# else:
#     print('not Anagram')      
    
    
#Python program to check a String is palindrome or not.    


# str1=input('enter the string :')
# sum=''
# for i in str1:
#     sum=i+sum
# if str1==sum:
#     print('pal')
# else:
#     print('not pal')    
    
#Python program to check given character is vowel or consonant    


# str1=input('enter the string :')
# for i in str1:
#     if i in 'aeiouAEIOU':
#         print('vowel')
#     else:
#         print('consonant')
        
#Python program to check given character is digit or not.       

# n=input('enter the character :') 
# str1=''
# for i in n:
#     if i.isdigit():
#         str1=str1+i
#     else:
#         pass
# print(str1)   



#Python program to check given character is digit or not using isdigit() method.


#Python program to replace the string space with a given character.


# str1='hi murat how are you'
# str2=''
# for i in str1:
#     r=str1.replace(' ','')    
# print(r)         


#Python program to replace the string space with a given character using replace() method.


#Python program to convert lowercase char to uppercase of string.
# str1='rammuratYA'
# str2=''
# for i in str1:
#     r=i.upper() 
#     str2=str2+r
# print(str2)     


#Python program to convert lowercase vowel to uppercase in string.

# str1='rammuratAEI'
# str2=''
# for i in str1:
#     if i in 'aeiou':
#         r=i.upper()
#         str2=str2+r
#     else:
#         str2=str2+i
# print(str2)


#Python program to delete vowels in a given string.

# str1='rammuratAEI'
# str2=''
# for i in str1:
#     if i in 'aeiouAEIUO':
#         str2=str2+''
#     else:
#         str2=str2+i
# print(str2)

#Python program to count Occurrence Of Vowels & Consonants in a String.


# str1='rammuratAEI'
# count1=0
# count2=0
# for i in str1:
#     if i in 'aeiouAEIUO':
#         count1=count1+1
#     else:
#         count2=count2+1
# print(count1)
# print(count2)

#Python program to print the highest frequency character in a String.
# str1='rammuaar'
# for i in str1:
#     r=count(i)


#Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
# str1='rammurat'
# str2=''
# for i in str1:
#     if i in 'aeiuoAEIOU':
#         str2=str2+'-'
#     else:
#         str2=str2+i
# print(str2)


#Python program to count alphabets, digits and special characters.

# str1='rammurat@12345'
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

#Python program to concatenate two strings using join() method.
#Python program to concatenate two strings without using join() method.

# str1='rammurat'
# str2='yadav'
# r=' '.join([str1,str2])
# print(r)

# str1='rammurat'
# str2='yadav'
# str3=str1+' '+str2
# print(str3)

        
        
#Python program to remove repeated character from string.
# str1='rammurat'
# str2=''
# for i in str1:
#     if i not in str2:
#         str2=str2+i
#     else:
#         pass
# print(str2)        
            
            
#Python program to calculate sum of integers in string.

# sum=0
# str='ram123423#$% '    
# for i in str:
#     if i.isdigit():
#         sum=sum+int(i)
#     else:
#         pass
# print(sum)    


#Python program to print all non repeating character in string.

# str1='rammurat'
# str2=''
# for i in str1:
#     if i not in str2:
#         str2=str2+i
# print(str2)       



#Python program to copy one string to another string.
# str1='rammurat'
# str2.copy(str1)

       