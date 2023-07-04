
#첨부파일

students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']


vote_dict = {}

for student in students:

    vote_dict[student] = vote_dict.get(student,0) + 1


#득표수가 많은 순서대로 내림차순 정렬
#득표수가 동일하면 이름순으로 오름차순 정렬

sort_vote_dict = sorted(vote_dict.items(), key = lambda item:[-item[1],item[0]])

for student,vote in sort_vote_dict:

    print(student)
