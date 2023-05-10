'''
Python, isinstance() function returns True if the object is specified types,
 and it will not match then return False. 

Syntex:
isinstance(obj,class)
Parameters : 

obj : The object that need to be checked as a part of class or not.
class : class/type/tuple of class or type, against which object is needed to be checked.
Returns : True, if object belongs to the given class/type if single class is passed or
 any of the class/type if tuple of class/type is passed, else returns False. Raises

TypeError: if anything other than mentioned valid class type. 
'''
 #Check if 80 is an isinstance of class int
number = 80
print(isinstance(number, int))