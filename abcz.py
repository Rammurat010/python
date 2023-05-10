
# 2: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 
# are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010


''''

     


 

    
    
    
# user input and split by comma and check divisible_by_5 append in new list
def checkDivisiblity():
    divisible_by_5=[]
    userInput = input("Enter a binary value with comma separted : ")
    numList=userInput.split(",")
    for bn in numList:
        dn=binToDec(int(bn))
        if dn%5==0:
            divisible_by_5.append(dn)
        else:
         pass
    return divisible_by_5

# convert decimal list which divible by 5 
def convertDecimalListToBinaryList(numList):
    empList=[]
    for i in numList:
        empList.append(decimalToBinary(i))
    return empList
    
    


#divisiblityNumList=checkDivisiblity()

print(convertDecimalListToBinaryList(checkDivisiblity()))



'''

list1=[4,4,7,8]
list1[0]=5
print(list1)






# power function

def power(a,b): 
     res = 1 
     for i in range(b): 
         res =res* a 
     return res 

# convert binaryToDecimal like 101=>5
def binToDec(bin_value):
    decimal_value = 0
    count = 0
    while(bin_value != 0):
        digit = bin_value % 10
        decimal_value = decimal_value + digit * power(2, count)
        bin_value = bin_value//10
        count =count+ 1
    return decimal_value


# convert DecimalToBinay like 5=>101
s=''
def decimalToBinary(num):
    global s
    if num>1:
        decimalToBinary(num//2)
    s=s+str(num%2)
    return s


def decimalListToBinaryList(decimalList):
    binaryList=[]
    for i in decimalList:
        c=decimalToBinary(i)
        binaryList.append(c)
    return binaryList





userInput=input('Enter a numner with comma separted : ')#0100,0011,1010,1001
strList=userInput.split(',')#['0100','0011','1010','1001']
divisible_by_5=[]
for str1 in strList:
    n=binToDec(int(str1))
    if n%5==0:
        divisible_by_5.append(n)
    else:
        pass
  # finally 5 diviable divisible_by_5= [10]  
    
l=decimalListToBinaryList(divisible_by_5)
print(l)       
    



        
        
        
        
        

    

























      
    









