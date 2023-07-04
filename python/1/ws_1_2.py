total_num = int(input('게시글의 총 개수를 입력하세요 : '))

num_per_one = int(input('한 페이지에 필요한 게시글의 수를 입력하세요 : '))

page_num = int(total_num/num_per_one)

print(page_num)
