#첨부파일
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

#리스트에서 튜플의 첫번째인 가격을 기준으로 내림차순 정렬
sort_grain_lst = sorted(grain_lst,key=lambda item:-item[1])

#가장 가격이 높은 0번째 원소의 튜플에서 작물 이름인 0번째를 출력
print(sort_grain_lst[0][0])
