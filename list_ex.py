# Write a Python program to insert an element at a specified position into a given list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]

# list=[1, 1, 2, 3, 4, 4, 5, 1]
# n=2
# list.insert(n,12)
# print(list)

# Write a Python program to extract a given number of randomly selected elements from a given list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]

# list1=[1, 1, 2, 3, 4, 4, 5, 1]
# for i in range(2):
#     n=int(input('enter the number :'))
#     for k in list1:
#         if n in list1:
#             print(n)
#             break
#         else:
#             print('not found')
#             break
        
# Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.
# Go to the editor
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 
# distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]    

# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# list2=[]
# for i in list1:
#     list2.append([1,i])
# print(list2)    

#  Write a Python program to round every number in a given list of numbers and print the total 
#  sum multiplied by the length of the list. Go to the editor
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result:
# 243

# list1= [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# sum=0
# for i in list1:
#     sum=sum+i*len(list1)
# print(sum)    


# Write a Python program to round the numbers in a given list, print the minimum and maximum numbers and
# multiply the numbers by 5. Print the unique numbers in ascending order separated by space. Go to the editor
# Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110

# list1 = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# for i in list1:
#     min_value=int(list1[0])
#     if i<min_value:
#         min_value=int(i)
# print(min_value)        

# Write a Python program to create a multidimensional list (lists of lists) with zeros. Go to the editor
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

# list1=[]
# for i in range(2):
#     list1.append([0,0])
# print(list1)    

# . Write a Python program to create a 3X3 grid with numbers. Go to the editor
# 3X3 grid with numbers:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# list1=[]
# for i in range(3):
#     list1.append([])
#     for j in range(1,4):
#         list1[i].append(j)
# print(list1)        

#  Write a Python program to read a matrix from the console and print the sum for each column. As input from the user, 
#  accept matrix rows, columns, and elements separated by a space (each row). Go to the editor
# Input rows: 2
# Input columns: 2
# Input number of elements in a row (1, 2, 3):
# 1 2
# 3 4
# sum for each column:
# 4 6



#  Write a Python program to Zip two given lists of lists. Go to the editor
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
# list1=[[1, 3], [5, 7], [9, 11]]
# list2=[[2, 4], [6, 8], [10, 12, 14]]
# list3=[]
# for i in range(len(list2)):
#     list3.append(list1[i]+list2[i])
# print(list3)  



# Write a Python program to count the number of lists in a given list of lists. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Number of lists in said list of lists:
# 4
# Original list:
# [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# Number of lists in said list of lists:  

# list1=[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# count=0
# for i in list1:
#     count=count+1
# print(count)    

# Write a Python program to find a list with maximum and minimum lengths. Go to the editor
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (3, [3, 5, 7])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (4, [1, 34, 5, 7])
# List with minimum length of lists:
# (1, [12])

# list1=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# min_length=len(list1[0])
# for i in range(len(list1)):
#     if i <min_length:
#         min_length=len(list1[i])
# print(min_length)        

# Write a Python program to check if a nested list is a subset of another nested list. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# [[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# False


# list1=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# list2=[[1, 3], [13, 15, 17]]
# count=0
# for i in list1:
#     for j in list2:
#         if j == i:
#             print(j)
#             count=count+1
#             print(count)
# if count==len(list2):
#     print('True')
# else:
#     print('false')            


#  Write a Python program to count the number of sublists that contain a particular element. Go to the editor
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# Original list:
# [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# Count 'A' in the said list:

# 3
# Count 'E' in the said list:
# 1
# count=0
# list1=[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# for i in list1:
#     for j in i:
#         if j=='E':
#             count=count+1
# print(count)            


# . Write a Python program to count the number of unique sublists within a given list. Go to the editor
# Original list:
# [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# Number of unique lists of the said list:
# {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# Original list:
# [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# Number of unique lists of the said list:
# {('green', 'orange'): 2, ('black',): 1, ('white',): 1}

# Write a Python program to sort each sublist of strings in a given list of lists. Go to the editor
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]


# list1=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# l=sorted(list1,key=lambda list1:list1[0])
# print(l)

# Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
# Go to the editor
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contains an element outside the given range:
# [[13, 14, 15, 17]]

# Write a Python program to find the maximum and minimum values in a given heterogeneous list. Go to the editor
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximum and Minimum values in the said list:
# (5, 2)

# list1=['Python', 3, 2, 4, 5, 'version']
# for i in list1:
#     if type(i)==int:
#         min_val=i
#         if i>min_val:
#             min_val=i
# print(min_val)            
    
# Write a Python program to extract common index elements from more than one given list. Go to the editor
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]

# list1=[1, 1, 3, 4, 5, 6, 7]
# list2=[0, 1, 2, 3, 4, 5, 7]
# list3=[0, 1, 2, 3, 4, 5, 7]

# for i in list1:
#     for j in list2:
#         for k in list3:
#             if i==j==k:
#                 print(j)


#  Write a Python program to convert a given list of lists to a dictionary. Go to the editor
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

# list1=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# dic={}
# for i in list1:
#     print(i)
#     for j in i:
#         print(j)
#         dic[i[:1]]=[i[1:]]
# print(dic)        


# Write a Python program that creates key-value list pairings within a dictionary. Go to the editor
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

dic1={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
dic2=[{}]
for i in dic1:
    print(i)
    dic2[i]=i
print(dic2)    