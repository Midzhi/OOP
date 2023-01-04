# # 3 1-балл
# Students room:
# Реализуйте студенческую комнату с помощью ООП:
#
# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)

class Student:

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return str(self.__dict__)


Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve)
print(Johnny)
print(Penny)
