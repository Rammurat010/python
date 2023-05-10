# 1: Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# count_letters=0
# count_digit=0
# def calculate_num_letters(n):
#      global count_letters
#      global count_digit
#      for i in n:
#         if ord(i) in range(97,123):
#              count_letters=count_letters+1
#              print(count_letters)
#         elif ord(i) in range (48,58): 
#              count_digit=count_digit+1
#              print( count_digit )


# n=input('Enter the sentence :')
# calculate_num_letters(n)




# 2: Write a program that computes the net amount of a bank account based a transaction log from 
# console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500


# def net_amount(list1):
#     total1=0
#     total2=0
#     for i in list1:
#         if i=='D300' or i== 'D100':
#             total1+=int(i[1:])
#         elif i=='W200':
#             total2+=int(i[1:])
#     return (total1-total2)


n=input('Enter the amount :')

list1=n.split(' ') 
print(list1)      
# print(net_amount(list1))





# 3: You are required to write a program to sort the (name, age, height) tuples by ascending order
# where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'),
#  ('Tom', '19', '80')]


# def sorting(tuple_list):
#     Sort_based_on_name=sorted(tuple_list, key=lambda a: a[0]) 
#     sort_based_on_age =sorted(tuple_list, key=lambda b: b[1]) 
#     sort_by_score     =sorted(tuple_list, key=lambda b: b[2])
    
#     print(Sort_based_on_name)
#     print(sort_based_on_age)
#     print(sort_by_score)

# tuple_list=[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'),('Tom', '19', '80')]
# sorting(tuple_list)























 