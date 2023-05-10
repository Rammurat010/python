
#281. Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. 
# Return all pairs of integers in a list. Go to the editor
# Sample Data:
# ([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
# [0, -3, -5, -7, -8] -> [[-3, 0], [-8, -5]]
# ([1, 2, 3, 4, 5]) -> [[1, 4], [2, 5]]
# ([100, 102, 103, 114, 115]) -> [[100, 103]]

# list1=[0, 3, 4, 7, 9,5]
# list2=sorted(list1)
# print(list2)
# list3=[]
# k=0
# for i in range(len(list2)+1):
#     if len(list2)>1:
#         r=[list2[k],list2[k+1]]
#         list3.append(r)
#         list2.remove(list2[k])
#         list2.remove(list2[k])
# print(list3)    


# 280. Write a Python program to extract the first specified number of vowels from a given string.
# If the specified number is less than the number of vowels present in the string then display "n is less 
# than the number of vowels present in the string". Go to the editor
# Sample Data:
# ("Python", 2) -> "n is less than number of vowels present in the string."
# ("Python Exercises", 3) -> "oEe"
# ("aeiou") -> "AEI"


# def display(str1):
#     count=0
#     str2=''
#     for i in str1:
#         if i in 'aeiouAEIOU':
#             count=count+1
#             if i not in str2:
#                 str2=str2+i
#     return count,str2            


# str1="Python Exercises"
# co,str3=display(str1)
# print(co)
# print(str3)


# 279. Write a Python program to check if each number is prime in a given list of numbers.
# Return True if all numbers are prime otherwise False. Go to the editor
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False


# def check_prime_list(list1):
#     count=0
#     for i in list1:
#         for j in range(1,i+1):
#             if i%j==0:
#                 count=count+1     
#                 print(count)          
#     if count==2:  
#         if count==len(list1):
#             print('True')  
#         else:
#             print('false')            
        
# list1=[1,3,17,7,11]
# check_prime_list(list1)


# 277. Write a Python program to calculate the largest and smallest gap between sorted elements of a list of integers.
# Go to the editor
# Sample Data:
# {1, 2 ,9, 0, 4, 6} -> 3
# {23, -2, 45, 38, 12, 4, 6} -> 15

# list1 =[23, -2, 45, 38, 12, 4, 6]
# r=sorted(list1)
# print(r[0]-r[1])

# Write a Python program to sum the missing numbers in a given list of integers. Go to the editor
# Sample Data:
# ([0, 3, 4, 7, 9]) -> 22
# ([44, 45, 48]) -> 93
# ([-7, -5, -4, 0]) -> -12


# def  sum_list(list1):
#     sum=0
#     for i in list1:
#         sum=sum+i
#     return sum   
    
    
# list1=[0, 3, 4, 7, 9]
# print(sum_list(list1))
# sum=0


# list2=[44, 45, 48]
# print(sum_list(list2))
# sum=0


# list3=[-7, -5, -4, 0]
# print(sum_list(list1))


# 276. Write a Python program to find the largest odd number in a given list of integers. Go to the editor
# Sample Data:
# ([0, 9, 2, 4, 5, 6]) -> 9
# ([-4, 0, 6, 1, 0, 2]) -> 1
# ([1, 2, 3]) -> 3
# ([-4, 0, 5, 1, 0, 1]) -> 5


# def largest_even_odd(list1):
#     list_even=[]
#     list_odd=[]
#     for i in list1:
#         if i%2==0:
#             list_even.append(i)
#         else:
#             list_odd.append(i)
#     e=sorted(list_even)  
#     print(e[-1]) 
#     o=sorted(list_odd)  
#     print(o[-1])      
                
# list1=[0, 9, 2, 4, 5, 6]
# largest_even_odd(list1)


# 275. Write a Python program to add all elements of a list of integers except the number at index.
# Return the updated string. Go to the editor
# Sample Data:
# ([0, 9, 2, 4, 5, 6] -> [26, 17, 24, 22, 21, 20]
# ([-4, 0, 6, 1, 0, 2]) -> [9, 5, -1, 4, 5, 3]
# ([1, 2, 3]) -> [5, 4, 3]
# ([-4, 0, 5, 1, 0, 1]) -> [7, 3, -2, 2, 3, 2]


# def update_string(lis1):
#     sum=0
#     list2=[]
#     for i in lis1:
#         sum=sum+i
#     for j in range(len(lis1)):
#         r=sum-lis1[j]
#         list2.append(r)
#     return list2
    
            

# lis1=[0, 9, 2, 4, 5, 6] 
# p=update_string(lis1)
# print(p)

# 274. Write a Python program to count the lowercase letters in a given list of words. Go to the editor
# Sample Data:
# (["Red", "Green", "Blue", "White"]) -> 13
# (["SQL", "C++", "C"]) -> 0

# list1=["Red", "Green", "Blue", "White"]
# count=0
# for i in list1:
#     for j in i:
#         if j.islower():
#             count=count+1
# print(count)  


# 272. Write a Python program to generate a list of numbers in the arithmetic progression starting with the 
# given positive integer and up to the specified limit. Go to the editor
# Sample Output:


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
# [5, 10, 15, 20, 25]
# list1=[]
# list2=[]
# list3=[]

#     if i<16:
#         list1.append(i)
#     elif i%3==0:
#         list2.append(i)
#     else:
#         if i<26:
#             if i%5==0:
#                 list3.append(i)                  
# print(list1)         
# print(list2)      
# print(list3)             


