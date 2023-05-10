#wap to find given num is prime or not
def is_prime_nub(n):
    count=0
    for i in range(2,n+1):
        if n%i==0:
          count=count+1  
    if count==1:
        return True
    else:
        return False
          

# n=int(input('Enter the number :'))
# print(is_prime_nub(n))

#wap to print given number is order prime list



def prime_list(n):
    list2=[]
    for i in range(1,n+1):
      isPrime= is_prime_nub(i)
      if(isPrime):
          list2.append(i)          
    return list2    


n=int(input('Enter the number :'))
print(prime_list(n)) 


#wap to find given num is even

# def is_even_num(n):
#     if n%2==0:
#      return True 
#     else:
#      return False      
 
# n=int(input('Enter the number :'))
# print(is_even_num(n))



#wap to find given num is odd


# def is_odd_num(n):
#     if n%2!=0:
#      return True 
#     else:
#      return False      
 
# n=int(input('Enter the number :'))
# print(is_odd_num(n))



#wap to print given number by the user and print all even list

# def even_number(list1):
#     list2=[]
#     for i in list1:
#      if (int(i))%2==0:
#         list2.append(i)
#     return list2    
    
 
# n=input('Enter the number :')
# list1=n.split(',')
# print(list1)
# print(even_number(list1))


#wap to print given number by the user and print all odd list


# def odd_number(list1):
#     list2=[]
#     for i in list1:
#      if (int(i))%2!=0:
#         list2.append(i)
#     return list2    
    
 
# n=input('Enter the number :')
# list1=n.split(',')
# print(list1)
# print(odd_number(list1))



