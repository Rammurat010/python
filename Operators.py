'''
These are some operations like
'''
#Arithmetic operators
print('\n----------Arithmetic operators----------------\n')

a=5
b=2
print("Addition(+) of",a,'and',b,'=',a+b)
print("Subtraction(-) of",a,'and',b,'=',a-b)
print("Divide(/) of",a,'and',b,'=',a/b)
print("Multiplication(*) of",a,'and',b,'=',a*b)
print("Reminder(%) of",a,'and',b,'=',a%b)
print("Exponent(**) of",a,'and',b,'=',a**b)
print("Floor(//) division of",a,'and',b,'=',a//b)

#Comparison operators

print('\n----------Comparison operators----------------')

# ==,>,<,>=,<=,!=

print('These are ==,>,<,>=,<=,!=')

#Assignment Operators
print('\n----------Assignment Operators----------------')

a=5
a+=a#a=a+a
print('+= operator use:',a)# output : 10
a-=2
print('-= operator use:',a)# output : 8
a*=a
print('*= operator use:',a)# output : 64
a%=2
print('%= operator use:',a)# output : 0
a=12
a**=4
print('**= operator use:',a)# output : 144
a=5
a//=2
print('//= operator use:',a)# output : 2.0

#Logical Operators

print('\n----------Logical Operators----------------')




#logical Operatos ----> and, or, not
print(1 and False)
print(False and 1)
print(1 and 1)
print(True and True)
print(1 and True)
print(0 and True)
print(1 and True)
print(0 and 1)
print(False and True)
print(False and 1)

print('\n-----------------------\n')
print(not 1) #False
print(not 0) #True
print(not True) #False
print(not False) #True



# round() and abs() function 


# round(num1,nmu2) take two parameter num1 is the number and num2 decide decimal places of the given num1
print('----------Round of function')

print(round(10))

print(round(1,2))

print(round(12.3,1))
print(round(12.464,1))
print(round(4.5))
print(round(2.5, None))


'''

Rounding with ndigit < 0
We can also pass a negative value for the ndigit argument. 
This will start rounding from the left of the decimal point!

So, if our original number has 3 digits after the decimal
 point, passing ndigit = -3 will remove those 3 digits before the decimal point and replace then with 0, giving us 0!


'''

print(round(123.456, 0))
print(round(123.456, -1))
print(round(123.456, -2))
print(round(123.456, -3))

#abs() function  Return the absolute of a number

print(abs(11.44))

print(abs(-1))
print(abs(3+4j))




print(0.1 + 0.1+0.1==0.30)


















