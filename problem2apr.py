#1:WPA that accepts a sequence of whitespace separated words as input and prints the words after 
# removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world





# def remove_duplicate(n):
#     str=""
#     list1=n.split(" ")
#     n = len(list1)
#     for i in range(n):
#         for j in range(0, n-1):# i=0 j=0 [babita rani archan tanya] ,j=1 [babita  archan rani tanya],j=2 [babita  archan rani tanya]
#             temp=0# i=1 j=0  [archan babita rani tanya],j=1 [archan babita rani tanya],j=2 [archan babita rani tanya]
#             # i=2 j=0 [archan babita rani tanya] j=1 [archan babita rani tanya],j=2 [archan babita rani tanya]
#             if list1[j] > list1[j+1]:
#                 temp=list1[j]
#                 list1[j]=list1[j+1]
#                 list1[j+1]=temp
#     for i in list1:
#         if i not in str:
#             str=str+" "+i
#     print(str)
# a=input("ENTER A STRING :")
# remove_duplicate(a)     



# 2: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 
# are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

def remove_duplicate(n):
    str=""
    list1=n.split(" ")
    n = len(list1)
    for i in range(n):
        for j in range(0, n-1):
            if list1[j] > list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    for i in list1:
        if i not in str:
            str=str+" "+i
    print(str)
a=input("ENTER A STRING :")
remove_duplicate(a)    


        
        

    

























      
    









