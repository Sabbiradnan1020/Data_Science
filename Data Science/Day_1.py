# name="Rahim"
# age=25
# height=5.9
# is_student=True
# print(name,age,height,is_student)




# name=input("Enter Your name :")
# age=int(input("Enter Your age :"))
# print("Enter name:",name)
# print("Enter age:",age)


# age=int(input("What is Your old :"))
# if age>=18:
#     print("You Are Adult And Man")
# elif age>=13:
#     print("Your are a child")
# else:
#     print("Your a baby")



# age=int(input("What is Your Old ?"))
# if age>=18:
#     print("You are a voter")
# else:
#     print("You are a not eligible")
# name=input("Enter your name")
# print("Hello",name+'!')

# for i in range(1,9):
#     print("Number :",i)

# i=1
# while i<=5:
#     print("Number:",i)
#     i+=1


# List

# fruits=['Apple','Banana','Mango','Pinaple','Strabewary','Juck']
# # print(fruits[5])
# # fruits.append('Orange')
# # print(fruits)

# for fruit in fruits:
#     print("I like",fruit)
  

# tuple

# colars=('Red','Green','Blue','SkyBlue')
# print(colars[0])


# Set

# numbers={1,2,3,4,5,6,2}
# print(numbers)


# Dictionary

# student={
#     'Name':"Korim",
#     'Roll':1,
#     'Grade':'A+',
#     'Father_Name':'Jobbar',
#     'Martial_Staues':'Single'
# }
# # print(student['Roll'])
# for key,value in student.items():
#     print(key,":",value)



# total =0
# for i in range(1,101):
#     total+=i
# print('Total Sum:',total)



# names=[]
# for i in range(5):
#     name=input("Enter the Name:")
#     names.append(name)
# print("Enter the show Your Name:",names)

# student={}
# student["name"]=input("Enter the student name :")
# student['Marks']=int(input("Enter the student Marks :"))
# print(student)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num%2==0:
#         print("Even :",num)


# def great():
#     print("Hello, Friends")
# great()    

# def great_user(name):
#     print("Hello",name)
# great_user("Rahim")


# def add(a,b):
#     return a+b
# result=add(7,8)
# print(result)


# def sum(a,b):
#     return a+b
# result=sum(10,60)
# print(result)


# def check_eligiable(age):
#     if age>=18:
#         return 'Eligiable'
#     else:
#         return 'Not Eligibale'
# print(check_eligiable(90))


# def celcius_to_farenhaite(c):
#     return(c*9/5)+32
# tem=float(input("C tempeturte"))
# print('F',celcius_to_farenhaite(tem))

# Writing to the file
# with open("info.txt", 'w') as file:
#     file.write("My name is Tahim\n")
#     file.write("I am learning Python")

# # Reading from the file and showing output
# with open("info.txt", 'r') as file:
#     content = file.read()
#     print(content)

# with open("info.txt",'a')as file:
#     file.write("\n")

# import csv

# with open('F:/Data Science/students_data.csv', 'r') as file:

#     render = csv.reader(file)
#     for row in render:
#         print(row)

# class Student:
#     def say_hello(self):
#         print('Hello,I am a Student')
# s1=Student()
# s1.say_hello()


# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_task(self):
#         print(f'Name: {self.name} , Old:{self.age}')
# s1=Student('Rahim',23)    
# s1.display_task()
# s2=Student('Korim',34)
# s2.display_task()

# class Student:
#     def __init__(self,Name,Marks):
#         self.Name=Name
#         self.Marks=Marks
#     def cheak_grade(self):
#         if self.Marks>=80:
#             grade='A'
#         elif self.Marks>=60:
#             grade='B'
#         elif self.Marks>=40:
#             grade='C'
#         else:
#             grade='F'
#         print(f'Name:{self.Name} , Marks:{self.Marks}')
# s1=Student('Jobbar',90)
# s1.cheak_grade()



# class Book:
#     def __init__(self,name,author):
#         self.name=name
#         self.author=author
#     def show_info(self):
#         print(f'Name:{self.name} , Author:{self.author}')
# s1=Book('Waiting','Humayan Ahmed')
# s1.show_info()
    

# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount

#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#         else:
#             print('Efficient Balance')
#     def show_balance(self):
#         print(f'{self.name} and balance :{self.balance}')
# s1=Bankaccount('Anisur',5000)
# # s1.deposit(5000)        
# s1.show_balance()   
# s1.withdraw(3000)
# s1.show_balance()
# s1.deposit(10000)
# s1.show_balance()


# class Student: 
#     def __init__(self, name, id, marks):
#         self.name = name
#         self.id = id
#         self.marks = marks  
#         self.grade = None

#     def calculate_grade(self):
#         avg = sum(self.marks.values()) / len(self.marks)
#         if avg >= 90:
#             self.grade = 'A+'
#         elif avg >= 70:
#             self.grade = 'A'
#         elif avg >= 50:
#             self.grade = 'B+'
#         elif avg >= 33:
#             self.grade = 'D'
#         else:
#             self.grade = 'F'

#     def show_details(self):
#         print(f'Name: {self.name}, ID: {self.id}')
#         print("Marks:")
#         for subject, mark in self.marks.items():
#             print(f'Subject: {subject}, Mark: {mark}')
#         print(f'Overall Grade: {self.grade}')
    

# s1=Student('ANis','CSE1102',{'MAth ':92,'English':100,'Bangla':96})
# s1.calculate_grade()
# s1.show_details()

