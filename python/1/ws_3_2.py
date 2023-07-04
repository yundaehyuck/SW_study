
s = input('문자열을 입력하세요 : ')

len_s = len(s)

mid = int(len_s/2)

if len_s % 2 == 0:

    print(s[mid-1]+s[mid])

else:

    print(s[mid])
