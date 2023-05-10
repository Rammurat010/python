#Q1.

# row=1
# n=5
# i=0
# while i<=5:
#      print('*'*i)
#      i=i+1
  
  



#Q2..



# n=5
# i=5
# while i>=0:
#      print('*'*i)
#      i=i-1




#Q3..




#Q4..

# n=5
# i=4
# while i>=0:   
#      print('#'*(4-i)+'@'*(2*i+1))
#      i=i-1
 

# Q...Python program to convert lower letter to upper and upper letter to lower in a string. 

# num  = input("Enter a String :")
# x = []
# for i in range(len(num)):
#     if num[i].isupper():
#         x.append(num[i].lower())
#     elif num[i].islower():
#         x.append(num[i].upper())

# Q..


# num = input("Enter a string ").split()
# search = input("Enter a word to search ")
# if search in num:
#     print(f"{search} exist in String")
# else:
#     print(f"{search} not exist in String")


#Q...Write a python program to sort letters of word by lower to upper case format.

# strn = 'pytHOnloBBy'
# lower = []
# upper = []
# for i in range(len(strn)):
#     if strn[i].islower():
#         lower.append(strn[i])
#     else:
#         upper.append(strn[i])

# # printing result
# result = ' '.join(lower+upper)
# print(result)