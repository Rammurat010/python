
# class House:
#   def __init__(self, owner, length, width, address, no_of_floors):
#     self.owner = owner
#     self.address = address
#     self.no_of_floors = no_of_floors
#     self.area = length * width
#     self.l=length
#   def does_house_require_stairs(self):
#     if self.no_of_floors > 1:
#       return True
#     return False

#   def set_no_of_floors(self):
#     self.no_of_floors = 1


# ambresh_house = House(owner="Ambresh",
#                       address="13/106 Indira Nagar",
#                       width=120,
#                       length=100,
#                       no_of_floors=6)
# Rammurat_house = House(owner="Rammurat",
#                        width=120,
#                        address="13/110 Indira Nagar",
#                        length=110,
#                        no_of_floors=1222)

# alkesh_house=House(owner='alkesh',
#                        width=120,
#                        address="13/110 Indira Nagar",
#                        length=110,
#                        no_of_floors=1222)

# #print(ambresh_house.no_of_floors)
# ambresh_house.set_no_of_floors()
# print(ambresh_house.no_of_floors)
# print(Rammurat_house.no_of_floors)
# print(alkesh_house.l)

# a={'name':'murat','place':'noida'}
# print(a['place'])



# class Car:
#   #properties/state/data members
#   def __init__(self, make, m, speed,madeInCountry,cost,fuel,distance,dimension):
#     #declare class properties in this function
#     self.make = make
#     self.model = m
#     self.speed = speed
#     self.madeInCountry=madeInCountry
#     self.cost=cost
#     self.distance=distance
#     self.fuel=fuel
#     self.dimension=dimension
    
    
#     # self.type = None
#   def car_mileage(self):
#       return  self.distance/self.fuel,'km''/''h'  

#   def drive(self):
#     return (f"Driving {self.make} {self.model} at {self.speed} km/h")
  
#   def area(self):
#     return self.dimension['length']*self.dimension['width']

    
# nano=Car(make="made by tata",
#          model='10_january_2008',
#          speed=105,
#          madeInCountry='India',
#          cost='2.5lakh',
#          fuel=26,
#          distance=450,
#          dimension={'length':20,'width':30})         
# print(nano.drive())
# print(nano.car_mileage())
# print(nano.dimension)
# print(nano.area())
# print(nano.model)







#Create a class Employee with attributes name, age, and salary. 
# Create another class Manager that inherits from Employee and adds an attribute department.
# Create another class Administrator who has name, age, salary, type (CEO, COO, CTO, CFO).
# You will be judged on the use of inheritance here 



# class Employee:
#   def __init__(self,name, age, salary):
#     self.name=name
#     self.age=age
#     self.salary=salary
#   def get_yearly_salary(self): 
#     return ' yearly salary', self.salary*12
  
    
# class Manager(Employee):
#    def __init__(self, name, age, salary,attribute_department):
#      super().__init__(name, age, salary) 
#      self.attribute_department=attribute_department
#    def get_yearly_salary(self): 
#      return 'Manager yearly salary', self.salary*12  
   
   
# class Administrator(Manager):
#    def __init__(self, name, age, salary,attribute_department,type):
#     super().__init__(name, age, salary,attribute_department)
#     self.type=type
#    def get_yearly_salary(self): 
#      return 'Administrator yearly salary', self.salary*12
    
# sohan=Manager(name='murat',
#                 age=25,
#                 salary=4,
#                 attribute_department='assi')    
 
# pappu=Administrator(name='murat',
#                 age=25,
#                 salary=5,
#                 attribute_department='assi',
#                 type= 'CEO')
  
# print(sohan.salary)  
# print(sohan.get_yearly_salary())
# print(pappu.get_yearly_salary())
  
    
     
# Access the file inheritance_1, currently the file has two classes Animal and
#    Dog(this inherits from Animal). 
# Create classes Cat, Mouse, Hen, Peacock, Whale.(use your judgement whether they should 
#      inherit from animal or not)

# All these classes should also have the following properties/state/behaviors (you will 
#     be judged on the use of inheritance here.)
# 1. Type (Bird/Four-legged-animal/Fish etc)
# 2. Mammal or not (should be a boolean)
# Note: You can do a lot of things to this code, use your imagination and what you learn 
# in class to add to the code




# class Animal:
#   def __init__(self,name):
#     self.name=name
    
    
# class Dog(Animal):
#   def __init__(self,name):
#     super(). __init__(name)
#   def dog1(self):
#     return 'It have 4 legs'
#   def Mammal(self):
#     return True
    
