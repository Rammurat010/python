#1: Take 2 int values from user and print greatest among them


a=int(input("First input value :" ))
b =int(input("Second input value :" ))
if a>b:
    print("value a is greatest :" )
elif a==b:
    print("a & b is same :" )     
else : 
    print("value b is greatest" ) 
    
    
    

#2: Take values of length and breadth of a rectangle from user and check if it is square or not.

'''
a=int(input("Take values of length  :" ))
b =int(input("Take values of breadth :" ))
if a==b:
 print("rectangle is square :" )   
else:
 print("rectangle is not square :" )

 '''


#3: Take input of age of 3 people by user and determine oldest and youngest among them.

'''

a=int(input("Take input of age of first person  :" ))
b=int(input("Take input of age of second person :" ))
c=int(input("Take input of age of third person  :" ))
if a>b and b>c:
    print(" a is oldest  \n c is youngest " )
elif a>c and c>b:
    print(" a is oldest  \n b is youngest " )
elif b>c and c>a:  
    print(" b is oldest  \n a is youngest " ) 
elif b>a and a>c:
    print(" b is oldest  \n c is youngest " )  
elif c>a and a>b: 
    print(" c is oldest  \n b is youngest " )
elif c>b and b>a:
    print(" c is oldest   \n a is youngest " )
else a=b and b=c:
    print("same age") 
    '''
    