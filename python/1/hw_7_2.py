class Doggy():

    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self,name,breed):

        self.name = name
        self.breed = breed

        ##instance를 생성하면 개가 태어나는거니까

        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1 
    
    def __del__(self):
        #instance를 삭제하면 개가 죽는거니까
        Doggy.num_of_dogs -= 1

    def bark(self):

        print("멍멍")
    
    @classmethod
    def get_status(cls):

        print(f"살아있는 개의 수: {cls.num_of_dogs}, 태어난 개의 수: {cls.birth_of_dogs}")

dog1 = Doggy('a','A')
dog2 = Doggy('b','B')
dog3 = Doggy('c','C')

dog1.bark()
dog2.bark()
dog3.bark()

Doggy.get_status()

del dog1

print("dog1 죽음")
Doggy.get_status()

    
