# 1: Take a blank list X= [], Perform all these actions:
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


# list= []
# list.insert(0,5)
# list.insert(1,10)
# list.insert(0,6)
# print(list)   #[6, 5, 10]
# list.remove(6)
# print(list)
# list.append(9)
# list.append(1)   #[5, 10, 9, 1]
# list.sort()
# print(list)   #[1, 5, 9, 10]
# list.pop()    #[1, 5, 9]
# list.reverse()
# print(list)  #[9, 5, 1] 


#2: Calculate avg and percentage of a student marks, You will get input in a 
# string format like this (Input: 'Malika 52 56 60'), 
# You need to calculate the avg and percentage of marks.

# a=int(input("Enter the first subject mark  :"))
# b=int(input("Enter the second subject mark :"))
# c=int(input("Enter the third subject mark  :"))
# r=  (a+b+c)
# avg = r/3
# percentage =(r/300)*100
# print("avg  : ",avg)
# print("percentage  : ", percentage)

# a=input("Enter the first name and mark1 mark2 mark3 : ")
# list=a.split()
# #avg
# numberString=list[1:]
# sumOfNumbers=int(numberString[0])+int(numberString[1])+int(numberString[2]);
# avg=(sumOfNumbers)/3
# print('Average : ',avg)
# # percentage 
# percentage=(sumOfNumbers/300)*100
# print('Percentage : ',percentage)

dataString=input("Enter the first name and mark1 mark2 mark3 : ")
dataString=dataString.split()
print(dataString)
a=  dataString[1:]
print(type(dataString))
print(a)




