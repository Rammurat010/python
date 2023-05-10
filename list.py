

'''

1->cmp(list1, list2) =>compare to list is equal or not
2->len(list)=>Find the length of the list
3->clear(): Removes all the elements from the list.
4->copy():  Returns a duplicate of the list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

5->index(): Returns the first appearance of a particular value.

In the below example, let’s examine the index of February within the list of months.

months = ['January', 'February', 'March', 'April', 'May'] 
months.index('March')=2



6->count() function
The count() method returns the number of elements with the desired value.
fruits = ['cherry', 'apple', 'cherry', 'banana', 'cherry']
x = fruits.count("cherry")=3




'''





# #List
# sub=['Math','Comp','Science']
# print(sub)
# print(type(sub))
# print(sub[0])
# print(sub[-1])
# print(sub[0:2])
# print(sub[:12])

# #fucntions
# sub.append('Geo')
# print(sub)
# sub.insert(1,"Phys")
# print(sub)

# sub1=['Chem','Accounts']
# #sub.insert(0,sub1)#[['Chem', 'Accounts'], 'Math', 'Phys', 'Comp', 'Science', 'Geo']
# #sub.extend(sub1)#['Math', 'Phys', 'Comp', 'Science', 'Geo', 'Chem', 'Accounts']

# sub3=sub1+sub#['Chem', 'Accounts', 'Math', 'Phys', 'Comp', 'Science', 'Geo']
# print(sub3)
# print('\n------------------------------\n')


#Write a Python program to insert an element before each element of a list.

# list1=[1,2,3,4,5]
# l=len(list1)
# for i in range(0,l+1,2):
#    list1[i]='c'
# print(list1)


#Write a Python program to print nested lists (each list on a new line) using the print() function. 


# 49. Write a Python program to convert a list to a list of dictionaries. Go to the editor
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
#                   {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# lists1= ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# lists2=[]
# dict={}
# for i in lists1:
#     for j in i:
#      lists2.append(j)  
# dict['color_name']=      
# print(dict)        


#  Write a Python program to split a list every Nth element. Go to the editor
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

#  Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


#  Write a Python program to combine values in a list of dictionaries. Go to the editor
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})


# list1 =[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# list1=[]
# for i in list1:
#     for j in i:
        
 
 
# a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
# cp={}
# val=0
# for d in a:
#     if d['item'] not in cp:
#         cp[d['item']] = d['amount']
        
#     else:
#         cp[d['item']] += d['amount'] 
# print(cp)     
    

#Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# str1='w3resource'
# dict1={}
# for i in str1:
#     if i=='r' or i=='e':
#      dict1[i]=2
#     else:
#          dict1[i]=1 
# print(dict1)    
    
#Write a Python program to remove spaces from dictionary keys. 

# Write a Python program to print a dictionary line by line.

#Write a Python program to count the number of items in a dictionary value that is a list.

# dic={'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# count=0
# for i in dic:
#     if i in dic:
#         count=count+1
# print(count)        

#Write a Python program to sort Counter by value. Go to the editor
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

# dic={'Math':81, 'Physics':83, 'Chemistry':87}
# print((sorted(dic.values())))


# Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})


# list1= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'] 
# list2=[1, 2, 2, 3]
# dic={}
# for i in list1:
#     for j in list2:
#         dic[i]={j}
#         list2.remove(j)
#         break     
# print(dic)

# Write a Python program to match key values in two dictionaries. Go to the editor
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

# dic={'key1': 1, 'key2': 3, 'key3': 2}
# dic2={'key1': 1, 'key2': 2}
# for i in dic:
#     for j in dic2:
#         if dic[i]==dic2[j]:
#             y=('yes')
#         else:
#             y='no'
# print(y)            
    
    
    
# list1=[4,55,67,87,45,54,56]
# n=3
# max_value=list1[0]
# for j in range(n):
#     max_value=list1[0]
#     for i in list1:
#       if i>=max_value:
#         max_value=i
#     else:  
#         list1.remove(max_value) 
# print(max_value) 

# Write a Python program to create a dictionary of keys x, y, and z where each key has 
# as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from 
# the dictionary. Go to the editor
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]   
       
# dic={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#  'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

# for key,value in dic.items():
#     print(value[4:5])
       
        
#Write a Python program to drop empty items from a given dictionary. Go to the editor
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}        

# dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
# dict1={}
# for key,value in dic.items():
#     if value!=None:
#         dict1[key]=value
# print(dict1)        

# Write a Python program to filter a dictionary based on values. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
        
# dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}   

#Write a Python program to create a list with infinite elements.


# list1=[]
# i=1
# while i>=0:
#     list1.append(i)
#     i=i+1
# print(list1)    


#Write a Python program to concatenate elements of a list
    
    
# list1=[3,4,5,65,6,] 
# sum=0   
# for i in list1:
#     sum=sum+i
# print(sum)    


#Write a Python program to remove key-value pairs from a list of dictionaries.



# 203. Write a Python program to join adjacent members of a given list.  
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']



# 202. Write a Python program to find the indexes of all None items in a given list.  
# Original list:
# [1, None, 5, 4, None, 0, None, None]
# Indexes of all None items of the list:
# [1, 4, 6, 7]


# list1=[1, None, 5, 4, None, 0, None, None]
# list2=[]
# for i in range(len(list1)):
#     if list1[i]==None:
#         list2.append(i)
# print(list2)        
    
# 200. Write a Python program to pair consecutive elements of a given list.  
# Original lists:
# [1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# Original lists:
# [1, 2, 3, 4, 5]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5]]
# Click me to see the sample solution


# list1=[1, 2, 3, 4, 5, 6]
# list2=[]
# for i in range(len(list1)-1):
#     print(i)
#     r=[list1[i],list1[i+1]]
#     list2.append(r)
# print(list2)  


# 199. Write a Python program to convert a Unicode list to a list of strings.  
# Original lists:
# ['S001', 'S002', 'S003', 'S004']
# Convert the said unicode list to a list contains strings:
# ['S001', 'S002', 'S003', 'S004']  


# 198. Write a Python program to compare two given lists and find the indices of the values present in both lists.  
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [7, 8, 5, 2, 10, 12]
# Compare said two lists and get the indices of the values present in both lists:
# [1, 4]
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [7, 8, 5, 7, 10, 12]
# Compare said two lists and get the indices of the values present in both lists:
# [4]
# Original lists:
# [1, 2, 3, 4, 15, 6]
# [7, 8, 5, 7, 10, 12]
# Compare said two lists and get the indices of the values present in both lists:
# []



# list1= [1, 2, 3, 4, 5, 6]
# list2= [7, 8, 5, 2, 10, 12]
# list3=[]

# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i]==list2[j]:
#             list3.append(i)
# print(list3)            


# 197. Write a Python program to compute the average of the n-th element in a given list of lists with different lengths.  
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]



# 196. Write a Python program to move a specified element in a given list.  
# Original list:
# ['red', 'green', 'white', 'black', 'orange']
# Move white at the end of the said list:
# ['red', 'green', 'black', 'orange', 'white']
# Original list:
# ['red', 'green', 'white', 'black', 'orange']
# Move red at the end of the said list:
# ['green', 'white', 'black', 'orange', 'red']
# Original list:
# ['red', 'green', 'white', 'black', 'orange']
# Move black at the end of the said list:
# ['red', 'green', 'white', 'orange', 'black']
# n='green'



# list1=['red', 'green', 'white', 'black', 'orange']
# list2=[]

# for i in list1:
#     if i==n:
#         pass
#     else:
#         list2.append(i)
# print(list2)  




# 195. Write a Python program to traverse a given list in reverse order, and print the elements 
# with the original index.  
# Original list:
# ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red
# Traverse the said list in reverse order with original index:
# 3 black
# 2 white
# 1 green
# 0 red      



# 194. Write a Python program to sum two or more lists. The lengths of the lists may be different.  
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
# [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]


# list1=[[1, 2, 4], [2, 4, 4], [1, 2]]
# list2=[]

# for i in list1:
#     sum=0
#     for j in i:
#         sum=sum+j
#     list2.append(sum) 
# print(list2)       


# 192. Write a Python program to remove all strings from a given list of tuples.  
# Original list:
# [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# Remove all strings from the said list of tuples:
# [(100,), (80,), (90,), (88, 89), (90, 92)]


list1=[(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
list2=[]
for i in list1:
    for j in i:
        if type(j)==str:
            pass
        else:
            list2.append(j)
print(list2)            