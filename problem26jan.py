#1: Write a program to remove characters from a string starting from zero up to n and return a new string.

# def remove(str1,n):
#  str2=str1[n:]
#  return (str2)
# print(remove('rammurat',3)) 



#Write a program to accept a string from the user and display characters 
# that are present at an even index number.


# def display_characters(str1):
#  str1='rammurat'
#  str2=''
#  for i in range(len(str1)):
#       if i%2==0:
#        str2=str2+str1[i]
#  return str2  
# print(display_characters('rammurat'))    



#Write a program to check if the given number is a palindrome number.


def palindrome(n):
    n=121
    p= n
    rev = 0
    while p> 0:
      R= p % 10
      rev= (rev * 10) + R
      p= p// 10
    if p== rev:
     return True
    else:  
     return False
print(palindrome(121))          


#4: Given a two list of numbers, write a program to create a new list such that the new list 
# should contain odd numbers from the first list and even numbers from the second list.


# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# def new_list(list1,list2):
#  list3=[]    
#  for i in list1:
#     if i%2!=0:
#       list3.append(i)  
#  for j in list2:
#     if j%2==0:
#       list3.append(j)    
#  return list3
# print(new_list(list1,list2)) 




for i in range(1,6):
  print(' '*(6-i)+'*'*i)