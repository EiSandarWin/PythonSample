#class Person:
   # pass
#p = Person()
#print(p)

#Methods
#class Person:
#    def say_hi(self):
 #       print('Hello,how are you')

#p = Person()
#p.say_hi()

#__init__method
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#    def say_hi(self):
#         print('Hello, my name is ',self.name)
#
# p = Person('Ei Sandar Win')
# p.say_hi()

# class Dog:
#     def __init__(self,name):
#        self.name = name
#
#    def say_name(self):
#         print('Dog name is',self.name)
#
#
#     def say_color(self):
#         print('Dog color is', self.color)
#
#     def say_color(self):
#         print('Owner is', self.owner)
# p = Dog('Rambo')
#
#
# d = dog ('Name')
# d.dogcolor('Black')
# d.dogowner('Ukaung')

# p.say_name()
# p.say_color()
# p.say_owner()

# class Robot:
#
#     population = 0
#     def __init__(self,name):
#         self.name = name
#         print("(Initializing{})".format(self.name))
#         Robot.population += 1
#
#     def die(self):
#         print("{} is being destroyyed!".format(self.name))
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There ar still {:d} robots working.".format(Robot.population))
#
#     def say_hi(self):
#         print("Greetings,my sisters call me{}.".format(self.name))
#
#     @classmethod
#     def how_many(cls):
#         print("We have {:d} robots.".format(cls.population))
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# Robot.how_many()
#
# droid3 = Robot('Q-35')
# droid3.say_hi()
# Robot.how_many()
#
# print("\nRobots can do some work here.\n")
#
# print("Robots have finished their work.so let's destroy them")
# droid1.die()
# droid2.die()
# droid3.die()
#
# Robot.how_many()

# class Dog:
#     population = 0
#     def __init__(self,name):
#         self.name = name
#         print("(Initializing{}".format(self.name))
#         Dog.population += 1
#
#     def free(self):
#         print("{} is being free!".format(self.name))
#         Dog.population -= 1
#
#         if Dog.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There are still {:d} dogs to feed.".format(Dog.population))
#
#     def say_hi(self):
#         print("Greetings,They call me{}.".format(self.name))
#     @classmethod
#     def how_many(cls):
#         print("We have {:d} dogs.".format(cls.population))
#
#
# droid1 = Dog("Bo Kyar")
# droid1.say_hi()
# Dog.how_many()
#
# droid2 = Dog("Aung Nat")
# droid2.say_hi()
# Dog.how_many()
#
# droid3 = Dog("Piggy")
# droid3.say_hi()
# Dog.how_many()
#
# print("\nDog eat their feed.\n")
# print("Dogs have finished their eating.so lets they free")
# droid1.free()
# droid2.free()
# droid3.free()

# class SchoolMember:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Initialized SchoolMember: {})'.format(self.name))
#     def tell(self):
#         print('Name:"{}" Age:"{}"'.format(self.name, self.age),end="")
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Initialized Student:{}'.format(self.name))
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks:"{:d}"'.format(self.marks))
#
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Initialized Student:{}'.format(self.name))
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks:"{:d}"'.format(self.marks))
#
# t = Teacher('Mrs. Shriidya', 40, 30000)
# s = Student('Swaroop', 25, 75)
#
# print()
#
# members =[t,s]
# for member in members:
#     member.tell()

class Dog:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('(Initialized Dog:{})'.format(self.name))

    def bark(self):
        print('Name:"{}" Age:"{}" Gender:"{}"'.format(self.name,self.age,self.gender),end="")

class Shamoyed(Dog):
    def __init__(self,name,age,gender,child):
        Dog.__init__(self,name,age,gender)
        self.child = child
        print('(Initialized Dog:"{}"'.format(self.name))

    def bark(self):
        Dog.bark(self)
        print('Child:"{:d}"'.format(self.child))

class GoldenRetriver(Dog):
    def __init__(self, name, age, gender, child):
        Dog.__init__(self, name, age, gender)
        self.child = child
        print('(Initialized Dog:"{}"'.format(self.name))

    def bark(self):
        Dog.bark(self)
        print('Child:"{:d}"'.format(self.child))


class Husky(Dog):
    def __init__(self, name, age, gender, child,master):
        Dog.__init__(self, name, age, gender)
        self.child = child
        self.master = master
        print('(Initialized Dog:"{}"'.format(self.name))

    def bark(self):
        Dog.bark(self)
        print('Child:"{:d}"'.format(self.child,self.master))

s = Shamoyed('Bo Bo', 4, 'Female', 4)
g = GoldenRetriver('Shaung Shaung', 3, 'Male', 1)
h = Husky('Ki Ki', 6, 'Female', 2, 2)

print()
members = [s, g, h]
for member in members:
    member.bark()



