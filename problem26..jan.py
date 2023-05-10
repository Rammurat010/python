#1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#  between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.


# for i in range(2000,3000,1):
#     if i%7==0 and i%5!=0:
#      print(i,',',end='') 



#2: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the 
# dictionary.Suppose the following input is supplied to the program: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# def generate_dictionary(n):
#  d={}
#  for i in range(1,n+1):
#    d[i]=i*i
#  return d
# print(generate_dictionary(8)) 



# 3: Write a program which accepts a sequence of comma-separated numbers from console and 
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# num='34,67,55,33,12,98'
# list1=num.split(',')
# print(list1)
# tuple=tuple(list1)
# print(tuple)





# 4: Write a program that accepts a comma separated sequence of words as input and prints the words in 
# a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


# def sorting1( words):
#   words=sorted(words)
#   return words
# words=('without','hello','bag','world')
# print(sorting1(('without','hello','bag','world')) )  




#1: WPA to convert Snake case into Camel case. eg. Input: this_is_program => Output: ThisIsProgram

# def small_to_capital_convert(c):
#     cap_c = ord(c)-32
#     return chr(cap_c)

# def snake_to_camel(str_1):
#     # amit_kumar_tiwari
#     new_str = ''
#     next_capital_char = False
#     for i in str_1:
#         if next_capital_char:
#             new_i = small_to_capital_convert(i)
#         else:
#             new_i = i
#         if i == '_':
#             next_capital_char = True
#         else:
#             next_capital_char = False
#             new_str += new_i


# for i in range(7):
#     k=65
#     for j in range(5-i):
#         print(' ',end='')
#     for m in range(1+i):
#         print(chr(k),end='')
#         k=k+1
#     print() 
# print(chr(65))           

            
            
#     return new_str
# print(snake_to_camel('amit_kumar_tiwari'))
# def camel_to_snake(str_1):
#     new_str = ''
#     for i in str_1:
#         pass
#     return new_str
#2: WPA to convert Camel Case into snake case. eg. Input: ThisIsProgram => Output: this_is_program

# str1='ThisIsProgram'
# str2=''
# for i  in str1:
#    if  i.isupper():
#      str2=str2 +'_'+i.lower()
#    else:
#     str2=str2+i
# print(str2[1:])



str1= "fibnocci series "
print(str1.find('o'))


# a=0
# b=1
# c=0
# print(a)
# for i in range(1,9):
#     a=b
#     b=c
#     c=a+b
#     print(c)  


