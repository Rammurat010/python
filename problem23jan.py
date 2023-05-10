#1: Write a Python function that takes a list of integers as an argument and returns the sum of 
# all the even numbers in the list.
# list1=[3,4,5,6,7,8,9]
# def sumeven(list1):
#     sum=0
#     for i in list1:
#      if i%2==0:
#       sum=sum+i
#     return sum            
# print(sumeven((list1)))



#2: Write a Python function that takes a string as an argument and returns a new string 
# with all the vowels removed.
# str1= input('Enter the string :')
# def pappu(str1):
#      result=''
#      for i in str1:
#        if i not in "AEIOUaeiou":
#             result=result+i
#      return result  
# print(pappu(str1))          



#3: Write a Python function that takes a dictionary as an argument and returns a 
# list of all the keys in the dictionary.


# dct={'name':'pappu','age':26,'mobilenum':764872764}
# def keys(dct):
#     list=[]
#     for i in dct:
#       list.append(i)
#     return list
# print(keys(dct))      


#4: Write a Python function that takes a list of strings as an argument and 
# returns the longest string in the list.



# list=['ram','rammurat','pappu','mohan']
# def longest_string(list):
#     maxlen=0
#     for i in list:
#         if len(i)>maxlen:
#             maxlen=len(i)
#             str1=i
#     return str1
# print(longest_string(list))    



#5: Write a Python function that takes a list of integers as an argument and returns a new list of all
#  the prime numbers in the original list.


# list=[4,45,7,9,11,8,25,22,31]
# def prime_numbers(list):
#     list1=[]
#     count=0
#     for i in list:
#        for j in range(1,i+1):
#         if i%j==0:
#            count=count+1
#         else:
#             pass   
#        if count==2:
#         list1.append(i)
#        else:
#         pass 
#     return list1  
# print(prime_numbers(list)) 

number=35
def prime_number(number):
    i=1
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count=count+1
        if count==2:
            print('prime number',number)
            break
        else:    
          print('not prime number',number)
    return number
print(prime_number(number))       



