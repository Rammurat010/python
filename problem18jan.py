# Q1:
#     *
#    *
#   ***
#  ***
# ***

# n=8
# for i in range(5):
#     for j in range(5):
#         if  j+i==4 or j+i==5 or j+i==6:
#          print('*' , end='')    
#         else:
#          print(end=' ')   
#     print()







#Q..2:
# 1
# 12
# 123
# 1234
# 12345
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print('')    



#Q.3

# 1
# 12
# 121
# 1221
# 12221

# n=5
# for i in range(1,5):
#     for j in range(1,i+1):
#          print(j,end='')
#     for j in range(i-1,0,-1):  
#         print(j,end='')    
#     print()


#4:
# A
# AB
# ABC
# ABCD
# ABCDE


# n=6
# r=ord('A')
# for i in range (n):
#     for j in range(i):
#         print(chr(r+j),end='')
#     print()


# for i in range (65,70):
#      for j in range(65,i+1):
#         print(chr(j),end="")
#      print()



# n=5
# i=4
# while i>=0:   
#      print('#'*(4-i)+'@'*(2*i+1))
#      i=i-1
 



# 5:
#       A
#      BAB
#     CBABC
#    DCBABCD
#   EDCBABCDE



# for i in range(1, 6):
#     print(" "*(5-i), end="")
#     for j in range(i):
#         print(chr(64+i-j), end="")
#     for j in range(i-1):
#         print(chr(64+i-j-1), end="")
#     print()




