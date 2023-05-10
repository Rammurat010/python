


# f=open('D:\\python123\A.txt','x')   # empty file
#print('creat A empty file')

# f=open('D:\\python123\B.txt','w')
# f.write('hii murat')
#print('wrote sucessfully')
 
 
# f=open('D:\\python123\B.txt','a')
# f.write(' hii murat')
#print('append sucessfully')


# f=open('D:\\python123\B.txt','a')
# f.write(' \n hii murat')
#print('append sucessfully')


# f=open('D:\\python123\B.txt','r')
# print(f.read(10))
# print(f.readline())
# print(f.readlines())


# with open('D:\\python123\B.txt','r') as f1:
#     with open('D:\\python123\c.txt','w') as f3:
#         for i in f1:
#             f3.write(i)
#print('copy sucessfully')

# f=open('D:\\python123\z.txt','x')
# import os
# if os.path.exists('D:\\python123\z.txt'):
#     os.remove('D:\\python123\z.txt')
#     print('file delete')
# else:
#     print('not found')


#file close
#f.close()

# import os
# os.rmdir('C:\Users\hp\OneDrive\Desktop\DATA')


while(1):
    print("EMPLOYEE MANAGEMENT SYSTEM:")
    print(" 1 for  Addition data :")
    print("2 for show data :")
    print(" 3 for Search  data :")
    print(" 0 for Exit :")
    n=int(input("enter the number :"))
    if n==0:
        break
    elif n==1:
        print("Enter employee details :")
        emp=input("Enter Nname Of employee:")
        dept=input("Enter employee department :")
        id=input("Enter employee ID:")
        sal=input("Enter salary:")
        f=open("D:\\python123\Murat123.txt",'a')
        f.write(emp+"-"+dept+"-"+id+"-"+sal+"\n")
        f.close()
    elif n==2:
        print("details\n")
        f=open("D:\\python123\Murat123.txt",'r')
        for line in f.readlines():
            print(line)
        f.close()
    elif n==3:
        count=0
        search=input("enter employee id:\n")
        f=open("D:\\python123\Murat123.txt",'r')
        for line in f.readlines():
           list=line.split("-")
           if list[2]==search:
                print(list)
                count+=1
        if count==0:
            print("RECORD NOT FOUND:\n")
        f.close()






























# with open('D:\\python123\A.txt','r') as f2:
#     with open('D:\\python123\z.txt','w') as f3:
#         for i in f2:
#             f3.write(i)

# print(' wrote file')
# print('file created')


# [15:20, 2/28/2023] Murat: # a = 5
# b = 0
# try:
#     print(a/i)
# except ZeroDivisionError:
#     print("There was an error while dividing by", b)
# except NameError:
#     print("Name Error")
# a = 5
# b = 0
# try:
#     print(a/b)
# except Exception:
#     print("There was an exception")
# a = 5
# b = 0
# try:
#     print(a/b)
# except Exception as e:
    # print("There was an exception", e)
# a = 5
# b = 0
# try:
#     print(a/b)
# except (NameError,ZeroDivisionError) as e:
#     print("There was an exception", e)
# [15:20, 2/28/2023] Murat: try:
#     print("Resource open")
#     print(5/1)
#     print("HI")
# except Exception as error:
#     print(error)
# else:
#     print("Inside else, try got success")
# finally:
#     print("Resource close")
# [15:20, 2/28/2023] Murat: class DateOfBirthException(Exception):
#     def _init_(self, error_message="There was an error"):
#         self.error_message=error_message
#         super()._init_(self.error_message)
        
# dob = 1990
# try:
#     if dob < 1995:
#     # raise ZeroDivisionError("There was an error")
#         raise DateOfBirthException("New message")
# except DateOfBirthException as e:
#     print(e)
# [15:20, 2/28/2023] Murat: try:
#     print(5/1)
#     try:
#         print(a)
#     except Exception as error:
#         print(error)
# except Exception as error:
#     print(error)
# finally:
#     try:
#         print(5/0)
#     except Exception as error:
#         print(error)




# class DateOfBirthException(Exception):
#     def _init_(self, error_message="There was an error"):
#         self.error_message=error_message
#         super()._init_(self.error_message)
        
# dob = 1999
# try:
#     if dob < 1995:
#     # raise ZeroDivisionError("There was an error")
#         raise DateOfBirthException("New message")
# except DateOfBirthException as e:
#     print(e)