# class Cat(Animal):  
#   def __init__(self,name):
#     super(). __init__(name)
#   def cat1(self):
#     return 'It have 4 legs' 
#   def Mammal(self):
#     return True
    
# class Mouse(Animal):  
#   def __init__(self,name):
#     super(). __init__(name)
#   def mouse1(self):
#     return 'It have 4 legs' 
#   def Mammal(self):
#     return False
    
# class Hen(Animal):  
#   def __init__(self,name):
#     super(). __init__(name)
#   def hen1(self):
#     return 'It have 2 legs' 
#   def Mammal(self):
#     return False
    
# class Peacock(Animal):  
#   def __init__(self,name):
#     super(). __init__(name)
#   def peacock1(self):
#     return 'It have 2 legs'
#   def Mammal(self):
#     return False
     
# class Whale(Animal):  
#   def __init__(self,name):
#     super(). __init__(name)
#   def whale1(self):
#     return 'It is a fish'
#   def Mammal(self):
#     return False
    
# Dog_subject=Dog(name='rohan1')    
# Cat=Cat(name='rohan2')  
# Mouse=Mouse(name='rohan3')  
# Hen=Hen(name='rohan4')  
# Peacock_subject=Peacock(name='rohan5')  
# Whale_subject=Whale(name='rohan6')  


# print(Dog_subject.name)   
# print(Dog_subject.dog1()) 
# print(Dog_subject.Mammal())                
       
  



#Create a class Fruit with an attribute color and a method info that returns a string.
# Create another class Apple that inherits from Fruit and adds an attribute variety.
# Override the info method to return a string with both the color and variety of the 
#  apple.[You will be judged on the use of inheritance and super() over here]



# class Fruit:
#   def __init__(self,color):
#      self.color=color
     
#   def quality(self):
#     return 'Good quality' 
  
  
# class Apple(Fruit):
#   def __init__(self,color,attribute_variety):
#     super().__init__(color)
#     self.attribute_variety=attribute_variety
    
#   def quality(self):
#     return "red and fuji apple" 
  
  
# fruit_object=Fruit(color='red') 

# Apple_object=Apple(color='red',attribute_variety='fuji Apple')  

# print(fruit_object.color)
# print(fruit_object.quality())


# print(Apple_object.color)





#Create class Vegetables with an attribute color and a method info that returns a string.
# Create another class Cucumber that inherits from Fruit and adds an attribute variety. 
# Override the info method to return a string with both the color and variety of the apple.


# class Vegetables:
#   def __init__ (self,attribute_color):
#     self.attribute_color=attribute_color
#   def taste(self):
#     return "bitter_flavor" 
  
# class Cucumber(Fruit):
#   def __init__(self,color,attribute_variety):
#     super().__init__(color)
#     self.attribute_variety=attribute_variety
#   def quality(self):
#     return 'Green and flavor_texture'
  
  
  
# Cucumber_object=Cucumber(color='Green',
#                            attribute_variety= 'flavor_texture')

# print(Cucumber_object.color)
# print(Cucumber_object.quality())

  
  
  
#   Initialize a dictionary dimension with keys length, width, and height.
  

  
  
# class Bed:
#     def __init__(self,color,location ):
#         self.color=color
#         self.location=location
      
# class Mohit(Bed):
#     def __init__(self, color, location,dimension,moveable):
#         super().__init__(color,location)
#         self.dimension=dimension
#         self.moveable=moveable
#     def print_moveable(self):
#         print(self.moveable)    
       
#     def valume(self):
#         return self.dimension['length']*self.dimension['width']*self.dimension['height']           
   
# Mohit_objct=Mohit(color='red',
#                   location='noida',
#                   dimension={'length':4,'width':6,'height':8},
#                   moveable=True)
# print(Mohit_objct.valume())
# print(Mohit_objct.color)
# print(Mohit_objct.location)
# print(Mohit_objct.moveable)






# Write a program to make a class Base, this class only has one attribute, 
# and that is name and has a behavior getName 

# Make another class Child that inherits from the Base class and has another
# attribute age, this class also has a behavior get_age()
# Make another class GrandChild that inherits from Child and has another 
# attribute address, this class also has a behavior getAddress()
# Now initialize 2 GrandChild objects and print age, name, and address


# class Base:
#     def __init__(self,name):
#        self.name=name
      
 
#     def getName(self):
#       return self.name
         
# class Child(Base):
#     def __init__(self,name,age):
#      super().__init__(name)
#      self.age=age
       
#     def get_age(self):
#      return self.age
    
