# Property 데코레이터

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.__name

    def set_name(self, setName):
        self.__name = setName

name = 'hong'
age = 20
grade = 'A'

student = Student(name, age, grade)
print(student.get_name())

# 출력
# hong


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.__name

    def set_name(self, setName):
        self.__name = setName

    name = property(get_name, set_name)

name = 'hong'
age = 20
grade = 'A'

student = Student(name, age, grade)

print(student.name)
student.name = 'jang'
print(student.name)

# 출력
# hong
# jang


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    @property
    def get_name(self):
        return self.__name

    @name.setter
    def set_name(self, setName):
        self.__name = setName


name = 'hong'
age = 20
grade = 'A'

student = Student(name, age, grade)



