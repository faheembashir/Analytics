class Car:
    pass

car1 = Car()


# class Student:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
  
#     def hello(self):
#         print(self.name,self.age)

# s1 = Student("Faheem",22)
# s1.hello()


employees={
  1:  {"name":"faheem", "salary":50000},
  2:  {"name":"Rahil", "salary":80000},
   3: {"name":"zahid", "salary":100000},
   4: {"name":"shahid", "salary":90000},
}

total_salary=0
for i in range(1,len(employees)+1):
    total_salary=total_salary+employees[i]["salary"]
print(total_salary/len(employees))
   