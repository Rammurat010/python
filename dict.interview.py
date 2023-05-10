# 80. Write a Python program to find the key of the maximum value in a dictionary. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')

# d={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# max_key='Theodore'
# for key in d:
#     if d[key]>=d[max_key]:
#        max_key=key
# print(max_key)       
       


# 79. Write a Python program to create a flat list of all the values in a flat dictionary. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the values of the said flat dictionary:
# [19, 20, 21, 20]


# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# list1=[]
# for i in d:
#     list1.append(d[i])
# print(list1)   


# 78. Write a Python program to create a flat list of all the keys in a flat dictionary. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the keys of the said flat dictionary:
# ['Theodore', 'Roxanne', 'Mathew', 'Betty'] 
    
    
# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

# list1=[]
# for i in d:
#     list1.append(i)    
# print(list1)    



# 77. Write a Python program to transform a dictionary into a list of tuples. Go to the editor
# Sample Output:
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

# d={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# list1=[]
# for i in d.items():
#     list1.append(i)
# print(list1)    



# 76. Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and 
# the elements of the second one serve as values. Each item in the first list must be unique and hashable. Go to the editor
# Sample Output:
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f']
# [1, 2, 3, 4, 5]
# Combine the values of the said two lists into a dictionary:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# d1=['a', 'b', 'c', 'd', 'e', 'f']
# d2=[1, 2, 3, 4, 5]
# d3={}
# for i in d1:
#     d3.append(i)
# for j in d2:
#     d3.append(d2[j])    
# print(d3)

#Write a Python script to sort (ascending and descending) a dictionary by value.

# d={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# r=sorted(d,key=lambda d:d[0]   )
# print(d)


# 3. Write a Python script to concatenate the following dictionaries to create a new one. Go to the editor
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d5={}
# for i in (dic1,dic2,dic3):
#     d5.update(i)
# print(d5)    



# Check whether a given key already exists in a dictionary

# n=1
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# if n in d:
#     print('yes')
# else:
#     print('no')


# Write a Python script to merge two Python dictionaries.


# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d=d1.copy()
# d.update(d2)
# print(d)



#Write a Python program to iterate over dictionaries using for loops.

# d = {'Red': 1, 'Green': 2, 'Blue': 3} 

# for key,value in d.items():
#     print(key,d[key])



#Write a Python program to sum all the items in a dictionary. 
# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# sum=0
# for kay in d:
#     sum=sum+d[kay]
# print(sum)    


#Write a Python program to map two lists into a dictionary.



# keys = ['red', 'green', 'blue']
# values = ['FF0000','008000', '0000FF']
# d=keys.copy()
# d.update(values)
# print(d)



#Write a Python program to get the maximum and minimum values of a dictionary.
# d={'x':500, 'y':5874, 'z': 560}

# x=max(d,key=lambda key: d[key])
# print(x)




#Write a Python program to remove duplicates from the dictionary.


#Write a Python program to print all distinct values in a dictionary.

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# dic={}
# for key in L.key():
#     if key not in dic:
#         dic.append(L['kay'])
# print(dic)        

#Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

# dic = {"A":12,"B":13,"C":9,"D":89,"E":34,"F":17,"G":65,"H":36,"I":25,"J":11}
# list1=[]
# for i in dic.values():
#     list1.append(i)
# print(list1)    

# sorted(list1)
# print('3rd largest values ',list1[-3])



# Write a Python program to combine values in a list of dictionaries. Go to the editor
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})


# d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# dic=

# for i in d:
#     if i not in dic:
#         dic[i]='amount'
# print(dic)        



#Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# str1='w3resource'
# dic={}
# for i in str1:
#     dic[i]=1
# dic['r'] =2
# dic['e']=2   
# print(dic)    
    
    
    
#Write a Python program to print a dictionary in table format.    
#my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}


num = {'n1': [2, 3, 1], 'n5': [5, 1, 2], 'n3': [3, 2, 4]}
num1=[]
for j in num.values():
    num1.append(j)
sorted(num1)

print(num1)
