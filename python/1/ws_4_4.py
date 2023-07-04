
#첨부파일

word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

word1_sum = 0
word2_sum = 0

for c in word1:

    word1_sum += ord(c)

for c in word2:
    
    word2_sum += ord(c)


if word1_sum > word2_sum:

    print(word1)

elif word1_sum < word2_sum:

    print(word2)

else: #아스키코드 값의 합이 서로 같으면 2개 다 반환

    print(word1,word2)
