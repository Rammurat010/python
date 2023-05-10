'''
The operator module exports a set of efficient functions 
corresponding to the intrinsic operators of Python.
For example, operator.add(x, y) is equivalent to the expression x+y

Syntex:

operator.add(a,b)=> retrun the sum of a and b
operator.sub(a,b)=> retrun the subtraction of a and b
operator.mul(a,b)=> retrun the multiplication of a and b
operator.truediv(a,b)=> retrun the division of a and b
operator.mod(a,b)=> retrun the modules of a and b
operator.pow(a,b)=> retrun the power of a and b
operator.floordiv(a,b)=> retrun the floor division of a and b



'''

import operator
a =int(input("Enter the first value : "))
b =int(input("Enter the second value : "))
print('Addition of',a,'+',b,'=',operator.add(a,b))
print('Subtraction of',a,'-',b,'=',operator.sub(a,b))
print('Multiplication of',a,'*',b,'=',operator.mul(a,b))
print('Division of',a,'/',b,'=',operator.truediv(a,b))
print('Modulus of',a,'%',b,'=',operator.mod(a,b))
print('Power of',a,'**',b,'=',operator.pow(a,b))
print('floor division of',a,'\\',b,'=',operator.floordiv(a,b))
print('Addition of',a,'+',b,'=',operator.add(a,b))