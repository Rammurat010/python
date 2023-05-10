#1: take a input number and print Table of that number
# n= int(input("take a input number :" ))
# for i in range(1,11):
#      b=n*i
#      print(n,"*",i,'=',b)
     

#2: Calculate the sum of all numbers from 1 to a given number

# n= int(input("Enter a input number :" ))
# result=sum(range(1,n+1))
# print(" sum of", n, "num is ", result)


# n= int(input('enter the number'))
# sum=0
# for i in range(n):
#      sum=sum+i





#3: Count the total number of digits in a number

# ram=int(input(("Enter the nub :" )))
# pappu=len(str(ram))
# print("total number of digit is",pappu)


# num = int(input('enter the number'))
# count=0
# for i in str(num):
#     count=count + i
# print(count)    




#Print list in reverse order using a loop

# list=['pappu','sohan','mohan','rohan']
# list.reverse()
# print(list)


list=[10,2,3,4,5,6,7,8,9 ]
new_list=[]
for i in list:
    new_list.insert(-i, i)
print(new_list)    



# Reverse a given integer number

# num=int(input("Enter the number :"))
# print(str(num)[::-1])