# 271.Write a Python program to check if there are duplicate values in a given flat list. Go to the editor
# Sample Output:
# Original list:
# [1, 2, 3, 4, 5, 6, 7]
# Check if there are duplicate values in the said given flat list:
# False
# Original list:
# [1, 2, 3, 3, 4, 5, 5, 6, 7]
# Check if there are duplicate values in the said given flat list:
# True

# list1=[1, 2, 3, 3, 4, 5, 5, 6, 7]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)        
# if len(list2)==len(list2):
#     print(True)
# else:
#     print(False)




# 270. Write a Python program to check if the elements of the first list are contained in the second one
# regardless of order. Go to the editor
# Sample Output:
# True
# True
# False
# True

# 269. Write a Python program to get every nth element in a given list. Go to the editor
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10]
# [5, 10]
# [6]



# 267. Write a Python program to get the cumulative sum of the elements of a given list. Go to the editor
# Sample Output:
# Original list elements:
# [1, 2, 3, 4]
# Cumulative sum of the elements of the said list:
# [1, 3, 6, 10]



# list1=[1, 2, 3, 4]
# list2=[]
# sum=0
# for i in range(len(list1)):
#     sum=sum+list1[i]
#     list2.append(sum)    
# print(list2)    
    
# n=5    
# list1=[]
# a=0
# b=1
# if n==1:
#     list1.append(a)
# elif n==2:
#     list1.append(a)   
#     list1.append(b)  
# else:
#     list1.append(a)   
#     list1.append(b)       
#     for i in range(n+1):
#         c=a+b
#         a=b
#         b=c
#         list1.append(c)
# print(list1)        


# 261. Write a Python program to get the most frequent element in a given list of numbers. Go to the editor
# Sample Output:
# 2
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# Item with maximum frequency of the said list:
# 2

# list1=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# count=0
# for i in list1:
#     l=list1.count(i)
#     if l >count:
#         count=l
#         print(i)   
   


# 259. Write a Python program to check if a given function returns True for at least one element in the list. Go to the editor
# Sample Output:
# False
# True
# False

# 257. Write a Python program to check if two given lists contain the same elements regardless of order. Go to the editor
# Sample Output:
# Original list elements:
# [1, 2, 4]
# [2, 4, 1]
# Check two said lists contain the same elements regardless of order!
# True
# Original list elements:
# [1, 2, 3]
# [1, 2, 3]
# Check two said lists contain the same elements regardless of order!
# True
# Original list elements:
# [1, 2, 3]
# [1, 2, 4]
# Check two said lists contain the same elements regardless of order!
# False


# list1=[1, 5, 4]
# list2= [2, 4, 1]
# sum1=0
# sum2=0
# for i in list1:
#     sum1=sum1+i
# for j in list2:
#     sum2=sum2+j
# if sum2==sum1:
#     print(True)
# else:
#     print(False)        


# 255. Write a Python program to perform a deep flattening of a list. Go to the editor
# Sample Output:
# Original list elements:
# [1, [2], [[3], [4], 5], 6]
# Deep flatten the said list:
# [1, 2, 3, 4, 5, 6]
# Original list elements:
# [[[1, 2, 3], [4, 5]], 6]
# Deep flatten the said list:
# [1, 2, 3, 4, 5, 6]


# list1=[1, [2], [[3], [4], 5], 6]
# list2=[]
# for i in list1:
#     if type(i)==list:
#         for k in i:
#             list2.append(k)
#     else:
#          list2.append(i)       
# print(list2)        


# 254. Write a Python program to get the weighted average of two or more numbers. Go to the editor
# Sample Output:
# Original list elements:
# [10, 50, 40]
# [2, 5, 3]
# Weighted average of the said two list of numbers:
# 39.0
# Original list elements:
# [82, 90, 76, 83]
# [0.2, 0.35, 0.45, 32]
# Weighted average of the said two list of numbers:
# 82.97272727272727



# 253. Write a Python program to get the n minimum elements from a given list of numbers. Go to the editor
# Sample Output:
# Original list elements:
# [1, 2, 3]
# Minimum values of the said list: [1]
# Original list elements:
# [1, 2, 3]
# Two minimum values of the said list: [1, 2]
# Original list elements:
# [-2, -3, -1, -2, -4, 0, -5]
# Threee minimum values of the said list: [-5, -4, -3]
# Original list elements:
# [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
# Two minimum values of the said list: [2, 2.2]

# list1=[1, 2, 3]
# list2=[]
# min_values=list[0]
# for i in range(len(list1)):
#     if min_values<list[i]:
#         min_values=list[i]
# print((min_values))        
        
        

# 251. Write a Python program that fills a list with the specified value. Go to the editor
# Sample Output:
# [0, 0, 0, 0, 0, 0, 0]
# [3, 3, 3, 3, 3, 3, 3, 3]
# [-2, -2, -2, -2, -2]
# [3.2, 3.2, 3.2, 3.2, 3.2]

# n=int(input('enter the number'))
# b=int(input('enter the value'))
# list1=[]
# for i in range(n+1):
#     list1.append(b)
# print(list1)    




# 250. Write a Python program to calculate the sum of a list, after mapping each element to a value using the 
# provided function. Go to the editor
# Sample Output:
# 20

# list=[{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]
# sum=0
# for i in list:
#     for j in i.values():
#         sum=sum+j
# print(sum)    

249. Write a Python program to get the minimum value of a list, after mapping each element to a value using a given function. Go to the editor
Sample Output:
2