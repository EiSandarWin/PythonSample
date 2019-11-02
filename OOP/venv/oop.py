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
#         if Dog.population == 0
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There are still {:d} dogs to feed.".format(Dog.population))





