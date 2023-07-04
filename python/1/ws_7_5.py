import random

class PairMatch():

    def __init__(self, student_list):

        self.student_list = student_list

    def pick(self,n):

        return random.sample(self.student_list,n)

        """result = set()

        while len(result) < n:

            result.add(random.choice(self.student_list))
        
        return list(result)"""

    def match_pair(self):

        """if len(self.student_list) < 2:

            return None

        result = []

        #홀수인 경우 3명을 먼저 짝을 지어줌

        if len(self.student_list) % 2 == 1:

            random_pick = self.pick(3)

            for student in random_pick:

                self.student_list.remove(student)
            
            result.append(random_pick)
        
        #홀수(3명을 이미 짝 지음)이든 짝수이든 여기까지오면 학생 수는 짝수가 됨
        while len(self.student_list) > 0:

            random_pick = self.pick(2)

            for student in random_pick:

                self.student_list.remove(student)
            
            result.append(random_pick)
        
        return result"""



        match_list = []

        if len(self.student_list) < 2: #처음부터 학생 수가 2보다 작으면 pair가 불가능.. 디테일이 부족했다

            return None
        
        else:

            while self.student_list:

                #처음부터 2명이나 3명일수도 있는데 그런 점을 생각못했네.. 디테일 부족

                if len(self.student_list) == 3 or len(self.student_list) == 2:

                    match_list.append(self.student_list)
                    break
                
                else:

                    two_student = random.sample(self.student_list,2)

                    match_list.append(two_student)

                    for a in two_student:

                        self.student_list.remove(a)
            
            
            return match_list

student_list1 = ['윤대혁','박현영','김예은','김기윤','정하림','정무남','정채은']

student_list2 = ['윤대혁','박현영','김예은','김기윤','정하림','정채은']

student_list3 = ['윤대혁','박현영','김예은']

student_list4 = ['윤대혁','박현영']

pair_match1 = PairMatch(student_list1)
pair_match2 = PairMatch(student_list2)
pair_match3 = PairMatch(student_list3)
pair_match4 = PairMatch(student_list4)

print('match1')
print(pair_match1.pick(3))
print(pair_match1.match_pair())

print('match2')
print(pair_match2.pick(2))
print(pair_match2.match_pair())

print('match3')
print(pair_match3.pick(1))
print(pair_match3.match_pair())

print('match4')
print(pair_match4.pick(1))
print(pair_match4.match_pair())