# class  GrandChild(Child):
#     def __init__(self,name,age,address):
#         super().__init__(name,age) 
#         self.address= address 
        
#     def getAddress(self):
#      return  self.address   
# Base_object=Base(name='Rohan')   
# Child_object=Child(name='Rohan',
#                    age=25)   
# GrandChild_object=GrandChild(name='Rohan',
#                    age=25,
#                    address='noida')
# print(GrandChild_object.name)
# print(GrandChild_object.age)
# print(GrandChild_object.getAddress())




# create a class vehicle with start_engine as behavior
# create a class public transport with get tickets as the behavior

# Now inherit these two classes in a class public transport and call those behaviors
# Now inherit these two classes in a class Bus and call those behaviors



# class Vehicle:
    
#     def start_engine(self):
#         return 'start'

# class  Public_transport:
#     def get_ticket(self):
#         return 'ticket'
# class  Bus(Vehicle,Public_transport):
#     pass    
# # bus_object=Bus()

# print(Bus().start_engine())   
# print(Bus().get_ticket())   




# a=1
# b=2
# c=a+b
# c=1+2  



#WAP to create An Employee class that inherits from both a Person class and a Worker class. 
# This would allow the employee to have both personal and professional properties and methods.

# Include name, address in person class as attributes
# include workEmail in employee class
# include shiftTiming as attribute in worker class

# class Person:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def get_name(self):
#         print('alkesh')
        
   
# class Worker:
#     def __init__(self,shiftTiming):
#         self.shiftTiming=shiftTiming
        
#     def get_name(self):
#         print('Murat')    
                


# class Employee(Person,Worker):
#     def __init__(self,name,address,shiftTiming,workEmail):
#         Person.__init__(self,name,address) 
#         Worker.__init__(self,shiftTiming)   
#         self.workEmail=workEmail

# Employee_object=Employee(name='Murat',
#                          workEmail='rammuratyadav224@gmai.com',
#                          address='noida',
#                          shiftTiming='9:00')    
#print(Employee_object.name)  
#print(Employee_object.workEmail) 
#print(Employee_object.address) 
#print(Employee_object.shiftTiming) 
# print('****************')
# print(Employee_object.get_name())  #











# class Employee2(Worker,Person):
#     def __init__(self,name,address,shiftTiming,workEmail):
#         Person.__init__(self,name,address) 
#         Worker.__init__(self,shiftTiming)   
#         self.workEmail=workEmail

# Employee_object=Employee2(name='Murat',
#                          workEmail='rammuratyadav224@gmai.com',
#                          address='noida',
#                          shiftTiming='9:00')  
# Employee_object2=Employee2(name='Murat',
#                          workEmail='rammuratyadav224@gmai.com',
#                          address='noida',
#                          shiftTiming='9:00') 

# print('**********1')   

# print(Employee_object2.get_name())   ###







##########




#WAP to create An ElectricVehicle class that inherits from both a Vehicle class and an ElectricDevice class. 
# This would allow the electric vehicle to have both the properties of a traditional vehicle and those of an 
# electric device. Include attributes in each classes as per your choice


# class Vehicles:
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
        
# class ElectricDevice:
#     def __init__(self,device_name):
#         self.device_name=device_name
        
# class  ElectricVehicle(Vehicles,ElectricDevice):
#     def __init__(self,name,year,device_name,auto):
#      Vehicles. __init__(self,name,year)
#      ElectricDevice.__init__(self,device_name) 
#      self.auto=auto
     
# ElectricVehicle_object=ElectricVehicle(name='bus',
#                                        year=20,
#                                        device_name='remote',
#                                        auto='free')  

# print(ElectricVehicle_object.name)
           
           
           
           
           
           
           
           
           
           
           
           
     








#WAP to create A Smartphone class that inherits from both a Phone class and a Computer class. 
# This would allow the smartphone to have both communication capabilities and computing capabilities. 
# Include attributes in each classes as per your choice


# class Phone:
#     def  communication(self):
#         return  'communication_capabilities'  
    
# class Computer:   
#     def   computing(self):
#         return 'computing_capabilities' 

# class Smartphone(Phone,Computer):
#      def smart_phone(self):
#          return'it has both quality of phone and computer'  
     
# Smartphone_object=Smartphone()    
# print(Smartphone_object.communication())
# print(Smartphone_object.computing())
# print(Smartphone_object.smart_phone())
  


# class Sum:
   
       
#     def add(self,n1,n2,n3=0):
#         return n1+n2+n3
    
        
# Sum_object=Sum()   
# print(Sum_object.add(1,2))     
# # print(Sum_object.n3)


