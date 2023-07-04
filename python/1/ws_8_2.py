
class Person:

    name = ''
    year = 0

    def __init__(self,name,age):

        self.name = name
        self.age = age
    
    @classmethod
    def details(cls,name,year):

        cls.name = name
        cls.year = year

        today_year = 2022
        age = today_year - cls.year + 1

        return cls(name,age)
    
    def check_age(self):

        if self.age < 19:

            return True
        
        else:

            return False

#생성자 활용

p1 = Person('daehyuck',29)

print("init:",p1.name, p1.age)
print(p1.check_age())

#class method이용

p2 = Person.details('daehyuck',1994)

print("class method:", p2.name,p2.age)
print(p2.check_age())
