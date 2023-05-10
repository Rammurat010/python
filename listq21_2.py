# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 
# or more and the first and last characters are the same. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']


# List1 = ['abc', 'xyz', 'aba', '1221']
# count=0
# for i in List1:
#     if len(i)>1 and i[0]==i[-1]:
#         count=count+1
# print(count)        


# def match_words(words):
#   ctr = 0

#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       ctr += 1
#   return ctr

# print(match_words(['abc', 'xyz', 'aba', '1221']))



# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a
# given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# r=sorted(list1, key=lambda list1 : list1[1] )
# print(r)


#Write a Python program to remove duplicates from a list.

# list1=[4,5,6,7,56,89,6,5]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)        

# Write a Python program to check if a list is empty or not. 
# n=[5,6]



#Write a Python program to clone or copy a list. 


# list1=[4,5,6,7,56,89,6,5]
# l=list1.copy()
# print(l)

#Write a Python program to find the list of words that are longer than n from a given list of words.

# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# Write a Python function that takes two lists and returns True if they have at least one common member.


# list1=[3,4,67,95,7,8]
# list2=[1,2,12,67]
# for i in list1:
#     for j in list2:
#         if i==j:
#             print(True)


#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# List1 =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# List1.pop(0)
# List1.pop(3)
# List1.pop(3)
# print(List1)
            
# Write a Python program to generate a 3*4*6 3D array whose each element is *

#Write a Python program to print the numbers of a specified list after removing even numbers from it. 


# list1=[2,3,4,5,6,7,8]
# list2=[]
# for i in list1:
#     if i%2!=0:
#         list2.append(i)
#     else:
#         pass
# print(list2)        

#Write a Python program to shuffle and print a specified list.


# Write a Python program to generate and print a list of the first and last 5 elements where the values are
# square numbers between 1 and 30 (both included). 


# n=30
# list2=[]
# for i in range(1,n+1):
#     list2.append(i*i)
# print(list2[:5])  
# print(list2[-5:])  
             
      
# Write a Python program to generate and print a list except for the first 5 elements, where the values are square numbers
# between 1 and 30 (both included).   

# n=30
# list2=[]
# for i in range(1,n+1):
#     list2.append(i*i)
# print(list2[5:])   

        
        
#Write a Python program to generate all permutations of a list in Python.


#Write a Python program to access the index of a list.

# list1=[24,35,4,5,6,7,8]
# n=len(list1)
# for i in list1:
#        print(n,i)
       
       
# 191. Write a Python program to find the maximum and minimum values of the three given lists.  
# Original lists:
# [2, 3, 5, 8, 7, 2, 3]
# [4, 3, 9, 0, 4, 3, 9]
# [2, 1, 5, 6, 5, 5, 4]
# Maximum value of the said three lists:
# 9
# Minimum value of the said three lists:
# 0       


# list1=[2, 3, 5, 8, 7, 2, 3]
# list2=[4, 3, 9, 0, 4, 3, 9]
# list3=[2, 1, 5, 6, 5, 5, 4]
# list4=list1+list2+list3
# max_value=list4[0]
# for i in list4:
#        if max_value<i:
#               max_value=i
# print(max_value)              



# list1=[2, 3, 5, 8, 7, 2, 3]
# list2=[4, 3, 9, 0, 4, 3, 9]
# list3=[2, 1, 5, 6, 5, 5, 4]
# list4=list1+list2+list3
# min_value=list4[0]
# for i in list4:
#        if min_value>i:
#               min_value=i
# print(min_value) 




# 190. Write a Python program to find the specified number of largest products from two given lists, 
# multiplying an element from each list.  
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [3, 6, 8, 9, 10, 6]
# 3 Number of largest products from the said two lists:
# [60, 54, 50]
# 4 Number of largest products from the said two lists:
# [60, 54, 50, 48]


# list1=[1, 2, 3, 4, 5, 6]
# list2=[3, 6, 8, 9, 10, 6]
# list3=[]
# for i in list1:
#        for j in list2:
#               r=i*j
#               list3.append(r)
# print(sorted(list3))              



# 189. Write a Python program to shift last element to first position and first element to last position 
# in a given list.  
# Original list:
# [1, 2, 3, 4, 5, 6, 7]
# Shift last element to first position and first element to last position of the said list:
# [7, 2, 3, 4, 5, 6, 1]
# Original list:
# ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
# Shift last element to first position and first element to last position of the said list:
# ['f', 'd', 'f', 'd', 's', 's', 'd', 's']


# list1=[1, 2, 3, 4, 5, 6, 7]

# for i in range(len(list1)):
       
#        if i==(len(list1)-1):
#               list1(len(list1))==list1[0]
#        elif i==0:
#               list1[0]=list1[len(list1)-1]          
# print(list1)                



# 188. Write a Python program to sort a given list of tuples by a specified element.  
# Original list of tuples:
# [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# Sort on 1st element of the tuple of the said list:
# [('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
# Sort on 2nd element of the tuple of the said list:
# [('item2', 10, 10.12), ('item1', 11, 24.5), ('item4', 12, 22.5), ('item3', 15, 25.1)]
# Sort on 3rd element of the tuple of the said list:
# [('item2', 10, 10.12), ('item4', 12, 22.5), ('item1', 11, 24.5), ('item3', 15, 25.1)]


# list1=[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# r=sorted(list1, key=lambda list1: list1[2])
# print(r)




# 187. Write a Python program to convert a given list of tuples to a list of strings.  
# Original list of tuples:
# [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# Convert the said list of tuples to a list of strings:
# ['red green', 'black white', 'orange pink']
# Original list of tuples:
# [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
# Convert the said list of tuples to a list of strings:
# ['Laiba Delacruz', 'Mali Stacey Drummond', 'Raja Welch', 'Saarah Stone']

# list1=[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# list2=[]
# for i in list1:
#        sum=''
#        for j in i:
#               sum=sum+j
#        list2.append(sum)       
# print(list2)              


# 186. Write a Python program to swap two sublists in a given list.  
# Original list:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Swap two sublists of the said list:
# [0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
# Swap two sublists of the said list:
# [0, 9, 3, 8, 6, 7, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]

# 185. Write a Python program to convert a given decimal number to a binary list.  
# Original Number: 8
# Decimal number ( 8 ) to binary list:
# [1, 0, 0, 0]
# Original Number: 45
# Decimal number ( 45 ) to binary list:
# [1, 0, 1, 1, 0, 1]
# Original Number: 100
# Decimal number ( 100 ) to binary list:
# [1, 1, 0, 0, 1, 0, 0]


n=8
list1=[]
while n>0:
       rem=n%2
       list1.append(rem)
       n=n//2
print(list1.reverse())       
