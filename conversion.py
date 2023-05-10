# decimal to binary 

'''
Python bin() Function
The python bin() function is used to return the binary representation of a specified integer.
A result always starts with the prefix 0b.

Signature
bin(n)
Parameters
n - An integer

'''



print('\n---------decimal to binary -------------\n')

#Python bin() Function Example 1


def decimalToBinary(n):
    return bin(n).replace("0b","")

print(decimalToBinary(5))


'''

#Python bin() Function Example 2 with out using bin()

n=int(input('Enter a number:'))
l=list()
while n!=0:
    rem=n%2
    l.append(rem)
    n=n//2

    print(l)

'''


# binary to decimal
print('\n---------binary to decimal-------------\n')
a='0b010'
# Base 2(binary)
print(int(a, 2)) #Base 2(binary)