# WAP to create a class Shape that has a method area()
# Now inherit the Shape class and create a class Square that takes in a length and returns the area in area()
# Now inherit the Shape class and create a class Circle that takes in a radius and returns the area in area() 
# formula for area is 3.14*r*r



# class Shape:
   
#     def area(self):
#         return 
# class Square( Shape): 
#     def __init__(self,length):
        
#         self.length=length
#     def area_square(self):
#         return self.length*self.length
# class Circle(Shape):
#     def __init__(self,radius):
      
#         self.radius=radius
#     def area_circle(self):
#         return   3.14*self.radius*self.radius
    
# Circle_object=Circle(radius=5)
# print(Circle_object.area_circle())

# Square_object=Square(length=7)
# print(Square_object.area_square())
              


# Define a class MyNumber and overload the plus operator such that when the following is executed the output is 30 

# num = MyNumber(10)
# result = num + 20
# print(result)


# class MyNumber:
#     def __init__(self,value): 
#         self.value=value
     
#     def __add__ (self,value1): 
#         return  self.value + value1
        
# MyNumber_object=MyNumber(value='a') 
# b='b'  
# print(MyNumber_object+b)     
        
# a=5
# b=6
# c=a+b 
# print(c)
# print(int.__add__(a,b) )  
    
# def my_decorator(alkesh):
#  i=3
#  if i>=0:     
#   def murat():
#     print("Before the function is called.")
#     alkesh()
#     print("After the function is called.")
#   return murat,


# @my_decorator
# def say_hello():
#   print("Hello!")
# say_hello()        


# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(name):
#             for i in range(num_times):
#                 func(name)
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Alice")
        

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self,second):
#         m1=self.m1+second.m1
#         m2=self.m2+second.m2
#         return Student(m1,m2)      
# pass
    
# a =Student(1,2)
# b =Student(13,24)
# d =Student(2,9)

# print(a+b)
# k=c+d
# print(k.m1)






# def my_decorator1(func):
#   def wrapper1():
#     n=input('enter the number')
#     if n == '2345':
#       func()
#     else:
#         print('not match')  
#   return wrapper1
  
# @my_decorator1
# def say_hello():
#   print("Hello!")

# say_hello()


# def my_decorator1(func):
#   def wrapper1():
#     print(func.__name__)
#     func()
#     print("Before the function is called.")
#     print("After the function is called.")
#   return wrapper1

# @my_decorator1
# @my_decorator1
# def say_hello():
#   print("Hello!")

# say_hello()




# def my_decorator1(func1):
#   def wrapper1():
#     print("func_1: ",func1.__name__)
#     func1()
#     print("Before the function is called.")
#     print("After the function is called.")

#   return wrapper1
  
# def my_decorator2(func2):
#   def wrapper2():
#     print("func2:", func2.__name__)
#     func2()
#     print("Before the function is called.")
#     print("After the function is called.")

#   return wrapper2
  
# def my_decorator3(func3):
#   def wrapper3():
#     print(func3.__name__)
#     func3()
#     print("Before the function is called.")
#     print("After the function is called.")
#   return wrapper3


# @my_decorator1
# @my_decorator2
# @my_decorator3
# def say_hello():
#   print("Hello!")

# say_hello()  

    
        
# class Question:
#     count=0
#     def __init__(self,name,classRoll_no,course,collage_name,fav_sub,hobbies,score=0):
#         self.name=name
#         self.classRoll_no=classRoll_no
#         self.course=course
#         self.collage_name=collage_name
#         self.fav_sub=fav_sub
#         self.hobbies=hobbies
#         self.score=score
#     def get_name(self):
#         if self.name=='KRISHNA':
#           count=count+1
#           return count
#     def get_classRoll_no(self):
#         if self.classRoll_no==1:
#           count=count+1
#           return count
#     def get_course(self):
#         if self.course=='B.tech':
#            count=count+1
#            return count
#     def get_collage_name(self):
#         if self.collage_name=='BSSITM':
#            count=count+1
#            return count
#     def get_fav_sub(self):
#         if self.fav_sub=='PYTHON':
#            count=count+1
#            return count
#     def get_hobbies(self):
#         if self.hobbies=='CRICKET':
#            count=count+1
#            return count
  
# question_obj=Question(name="Krishna",classRoll_no=1,course='B.tech',collage_name='BSSITM',fav_sub='PYTHON',hobbies='CRICKET')
# print(question_obj.get_name())
        
              