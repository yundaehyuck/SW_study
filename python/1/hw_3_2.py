
year = int(input('윤년인지 알고싶은 연도를 입력하세요 : '))

cond1 = (year % 4 == 0) and (year % 100 != 0)

cond2 = (year % 400 == 0)

if cond1 or cond2:

    print('윤년입니다.')

else:

    print('윤년이 아닙니다.')
