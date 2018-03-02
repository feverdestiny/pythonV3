# 类和继承



# class Myclass:
#     def __init__(self, replate, img):
#         self.r = replate
#         self.i = img
#
#     def f(self):
#         return 'hello world'
#
#
# x = Myclass(3, 2)
# print(x.i)
# print(x.f())
# print(x.r)

# class Person:
#     age: 0
#     name: ''
#     __weight: 0
#
#     def __init__(self, a, n, w):
#         self.age = a
#         self.name = n
#         self.__weight = w
#
#     def speak(self):
#         print('我是%s，今年%d，体重%dkg' % (self.name, self.age, self.__weight))
#
#
# # Person(18, 'lxi', 20).speak()
#
# class Student(Person):
#     grad: ''
#
#     def __init__(self, a, n, w, g):
#         Person.__init__(self, a, n, w)
#         self.grad = g
#
#     def speak(self):
#         print('我是%s，今年%d，我在读%d年级' % (self.name, self.age, self.grad))
#
#
# Student(18, 'lix', 20, 6).speak()


import calendar

yy = int(input('请输入年:'))
mm = int(input('请输入月:'))
print(calendar.month(yy, mm))
