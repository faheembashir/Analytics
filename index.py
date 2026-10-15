# import numpy as np 
# a=np.array([10,23,32,55,21])
# print(a.mean())   
# print("hello world")


# def add(a, b):
#     return a + b

# result=add(10,5)
# print(result)

# def outer():
#     print("This is outer function")
#     def inner():
#         print("This is inner function")
#     inner()
# outer()
# add = lambda a, b: a + b

# print(add(10, 20))

# even=lambda x: "even" if x%2==0 else "odd"
# print(even(4))

# greter=lambda a,b: a if a>b else b
# print(greter(100,20))


lt=[10,2,50,5,6,3]
# newLt=[]
# for i in lt:
#     res=i+i
#     newLt.append(res)
# print(newLt)


students = [
    10,25,23,20
]

# students.sort(key=lambda student: student[1],reverse=True)+
students.sort(reverse=True)

print(students)