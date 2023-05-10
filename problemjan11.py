#1: Write a program to convert All character into small letter without usign pre-defined function.
str=input('Enter the Captail word :')
count=''
for i in str:
    if ord(i) not in range(ord('A'),ord('Z')): 
        count=count+i
    else:
        p=ord(i)+32
        count=count+chr(p)   
print(count)      
# 
# 
# Write a program to convert All character into capital letter without usign pre-defined function.   

# str=input('Enter the small word :')
# count=''
# for i in str:
#     if i not in "abcdefghijklmnopqrstuvwxyz":
#         count=count+i
#     else:
#         p=ord(i)-32
#         count=count+chr(p)   
# print(count)   











'''3: emp = [{'name': 'Amit', 'salary': '100', 'city': 'Greater Noida'}, {'name': 'Ambresh',
 'salary': '150', 'city': 'Greater Noida'},{'name': 'Aman', 'salary': '100', 'city': 'Dheradun'}]
Remarks: all questions done via loop in generic format assume that this is very large list of dict
a: Take a name and find salary
b: Calculate avg salary
c: Calculate whose max salary
d: Take a city name and list down all emp who is beloging to that city
e: List down all emp whose name start with 'Am'
'''


emp = [{'name': 'Amit', 'salary': '100', 'city': 'Greater Noida'}, {'name': 'Ambresh','salary': '150', 'city': 'Greater Noida'},
   {'name': 'Aman', 'salary': '100', 'city': 'Dheradun'}]

# name=input('Enter the name: ' )
# sumSalary=0
# for i in emp:
#     if i['name']==name:
#         z=i['name']
#         print(z)
#         r= i["salary"]
#         print(r)   
#     sumSalary=int(i['salary'])
# avgSalary=sumSalary/3
# print('Avg SALAR:',str(avgSalary))

# city=input('Enter the city name: ' )
# for i in emp:
#     if i['city']==city:
#         z=i['name']
#         print(z)


# Maximum salary 


# e: List down all emp whose name start with 'Am'

# data=[]
# for i in emp:
#     if i['name'].__contains__('Am'):
#         data.append(i['name'])
# print(data)
    

# Python3 code to iterate through all values in a dictionary
 

# statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
 
# for i in statesAndCapitals:
#     print( statesAndCapitals[i] )