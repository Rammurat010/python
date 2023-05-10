#Complex number uses-
'''
Complex number are generally used in electronic,optic and quantum theroy for describing 
wave and periodic.


Fourier transform 

Auto signal processing in ML
Speach recongination system

Complex number is numric data type
A complex number has real ans imaginary part compont

i.e a+bj

a=> a is the real part 
b=> imaginary part
'''
#Implementations
num=2+3j
print(num)#(2+3j)
num1=2-3j
print(num1)#(2-3j)

num2=-2-3j
print(num2)#(-2-3j)

num3=4j
print(num3)#(4j)

num4=-4j
print(num4)#(-0-4j)

print(type(num3))#<class 'complex'>

print('-------------accessing the real and imaginary part each by one -------------')



num5=2+3j
print(num5.real)#2.0
print(num5.imag)# 3.0

num6=-2-3j
print(num6.real)#-2.0
print(num6.imag)# -3.0

num7=-3j
print(num7.real)#-0.0
print(num7.imag)# -3.0


num8=3j
print(num8.real)#0.0
print(num8.imag)#3.0


# How to use complex function



print('--------------Use complex funtion')

'''

a=complex(real,imaginary) two argument take and argument are {int,flat,string(always take a numer)} 


default value is 0
'''

a=complex()
print(a)#0j

a=complex(1,2)
print(a)#(1+2j)

a=complex(1)
print(a)#(1+0j)

a=complex(0)
print(a)#0j

a=complex(0,-2)
print(a)#(-2j)







a=complex(0.0)
print(a)#0j

a=complex(1.2)
print(a)#(1.2+0j)




# deal with string arguemnts
a=complex('0')
print(a)#0j

a=complex('2.4')
print(a)#2.4+0j








