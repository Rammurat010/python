'''
2: Find the output with reasons
True and False
2 and False
False and 4
'A' or 'a'
'True' or False
False or 0


'''
# ()
# print(True and False)#False
# print(2 and False)#False
# print(False or 4)#4
# print(False and 4)#False
# print('A' or 'a')#A
# print('True' or False)#True
# print(False or 0)#0




#Example 1: Access both key and value using items()
# dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
# for keys,values in dt.items():
#     print(keys,values)


# Access both key and value without using items()
# dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
# for key in dt:
#     print(key,dt[key])

#Access both key and value using iteritems()    
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
for key,value in dt:
    print(key,value)

