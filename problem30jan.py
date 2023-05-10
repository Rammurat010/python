#1: WPA lambda function which gives the area of triangle using LAMBDA.
# area_of_trinangle=lambda a,b: .5*a*b
# a=float(input('Enter the base length :'))
# b=float(input('Enter the height length :'))
# print(area_of_trinangle(a,b))


# 2: WPA to sort a list of tuples based on the second element of each tuple using LAMBDA:
# eg. [(1, 'Amit'), (3, 'Alkesh'), (4,'Rammurat'), (2, 'Ambresh')]

# listTuples = [(1, 'Amit'), (3, 'Alkesh'), (4,'Rammurat'), (2, 'Ambresh')]
# sortedList = sorted(listTuples, key=lambda x: x[1])
# print(sortedList)


# list_of_tuples= lambda list1 : sorted(list1)
# list1=[(1, 'zebra'),(4,'Rammurat'), (3, 'Alkesh'),  (2, 'pink')]
# print(list_of_tuples(list1))

#3: WPA to find the largest number in a list using Recurssion. [1,10,15,9,6,2,1,2,2]

# def largestNumner(numbers):
#     if len(numbers) == 1:
#         return numbers[0]
#     else:
#         return max(numbers[0], largestNumner(numbers[1:]))
    
# numList = [1, 10, 15, 9, 6, 2, 1, 2, 2]
# largest = largestNumner(numList)
# print(largest)




# def  largest(numbers):
#     if len(numbers)==1:
#         return  numbers[0]
#     else:
#      return max(numbers[0], largest(numbers[1:]))  
    
# list1=[-10,9,6,2,1,2,2,1]
# print(largest(list1))


# a={'name':'ram',
#  'from':'gkp', 
#   'mark':[2,3,4]}
# print(a.items())
# print(a.keys())
# print(a.values())


# d = {
#   'name' : 'Rahul',
#   'age' : 25,
#   'other' : 'Other Things'
# }
# print('Before delete :', d)

# #delete other.
# del d['other']
# print('After delete :', d)